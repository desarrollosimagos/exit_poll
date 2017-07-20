#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files


def reporte_encuesta(id_enc):

        reload(sys)
        sys.setdefaultencoding("utf-8")

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(12,10,10)  # MARGENE DEL DOCUMENTO
        
        pdf.set_font('Arial','B',12)
        pdf.ln(5)
        pdf.set_fill_color(0,0,0)
        pdf.set_text_color(255,255,255)
        pdf.cell(190,8,"SISTEMA DINÁMICO DE ENCUESTAS".decode("UTF-8"),'LTBR',1,'C',1)
        
        cursor = connection.cursor()
        sql_det = "SELECT en.nombre, TO_CHAR(en.fecha_update,'dd-mm-yyyy')fecha_update, en.user_create_id, en.estatus estatus, "
        sql_det += " (SELECT username FROM auth_user WHERE id = en.user_create_id) n_user, "
        sql_det += " (SELECT num_encuestado FROM aplicada_encuestaresultado WHERE cod_encuesta = en.id ORDER BY id DESC LIMIT 1) num_enc"
        sql_det += " FROM encuestas_encuesta as en "
        sql_det += " WHERE en.id = %s "

        cursor.execute(sql_det, [id_enc])
        row = dictfetchall(cursor)
        encuesta = row[0]['nombre']
        fecha = row[0]['fecha_update']
        usuario = row[0]['n_user']
        estatus = row[0]['estatus']
        num_encuestados = row[0]['num_enc']
        
        if estatus == '1':
            est = 'Borrador'
        elif estatus == '2':
            est = 'Activa'
        else:
            est = 'Cerrada'

        pdf.ln(5)
        pdf.set_font('Arial','',10)
        pdf.set_fill_color(255,255,255)
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial','B',10)
        pdf.cell(42,6,"Nombre de la Encuesta: ".decode("UTF-8"),'',0,'L',1)
        pdf.set_font('Arial','',10)
        pdf.cell(148,6,str(encuesta).decode("UTF-8"),'',1,'L',1)
        pdf.set_font('Arial','B',10)
        pdf.cell(26,6,"Elaborada por: ".decode("UTF-8"),'',0,'L',1)
        pdf.set_font('Arial','',10)
        pdf.cell(135,6,str(usuario).decode("UTF-8"),'',0,'L',1)
        pdf.set_font('Arial','B',10)
        pdf.cell(15,6,"Estatus: ".decode("UTF-8"),'',0,'R',1)
        pdf.set_font('Arial','',10)
        pdf.cell(14,6,str(est).decode("UTF-8"),'',1,'R',1)
        pdf.set_font('Arial','B',10)
        pdf.cell(13,6,"Fecha: ".decode("UTF-8"),'',0,'L',1)
        pdf.set_font('Arial','',10)
        pdf.cell(123,6,str(fecha).decode("UTF-8"),'',0,'L',1)
        pdf.set_font('Arial','B',10)
        pdf.cell(40,6,"N° de participantes: ".decode("UTF-8"),'',0,'R',1)
        pdf.set_font('Arial','',10)
        pdf.cell(14,6,str(num_encuestados).decode("UTF-8"),'',1,'R',1)
        
        pdf.ln(5)
        pdf.set_font('Arial','B',8)
        pdf.set_fill_color(0,0,0)
        pdf.set_text_color(255,255,255)
        pdf.cell(190,6,"Resultados".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.set_text_color(24,29,31)

        cursor = connection.cursor()
        sql_pre = "SELECT id, cod_encuesta, cod_pregunta, pregunta, tipo"
        sql_pre += " FROM preguntas_preguntas"
        sql_pre += " WHERE cod_encuesta = %s ORDER BY id"
        cursor.execute(sql_pre, [id_enc])
        row = dictfetchall(cursor)
        id_pre = row[0]['id']
        cod_pregunta = row[0]['cod_pregunta']
        pregunta = row[0]['pregunta']
        tipo = row[0]['tipo']
        
        
        k = 0
        for m in row:
            if m['tipo'] == '1':
                tipo_p = "Selección Simple"
            else:
                tipo_p = "Selección Multiple"
                    
            id_pre = m['id']
            pdf.set_font('Arial','B',8)
            pdf.set_fill_color(191,191,191)
            pdf.multi_cell(190,5,str(m['cod_pregunta'])+'. '+str(m['pregunta']).decode("UTF-8"),'LTBR','J',1)
            pdf.set_fill_color(228,228,228)
            pdf.cell(20,5,"Respuesta:".decode("UTF-8"),'LTB',0,'R',1)
            pdf.set_font('Arial','',8)
            pdf.cell(140,5,"("+str(tipo_p)+")".decode("UTF-8"),'TBR',0,'L',1)
            pdf.set_font('Arial','B',8)
            pdf.cell(15,5,"Total".decode("UTF-8"),'LTBR',0,'C',1)
            pdf.cell(15,5,"%".decode("UTF-8"),'LTBR',1,'C',1)
            pdf.set_fill_color(255,255,255)
            pdf.set_font('Arial','',8)

            cursor = connection.cursor()
            sql_res = "SELECT rr.id, rr.respuesta respuesta, "
            sql_res += " COALESCE((SELECT COUNT(ar.cod_respuesta)"
            sql_res += " FROM aplicada_encuestaresultado as ar "
            sql_res += " WHERE ar.cod_respuesta = rr.id GROUP BY ar.cod_respuesta),0) cantidad, "
            sql_res += " COALESCE(ROUND ( (SELECT COUNT(ar.cod_respuesta) "
            sql_res += " FROM aplicada_encuestaresultado as ar "
            sql_res += " WHERE ar.cod_respuesta = rr.id GROUP BY ar.cod_respuesta) * 100.0 /  "
            sql_res += " (SELECT COUNT(rr_s.id) "
            sql_res += " FROM respuestas_respuestas AS rr_s "
            sql_res += " INNER JOIN aplicada_encuestaresultado AS ar_s ON rr_s.id=ar_s.cod_respuesta "
            sql_res += " WHERE rr_s.cod_pregunta_id = rr.cod_pregunta_id), 2),0.00) porcentaje "
            sql_res += " FROM respuestas_respuestas as rr"
            sql_res += " WHERE rr.cod_pregunta_id = %s GROUP BY rr.id, rr.cod_respuesta, rr.respuesta  "
            sql_res += " ORDER BY rr.id, rr.respuesta"
            cursor.execute(sql_res, [id_pre])
            row = dictfetchall(cursor)

            if row == []:
                pdf.cell(190,5,"N/A",'LTBR',1,'L',1)

            else:
                # cod_respuesta = row[0]['cod_respuesta']
                respuesta = row[0]['respuesta']
                cantidad = row[0]['cantidad']
                porcentaje = row[0]['porcentaje']

                item = 0
                for j in row:
                    if k == 25:
                        pdf.add_page()
                        pdf.ln(10)
                        pdf.set_font('Arial','',8)
                        pdf.set_fill_color(255,255,255)
                        pdf.set_text_color(24,29,31)
                    
                    item = int(item) + 1
                    pdf.cell(5,5,"",'LTB',0,'C',1)
                    pdf.cell(5,5,str(item)+".",'TB',0,'C',1)
                    pdf.cell(150,5,j['respuesta'],'TBR',0,'L',1)
                    pdf.cell(15,5,str(j['cantidad']),'TBR',0,'R',1)
                    pdf.cell(15,5,str(j['porcentaje']),'TBR',1,'R',1)
                    k = k +1
        
        ruta_reporte = settings.MEDIA_PDF
        nombre = str(encuesta)+'.pdf'
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
