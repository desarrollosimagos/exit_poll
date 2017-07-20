#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings


def ver_encuesta(id_enc):

        reload(sys)
        sys.setdefaultencoding("utf-8")

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(12,10,10)  # MARGENE DEL DOCUMENTO

        pdf.set_fill_color(255,255,255)
        pdf.set_font('Arial','',12)
        pdf.set_y(0)
        pdf.set_x(75)
        pdf.write(30,"SISTEMA DINÁMICO DE ENCUESTAS".decode("UTF-8"))

        cursor = connection.cursor()
        sql_det = "SELECT nombre"
        sql_det += " FROM encuestas_encuesta "
        sql_det += " WHERE id = %s "
        cursor.execute(sql_det, [id_enc])
        row = dictfetchall(cursor)
        encuesta = row[0]['nombre']

        pdf.ln(20)
        pdf.set_font('Arial','B',8)
        pdf.set_fill_color(0,0,0)
        pdf.set_text_color(255,255,255)
        pdf.cell(190,6,encuesta.decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.set_text_color(24,29,31)

        cursor = connection.cursor()
        sql_pre = "SELECT id, cod_encuesta, cod_pregunta, pregunta, tipo"
        sql_pre += " FROM preguntas_preguntas"
        sql_pre += " WHERE cod_encuesta = %s ORDER BY id"
        cursor.execute(sql_pre, [id_enc])
        row = dictfetchall(cursor)

        if row == []:
                pdf.set_font('Arial','',8)
                pdf.set_fill_color(191,191,191)
                pdf.set_text_color(255,0,0)
                pdf.multi_cell(190,5,"**Aun no ha creado Preguntas para esta Encuesta".decode("UTF-8"),'LTBR','J',1)

        else:
			
                id_pre = row[0]['id']
                cod_pregunta = row[0]['cod_pregunta']
                pregunta = row[0]['pregunta']

                for m in row:
                        id_pre = m['id']
                        pdf.set_font('Arial','B',8)
                        pdf.set_fill_color(191,191,191)
                        pdf.multi_cell(190,5,str(m['cod_pregunta'])+'. '+str(m['pregunta']).decode("UTF-8"),'LTBR','J',1)
                        pdf.set_fill_color(255,255,255)
                        pdf.set_font('Arial','',8)

                        cursor = connection.cursor()
                        sql_res = "SELECT id, cod_respuesta, respuesta, tipo "
                        sql_res += " FROM respuestas_respuestas"
                        sql_res += " WHERE cod_pregunta_id = %s "
                        cursor.execute(sql_res, [id_pre])
                        row = dictfetchall(cursor)
                        if row == []:
                                pdf.set_font('Arial','',8)
                                pdf.set_text_color(255,0,0)
                                pdf.multi_cell(190,5,"**Aun no ha creado Respuestas para esta Pregunta".decode("UTF-8"),'LTBR','J',1)
                                pdf.set_text_color(24,29,31)
                        else:
                                cod_respuesta = row[0]['cod_respuesta']
                                respuesta = row[0]['respuesta']
                                
                                for j in row:
                                        pdf.cell(5,5,"[  ]",'LTB',0,'C',1)
                                        pdf.cell(185,5,j['respuesta'],'TBR',1,'L',1)
        
        ruta_reporte = settings.MEDIA_PDF
        nombre = str(encuesta)+'.pdf'
        pdf.output(ruta_reporte+'/'+nombre, 'F')
        archivo = open(ruta_reporte+'/'+nombre, "r")

        return nombre, archivo


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
