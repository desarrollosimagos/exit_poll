#!/usr/bin/env python2.6
#-*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.db import connection
import psycopg2
import string
import random

class Temporal(CreateView):

    
    def get(self, request, *args, **kwargs):
        print 'paso'
        cod_tel = self.request.GET.get('cod')
        response_data = {}
        print cod_tel
        
        
        if cod_tel == '1':
            chars=string.ascii_uppercase + string.digits
            cod_tel = ''.join(random.choice(chars) for _ in range(8))
            
            
            conn_string = "host='localhost' dbname='exit_poll' user='exitpoll' password='3x1Tpo0ll'"
            conn = psycopg2.connect(conn_string) 
            cur = conn.cursor()
            sql_count = " SELECT count(cod) FROM cod_tel where cod='"+str(cod_tel)+"'"
            cur.execute(sql_count)
            existe = cur.fetchone()[0]
            if existe == 0:
                sql_insert = " INSERT INTO cod_tel(cod) VALUES ('"+str(cod_tel)+"');"
                print sql_insert
                cur.execute(sql_insert)
                conn.commit()
            else:
                chars=string.ascii_uppercase + string.digits
                cod_tel = ''.join(random.choice(chars) for _ in range(8))
                sql_insert = " INSERT INTO cod_tel(cod) VALUES ('"+str(cod_tel)+"');"
                cur.execute(sql_insert)
                conn.commit()
            
            response_data['cod_tel'] = cod_tel

                
        else:
            tipo = cod_tel[:1]
            cod_tel = cod_tel[1:]
            conn_string = "host='localhost' dbname='exit_poll' user='exitpoll' password='3x1Tpo0ll'"
            
                            
                
               
            try:
                conn = psycopg2.connect(conn_string) 
            except:
                response_data['error_conexion'] = 'ok'
                return HttpResponse(json.dumps(response_data), content_type='application/json')
                
            try:
    
                cur = conn.cursor()
                tabla = 't'+tipo+cod_tel
                tabla = tabla.lower()
                
                if tipo == 'e':
                    votos = self.request.GET.get('votos')
                    votos_split = votos.split(',');
                    fin = self.request.GET.get('fin')
                    cur.execute("SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='" + tabla + "')")
                    exists = cur.fetchone()[0]
                    if exists == False:
                        cur.execute("CREATE TABLE IF NOT EXISTS "+str(tabla)+"(cod_tel character varying(8),id_tel INTEGER, candidato_id INTEGER, eleccion_id INTEGER, grupo_etareo INTEGER, sexo INTEGER, circuito INTEGER, estado INTEGER, municipio INTEGER, parroquia INTEGER, poligonal INTEGER, sector INTEGER)")
                        conn.commit()
                       
                    
                    for n in votos_split:
                        resultado = n.split('-')
                        id_tel = resultado[0]
                        candidato = resultado[1]
                        eleccion = resultado[2]
                        grupo_etareo = resultado[3]
                        sexo = resultado[4]
                        circuito = resultado[5]
                        estado = resultado[6]
                        municipio = resultado[7]
                        print(municipio)
    
                        
                        sql_insert = " INSERT INTO "+str(tabla)+"(cod_tel, id_tel, candidato_id, eleccion_id, grupo_etareo, sexo, circuito, estado, municipio)"
                        sql_insert += " VALUES ('"+str(cod_tel)+"',"+str(id_tel)+", "+str(candidato)+","+str(eleccion)+", "+str(grupo_etareo)+","+str(sexo)+", "+str(circuito)+","+str(estado)+", "+str(municipio)+");"
                        cur.execute(sql_insert)
                        conn.commit()
    
                    
                    cur.execute("SELECT id_tel FROM "+str(tabla)+"  ORDER BY id_tel DESC LIMIT 1;")
                    id_te = cur.fetchone()[0]
                    sql_insert_sele = "INSERT INTO votacion_votacion( candidatos_id, eleccion_id, grupo_etareo, sexo, circuito, estado, municipio) "
                    sql_insert_sele += "SELECT candidato_id, eleccion_id, grupo_etareo, sexo, circuito, estado, municipio FROM "+str(tabla)+";"
                    cur.execute(sql_insert_sele)
                    conn.commit()
                    sql_delete = "DELETE FROM "+str(tabla)+" WHERE id_tel <=  "+str(id_te)
                    print sql_delete
                    cur.execute(sql_delete)
                    conn.commit()
                    sql_eliminar = "DROP TABLE "+str(tabla)+""
                    print sql_eliminar
                    cur.execute(sql_eliminar)
                    conn.commit()
                    cur.close()
                    response_data['id'] = id_te
                    response_data['estatus'] = 'ok'
                else:                    
                    ############ Sistema Encuesta
                    
                    votos = self.request.GET.get('respuestas')
                    votos_split = votos.split(',');
                    #fin = self.request.GET.get('fin')
                    
                    cur.execute("SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='" + tabla + "')")
                    exists = cur.fetchone()[0]
                    
                    if exists == False:
                        cur.execute("CREATE TABLE IF NOT EXISTS "+str(tabla)+"(cod_tel character varying(8),id_tel INTEGER, cod_respuesta INTEGER, otras character varying(150), cod_encuesta INTEGER, num_encuestado INTEGER, estado INTEGER, grupo_etareo INTEGER, municipio INTEGER, sexo character varying(15))")
                        conn.commit()
                        

                     
                    num_encu_lis = []
                    for n in votos_split:
                        
                        num_encuesta = 0
                        resultado = n.split('-')
                        id_tel = resultado[0]
                        cod_respuesta = resultado[1]
                        otras = resultado[2]
                        cod_encuesta = resultado[3]
                        num_encuestado = resultado[4]
                        estado = resultado[5]
                        grupo_etareo = resultado[6]
                        municipio = resultado[7]
                        sexo = resultado[8]
                        print (id_tel, cod_respuesta, otras, cod_encuesta, num_encuestado, estado, grupo_etareo, municipio, sexo)
                        num_encu = resultado.count(num_encuestado)
                        num_enc_x = num_encu_lis.count(num_encuestado)
                        
                        if otras == '0':
                            otras = "''"
                        else:
                            otras = otras
                

                        if num_enc_x == 0 and num_encu == 1:
                            
                            num_encu_lis.append(num_encuestado)
                            total_lis= len(num_encu_lis)
                            sql_algo = "SELECT COALESCE(COUNT(id),0) AS total FROM aplicada_encuestaresultado WHERE cod_encuesta = %s"
                            cur.execute(sql_algo,[cod_encuesta])
                            cant_encues = cur.fetchone()[0]
                            if cant_encues > 0:
                                sql_encuestados = " SELECT num_encuestado FROM aplicada_encuestaresultado WHERE cod_encuesta = %s ORDER BY id DESC LIMIT 1"
                                cur.execute(sql_encuestados,[cod_encuesta])
                                ulti_encues = cur.fetchone()[0]
                                tot_insert = ulti_encues+total_lis
                            else:
                                tot_insert = 1
                       

                        sql_insert = " INSERT INTO "+str(tabla)+"(cod_tel, id_tel,cod_respuesta, otras, cod_encuesta, num_encuestado, grupo_etareo,  sexo,  estado,municipio)"
                        sql_insert += " VALUES ('"+str(cod_tel)+"',"+str(id_tel)+", "+str(cod_respuesta)+","+otras+", "+str(cod_encuesta)+","+str(tot_insert)+", "+str(grupo_etareo)+","+str(sexo)+","+str(estado)+", "+str(municipio)+");"
                        #print sql_insert
                        cur.execute(sql_insert)
                        conn.commit()
    
                            
                    cur.execute("SELECT id_tel FROM "+str(tabla)+"  ORDER BY id_tel DESC LIMIT 1;")
                    id_te = cur.fetchone()[0]
                    sql_insert_sele = "INSERT INTO aplicada_encuestaresultado( cod_respuesta, otras, cod_encuesta, num_encuestado, grupo_etareo, sexo,  estado, municipio ) "
                    sql_insert_sele += "SELECT cod_respuesta, otras, cod_encuesta, num_encuestado,  grupo_etareo, sexo, estado,municipio  FROM "+str(tabla)+";"
                   
                    cur.execute(sql_insert_sele)
                    conn.commit()
                    sql_delete = "DELETE FROM "+str(tabla)+" WHERE id_tel <=  "+str(id_te)
                    
                    cur.execute(sql_delete)
                    conn.commit()
                    sql_eliminar = "DROP TABLE "+str(tabla)+""
                    
                    cur.execute(sql_eliminar)
                    conn.commit()
                    cur.close()
                    response_data['id'] = id_te
                    response_data['estatus'] = 'ok'
             
            except:
                response_data['error'] = 'ok'
                
        
        return HttpResponse(json.dumps(response_data), content_type='application/json')
        
                
