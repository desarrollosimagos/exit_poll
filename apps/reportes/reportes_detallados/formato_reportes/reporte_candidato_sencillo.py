#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files


def detallado_candidato_sencillo(candidato):

        reload(sys)
        sys.setdefaultencoding("utf-8")

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(19,10,10)  # MARGENE DEL DOCUMENTO

        pdf.set_fill_color(255,255,255)
        pdf.set_font('Arial','B',12)

        cursor = connection.cursor()
        sql_cand = "SELECT CONCAT(nombre,' ',apellido) nom_ape FROM candidatos_candidatos "
        sql_cand += " WHERE id=%s "
        cursor.execute(sql_cand, [candidato])
        row = dictfetchall(cursor)
        nom_ape = row[0]['nom_ape']

        pdf.cell(180,5,"Listado de Exit Polls que participo: "+str(nom_ape).decode("UTF-8"),'',1,'C',1)
        pdf.ln(5)

        cursor = connection.cursor()
        sql_id = "SELECT CONCAT(c.nombre,' ',c.apellido) nom_ape, v.eleccion_id id_e"
        sql_id += " FROM candidatos_candidatos c"
        sql_id += " INNER JOIN votacion_votacion v ON v.candidatos_id = c.id "
        sql_id += " WHERE c.id=%s GROUP BY c.nombre, c.apellido, v.eleccion_id "
        cursor.execute(sql_id, [candidato])
        row = dictfetchall(cursor)

        # Fila de la cabezara de la tabla
        pdf.set_fill_color(0,121,194)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial','B',11)
        pdf.cell(10,8,"N°".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(100,8,"Exit Poll".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(25,8,"Obtenidos".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(25,8,"Totales".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,8,"%".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)

        for m in row:
            id_e = m['id_e']
            
            cursor = connection.cursor()
            sql_res = "SELECT e.nombre eleccion,"
            sql_res += " COUNT(v.candidatos_id) total_c,(SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s) total_v,"
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s), 2) porcentaje"
            sql_res += " FROM votacion_votacion v"
            sql_res += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
            sql_res += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
            sql_res += " WHERE v.candidatos_id=%s and v.eleccion_id=%s GROUP BY e.nombre "
            cursor.execute(sql_res, [id_e, id_e, candidato, id_e])
            row = dictfetchall(cursor)
            eleccion = row[0]['eleccion']
            total_c = row[0]['total_c']
            total_v = row[0]['total_v']
            porcentaje = row[0]['porcentaje']

            item = 0
            for p in row:
                item = int(item) + 1
                pdf.set_text_color(24,29,31)
                pdf.set_font('Arial','',9)
                pdf.cell(10,6,str(item).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(100,6,str(p['eleccion']).decode("UTF-8"),'LTBR',0,'L',1)
                pdf.cell(25,6,str(p['total_c']).decode("UTF-8"),'LTBR',0,'R',1)
                pdf.cell(25,6,str(p['total_v']).decode("UTF-8"),'LTBR',0,'R',1)
                pdf.cell(20,6,str(p['porcentaje'])+' %'.decode("UTF-8"),'LTBR',1,'R',1)

        
        ruta_reporte = settings.MEDIA_PDF
        nombre = str(nom_ape)+' Sencillo.pdf'
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