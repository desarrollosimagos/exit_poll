#encoding:utf-8
import class_pdf
import sys
import time
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files


def reporte_listado_exit_datallado(desde,hasta):

        reload(sys)
        fecha_hora = time.strftime("%d/%m/%Y")
        fecha = time.strftime("%d-%m-%Y")
        sys.setdefaultencoding("utf-8")
        #todo = kwargs.get('todo', None)
        #desde = kwargs.get('from_date', None)
        #hasta = kwargs.get('to_date', None)

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(19,10,10)  # MARGENE DEL DOCUMENTO

        pdf.set_fill_color(255,255,255)
        pdf.set_font('Arial','B',12)

        pdf.cell(180,5," Listado Detallado de Exit Polls desde el "+str(desde)+" "+"hasta el "+str(hasta),'',1,'C',1)
        pdf.ln(5)

        # Fila de la cabezara de la tabla
        pdf.set_fill_color(0,121,194)
        pdf.set_text_color(255,255,255)
        pdf.cell(15,10,"N°".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(125,10,"Exit Poll".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(40,10,"Votos".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)

        cursor = connection.cursor()
        sql_ele = "SELECT v.eleccion_id, e.nombre, COUNT(v.id) total FROM votacion_votacion v"
        sql_ele += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_ele += " WHERE e.fecha_create  between %s and %s"
        sql_ele += " GROUP BY e.nombre, v.eleccion_id "

        cursor.execute(sql_ele,[desde,hasta])
        row = dictfetchall(cursor)

        nombre = row[0]['nombre']
        total = row[0]['total']
        eleccion_id = row[0]['eleccion_id']
        i = 0
        k = 0
        j = 0
        item = 0

        for t in row:
            eleccion_id = t['eleccion_id']
            pdf.set_fill_color(255,255,255)
            if j == 1:
                    pdf.add_page()
                    pdf.set_fill_color(255,255,255)
                    pdf.set_font('Arial','B',12)
                    pdf.cell(180,5," Listado de Exit Polls desde el "+str(desde)+" "+"hasta el "+str(hasta),'',1,'C',1)
                    pdf.ln(5)
                    
                    # Fila de la cabezara de la tabla
                    pdf.set_fill_color(0,121,194)
                    pdf.set_text_color(255,255,255)
                    pdf.cell(15,10,"N°".decode("UTF-8"),'LTBR',0,'C',1)
                    pdf.cell(125,10,"Exit Poll".decode("UTF-8"),'LTBR',0,'C',1)
                    pdf.cell(40,10,"Votos".decode("UTF-8"),'LTBR',1,'C',1)
                    pdf.set_fill_color(255,255,255)
                    
                    j=0

            item = int(item) + 1
            # Filas que vienen de la BD
            pdf.set_font('Arial','B',11)
            pdf.set_fill_color(217,236,247)
            pdf.set_text_color(24,29,31)
            pdf.cell(15,8,str(item).decode("UTF-8"),'LTBR',0,'C',1)
            pdf.cell(125,8,str(t['nombre']).decode("UTF-8"),'LTBR',0,'L',1)
            pdf.cell(40,8,str(t['total']),'LTBR',1,'C',1)
            pdf.set_fill_color(255,255,255)
            pdf.set_font('Arial','B',10)

            #pdf.set_text_color(255,255,255)
            pdf.cell(15,8,"".decode("UTF-8"),'LTR',0,'C',1)
            pdf.set_fill_color(191,191,191)
            pdf.cell(10,8,"N°".decode("UTF-8"),'LTBR',0,'C',1)
            pdf.cell(30,8,"Cédula".decode("UTF-8"),'LTBR',0,'C',1)
            pdf.cell(85,8,"Candidato".decode("UTF-8"),'LTBR',0,'C',1)
            pdf.cell(40,8,"Votos".decode("UTF-8"),'LTBR',1,'C',1)
            pdf.set_fill_color(255,255,255)
            pdf.set_text_color(24,29,31)


            sql_exit = "SELECT c.cedula, CONCAT(c.nombre,' ',c.apellido) nom_ape, e.nombre, COUNT(v.id) total, v.candidatos_id id_c "
            sql_exit += " FROM votacion_votacion v"
            sql_exit += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
            sql_exit += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
            sql_exit += " WHERE v.eleccion_id=%s GROUP BY v.eleccion_id, c.nombre, c.apellido, e.nombre, c.cedula, v.candidatos_id ORDER BY total DESC"

            cursor.execute(sql_exit,[eleccion_id])
            row = dictfetchall(cursor)

            cedula = row[0]['cedula']
            nom_ape = row[0]['nom_ape']
            total = row[0]['total']

            item2 = 0
            for h in row:
                id_c = h['id_c']
                pdf.set_text_color(24,29,31) # COLOR DE BOLDE DE LA CELDA

                item2 = int(item2) + 1
                pdf.set_text_color(255,255,255)
                pdf.cell(15,6,"".decode("UTF-8"),'LR',0,'C',1)
                pdf.set_fill_color(127,127,127)
                pdf.cell(10,6,str(item2).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(30,6,str(h['cedula']).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(85,6,str(h['nom_ape']).decode("UTF-8"),'LTBR',0,'L',1)
                pdf.cell(40,6,str(h['total']),'LTBR',1,'R',1)
                pdf.set_fill_color(255,255,255)

                pdf.set_text_color(24,29,31)
                pdf.set_font('Arial','B',10)
                pdf.cell(15,6,"".decode("UTF-8"),'LR',0,'C',1)
                pdf.cell(10,6,"".decode("UTF-8"),'LTR',0,'C',1)
                pdf.set_fill_color(226,219,219)
                pdf.cell(15,6,"N°".decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(100,6,"Grupo Etáreo".decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(40,6,"N° de Votos".decode("UTF-8"),'LTBR',1,'C',1)

                sql_gru = " SELECT CONCAT (g.descripcion,' (',g.desde,'-',g.hasta,' Años)') descripcion, "
                sql_gru += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total, "
                sql_gru += " ROUND ((SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer)*100.0 / "
                sql_gru += " (SELECT COUNT (v.grupo_etareo) FROM votacion_votacion v WHERE v.eleccion_id=%s and candidatos_id=%s), 2) porcentaje "
                sql_gru += " FROM grupo_etareo_grupo_etareo AS g ORDER BY porcentaje DESC"
                cursor.execute(sql_gru,[eleccion_id,id_c,eleccion_id,id_c,eleccion_id,id_c])

                row = dictfetchall(cursor)

                descripcion = row[0]['descripcion']
                total = row[0]['total']

                item3 = 0
                for p in row:
                    pdf.set_fill_color(255,255,255) # COLOR DE BOLDE DE LA CELDA
                    pdf.set_font('Arial','',10)
                    item3 = int(item3) + 1
                    pdf.set_text_color(24,29,31)
                    pdf.cell(15,6,"".decode("UTF-8"),'LR',0,'C',1)
                    pdf.cell(10,6,"".decode("UTF-8"),'LR',0,'C',1)
                    pdf.cell(15,6,str(item3).decode("UTF-8"),'LTBR',0,'C',1)
                    pdf.cell(100,6,str(p['descripcion']).decode("UTF-8"),'LTBR',0,'L',1)
                    pdf.cell(40,6,str(p['total']),'LTBR',1,'R',1)
                    pdf.set_font('Arial','B',10)
                    pdf.set_fill_color(255,255,255)

            i =i+1
            j =j+1
            pdf.cell(180,1,"",'T',0,'L',1)

        ruta_reporte = settings.MEDIA_PDF
        nombre = 'Listado de Exit Polls Detallados al '+str(desde)+" "+"hasta el "+str(hasta)+'.pdf'
        pdf.output(ruta_reporte+'/'+nombre, 'F')
        archivo = open(ruta_reporte+'/'+nombre, "r")

        ruta = ruta_reporte+'/'
        delete_Files(ruta)
        
        return nombre, archivo

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
