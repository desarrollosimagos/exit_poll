#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files


def reporte_eleccion_sexo(sexo,tipo,estado,circuito,municipio):

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
        cursor.execute(sql_ele, [sexo])
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
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(15,8,"N°".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(95,8,"Género".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(50,8,"N° de Votos".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,8,"%".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)

         #Fin Cabezera
        pdf.set_text_color(24,29,31)
        pdf.set_font('Arial','',10) # TAMANO DE LA FUENTE
        sql_sexo = "SELECT COUNT(v.sexo) total, v.sexo sexo, "
        if tipo == '1':
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s), 2) porcentaje"
        elif tipo == '2':
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.estado="+str(estado)+"), 2) porcentaje"
        elif tipo == '3':
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.circuito="+str(circuito)+"), 2) porcentaje"
        else:
            sql_sexo += " ROUND (COUNT (v.sexo) * 100.0 / (SELECT COUNT (v.candidatos_id) FROM votacion_votacion v WHERE v.eleccion_id=%s  AND v.municipio="+str(municipio)+"), 2) porcentaje"
        sql_sexo += " FROM votacion_votacion v"
        sql_sexo += " INNER JOIN elecciones_eleccion e ON v.eleccion_id = e.id"
        sql_sexo += " INNER JOIN candidatos_candidatos c ON v.candidatos_id = c.id"
        if tipo == '1':
            sql_sexo += " WHERE v.eleccion_id=%s "
        elif tipo == '2':
            sql_sexo += " WHERE v.eleccion_id=%s AND v.estado="+str(estado)+""
        elif tipo == '3':
            sql_sexo += " WHERE v.eleccion_id=%s AND v.circuito="+str(circuito)+""
        else:
            sql_sexo += " WHERE v.eleccion_id=%s AND v.municipio="+str(municipio)+""
        sql_sexo += " GROUP BY v.sexo ORDER BY total DESC "

        cursor.execute(sql_sexo, [sexo,sexo])
        row = dictfetchall(cursor)
        total = row[0]['total']
        porcentaje = row[0]['porcentaje']
        
        item3 = 0
        for q in row:
                pdf.set_fill_color(255,255,255) # COLOR DE BOLDE DE LA CELDA
                sexos = q['sexo']
                if sexos == '2':
                    genero = 'Masculino'
                else:
                    genero = 'Femenino'
        
                item3 = int(item3) + 1
                pdf.set_text_color(24,29,31)
                pdf.cell(15,6,str(item3).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(95,6,str(genero).decode("UTF-8"),'LTBR',0,'L',1)
                pdf.cell(50,6,str(q['total']),'LTBR',0,'R',1)
                pdf.cell(20,6,str(q['porcentaje'])+' %','LTBR',1,'R',1)
                pdf.set_fill_color(255,255,255)

        pdf.set_font('Arial','B',12)
        pdf.set_fill_color(97,97,97)
        pdf.set_text_color(255,255,255)
        if tipo == '1':
                sql_tot = 'SELECT COUNT(id) total FROM votacion_votacion WHERE eleccion_id=%s'
        elif tipo == '2':
                sql_tot = "SELECT COUNT(id) total FROM votacion_votacion WHERE eleccion_id=%s AND estado="+str(estado)+""
        elif tipo == '3':
                sql_tot = "SELECT COUNT(id) total FROM votacion_votacion WHERE eleccion_id=%s AND circuito="+str(circuito)+""
        else:
                sql_tot = "SELECT COUNT(id) total FROM votacion_votacion WHERE eleccion_id=%s AND municipio="+str(municipio)+""
        cursor.execute(sql_tot, [sexo])
        row = dictfetchall(cursor)

        total = row[0]['total']

        pdf.cell(110,6,"TOTAL".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(50,6,str(total),'LTBR',0,'R',1)
        pdf.cell(20,6,"100 %",'LTBR',1,'R',1)

        ruta_reporte = settings.MEDIA_PDF
        nombre = str(eleccion)+' Genero.pdf'
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
