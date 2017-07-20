#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files


def detallado_eleccion_detallado(detallado,tipo,estado,circuito,municipio):

        reload(sys)
        sys.setdefaultencoding("utf-8")

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(19,10,10)  # MARGENE DEL DOCUMENTO

        cursor = connection.cursor()
        sql_ele = "SELECT e.nombre FROM votacion_votacion v INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id "
        sql_ele += " WHERE v.eleccion_id=%s GROUP BY e.nombre "
        cursor.execute(sql_ele, [detallado])
        row = dictfetchall(cursor)
        eleccion = row[0]['nombre']
        
        pdf.ln(1)
        pdf.set_fill_color(255, 255, 255)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(180,5,eleccion.decode("UTF-8"),'',1,'C',1)
        pdf.set_font('Arial', 'B', 10)
        if tipo == '2':
                sql_estado = "SELECT estado FROM estados_estado WHERE id=%s"
                cursor.execute(sql_estado, [estado])
                est = dictfetchall(cursor)
                nom_estado = est[0]['estado']
                pdf.cell(15,5,"Estado:".decode("UTF-8"),'',0,'L',1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(90,5,str(nom_estado).decode("UTF-8"),'',1,'L',1)
        elif tipo == '3':
                sql_circuito = "SELECT c.n_circuito, e.estado FROM circuitos_circuito AS c "
                sql_circuito += " INNER JOIN estados_estado AS e ON e.id = c.estado_id "
                sql_circuito += " WHERE c.id=%s"
                cursor.execute(sql_circuito, [circuito])
                cir = dictfetchall(cursor)
                n_circuito = cir[0]['n_circuito']
                nom_estado = cir[0]['estado']
                pdf.cell(15,5,"Estado:".decode("UTF-8"),'',0,'L',1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(90,5,str(nom_estado).decode("UTF-8"),'',1,'L',1)
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(15,5,"Circuito:".decode("UTF-8"),'',0,'L',1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(90,5,str(n_circuito).decode("UTF-8"),'',1,'L',1)
        elif tipo == '4':
                sql_municipio = "SELECT c.n_circuito, e.estado, m.municipio FROM municipios_municipio AS m "
                sql_municipio += " INNER JOIN circuitos_circuito AS c ON c.id = m.circuito"
                sql_municipio += " INNER JOIN estados_estado AS e ON e.id = c.estado_id"
                sql_municipio += " WHERE m.id=%s"
                cursor.execute(sql_municipio, [municipio])
                mun = dictfetchall(cursor)
                n_circuito = mun[0]['n_circuito']
                nom_estado = mun[0]['estado']
                nom_municipio = mun[0]['municipio']
                pdf.cell(14,5,"Estado:".decode("UTF-8"),'',0,'L',1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(90,5,str(nom_estado).decode("UTF-8"),'',1,'L',1)
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(16,5,"Circuito:".decode("UTF-8"),'',0,'L',1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(90,5,str(n_circuito).decode("UTF-8"),'',1,'L',1)
                pdf.set_font('Arial', 'B', 10)
                pdf.cell(18,5,"Municipio:".decode("UTF-8"),'',0,'L',1)
                pdf.set_font('Arial', '', 10)
                pdf.cell(90,5,str(nom_municipio).decode("UTF-8"),'',1,'L',1)
        
        pdf.ln(5)

        # Fila de la cabezara de la tabla
        pdf.set_fill_color(0,121,194)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial','B',11)
        pdf.cell(15,10,"N°".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(105,10,"Candidatos".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(40,10,"N° de Votos".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,10,"%".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.set_font('Arial','',10)

        pdf.set_font('Arial','',10) # TAMANO DE LA FUENTE
        sql_res = "SELECT CONCAT(c.nombre,' ',c.apellido) nom_ape, COUNT(v.candidatos_id) can_v, v.candidatos_id id_c,"
        if tipo == '1':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s), 2) porcentaje"
        elif tipo == '2':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.estado="+str(estado)+"), 2) porcentaje"
        elif tipo == '3':
            sql_res += " ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.circuito="+str(circuito)+"), 2) porcentaje"
        else:
            sql_res += "ROUND (COUNT (v.candidatos_id) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.municipio="+str(municipio)+"), 2) porcentaje"
        sql_res += " FROM votacion_votacion v "
        sql_res += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_res += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
        if tipo == '1':
            sql_res += " WHERE v.eleccion_id=%s "
        elif tipo == '2':
            sql_res += " WHERE v.eleccion_id=%s AND v.estado="+str(estado)+""
        elif tipo == '3':
            sql_res += " WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+""
        else:
            sql_res += " WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+""
        sql_res += " GROUP BY v.candidatos_id, c.nombre, c.apellido ORDER BY porcentaje DESC"
        cursor.execute(sql_res, [detallado,detallado])
        j = 0
        item = 0
        row = dictfetchall(cursor)
        nom_ape = row[0]['nom_ape']
        can_v = row[0]['can_v']
        porcentaje = row[0]['porcentaje']

        pdf.set_fill_color(255, 255, 255)
        i = 1
        for t in row:
                id_c = t['id_c']
                pdf.set_fill_color(255,255,255)
                if j == 5:
                        pdf.add_page()
                        pdf.set_fill_color(255,255,255)
                        pdf.set_font('Arial','B',12)
                        pdf.cell(180,5,eleccion.decode("UTF-8"),'',1,'C',1)
                        pdf.ln(5)
                        # Fin Cabezera
                        j=0
                item = int(item) + 1
                # Filas que vienen de la BD
                pdf.set_fill_color(0,0,0)
                pdf.cell(180,1,"",'LTBR',1,'C',1)
                pdf.set_font('Arial','B',11)
                pdf.set_fill_color(217,236,247)
                pdf.set_text_color(24,29,31)
                pdf.cell(15,8,str(item).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(105,8,str(t['nom_ape']).decode("UTF-8"),'LTBR',0,'L',1)
                pdf.cell(40,8,str(t['can_v']),'LTBR',0,'R',1)
                pdf.cell(20,8,str(t['porcentaje'])+' %','LTBR',1,'R',1)

                pdf.set_font('Arial','B',10)
                pdf.set_fill_color(255,255,255)
                pdf.cell(15,6,"".decode("UTF-8"),'LTR',0,'C',1)
                pdf.set_fill_color(191,191,191)
                pdf.cell(15,6,"N°".decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(90,6,"Grupo Etáreo".decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(40,6,"N° de Votos".decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(20,6,"%".decode("UTF-8"),'LTBR',1,'C',1)

                sql_res = " SELECT CONCAT (g.descripcion,' (',g.desde,'-',g.hasta,' Años)') descripcion, "
                if tipo == '1':
                        sql_res += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total, "
                        sql_res += " ROUND ((SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer)*100.0 / "
                        sql_res += " (SELECT COUNT (v.grupo_etareo) FROM votacion_votacion v WHERE v.eleccion_id=%s and candidatos_id=%s), 2) porcentaje "
                elif tipo == '2':
                        sql_res += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND estado="+str(estado)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total, "
                        sql_res += " ROUND ((SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND estado="+str(estado)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer)*100.0 / "
                        sql_res += " (SELECT COUNT (v.grupo_etareo) FROM votacion_votacion v WHERE v.eleccion_id=%s and candidatos_id=%s AND estado="+str(estado)+"), 2) porcentaje "
                elif tipo == '3':
                        sql_res += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND circuito="+str(circuito)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total, "
                        sql_res += " ROUND ((SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND circuito="+str(circuito)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer)*100.0 / "
                        sql_res += " (SELECT COUNT (v.grupo_etareo) FROM votacion_votacion v WHERE v.eleccion_id=%s and candidatos_id=%s AND circuito="+str(circuito)+"), 2) porcentaje "
                elif tipo == '4':
                        sql_res += " (SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND municipio="+str(municipio)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer) total, "
                        sql_res += " ROUND ((SELECT COUNT (grupo_etareo) from votacion_votacion WHERE eleccion_id=%s and candidatos_id=%s AND municipio="+str(municipio)+" AND grupo_etareo BETWEEN g.desde::integer AND g.hasta::integer)*100.0 / "
                        sql_res += " (SELECT COUNT (v.grupo_etareo) FROM votacion_votacion v WHERE v.eleccion_id=%s and candidatos_id=%s AND municipio="+str(municipio)+"), 2) porcentaje "
                sql_res += " FROM grupo_etareo_grupo_etareo AS g ORDER BY porcentaje DESC"
                cursor.execute(sql_res,[detallado,id_c,detallado,id_c,detallado,id_c])
                row = dictfetchall(cursor)

                descripcion = row[0]['descripcion']
                total = row[0]['total']
                porcentaje = row[0]['porcentaje']

                item2 = 0
                for h in row:
                        pdf.set_fill_color(255,255,255) # COLOR DE BOLDE DE LA CELDA

                        item2 = int(item2) + 1
                        pdf.set_text_color(24,29,31)
                        pdf.set_font('Arial','',10)
                        pdf.cell(15,6,"".decode("UTF-8"),'LR',0,'C',1)
                        pdf.cell(15,6,str(item2).decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(90,6,str(h['descripcion']).decode("UTF-8"),'LTBR',0,'L',1)
                        pdf.cell(40,6,str(h['total']),'LTBR',0,'R',1)
                        pdf.cell(20,6,str(h['porcentaje'])+' %','LTBR',1,'R',1)
                        pdf.set_fill_color(255,255,255)
                
                i =i+1
                j =j+1
                pdf.cell(180,0.25,'','T',1,'R',1)

        pdf.set_font('Arial','B',11)
        pdf.set_fill_color(97,97,97)
        pdf.set_text_color(255,255,255)
        # sql_tot = 'SELECT COUNT(v.id) total FROM votacion_votacion v WHERE v.eleccion_id=%s'
        if tipo == '1':
                sql_tot = 'SELECT COUNT(v.id) total FROM votacion_votacion v WHERE v.eleccion_id=%s'
        elif tipo == '2':
                sql_tot = "SELECT COUNT(v.id) total FROM votacion_votacion v WHERE v.eleccion_id=%s AND v.estado="+str(estado)+""
        elif tipo == '3':
                sql_tot = "SELECT COUNT(v.id) total FROM votacion_votacion v WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+""
        else:
                sql_tot = "SELECT COUNT(v.id) total FROM votacion_votacion v WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+""
        cursor.execute(sql_tot, [detallado])
        row = dictfetchall(cursor)
        total = row[0]['total']

        pdf.cell(120,8,"TOTAL".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(40,8,str(total),'LTBR',0,'R',1)
        pdf.cell(20,8,"100 %",'LTBR',1,'R',1)

        ruta_reporte = settings.MEDIA_PDF
        nombre = str(eleccion)+' Detallado.pdf'
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
