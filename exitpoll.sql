--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.6
-- Dumped by pg_dump version 9.4.1
-- Started on 2015-06-05 15:25:17 VET

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

--
-- TOC entry 2458 (class 0 OID 26240)
-- Dependencies: 224
-- Data for Name: aplicada_encuestaresultado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY aplicada_encuestaresultado (id, cod_respuesta, otras, cod_encuesta, num_encuestado) FROM stdin;
66	1	\N	1	2
67	5	\N	1	2
68	9	\N	1	2
69	17	\N	1	2
70	19	\N	1	2
71	23	\N	1	2
72	3	\N	1	3
73	6	\N	1	3
74	9	\N	1	3
75	19	\N	1	3
76	23	\N	1	3
77	1	\N	1	4
78	5	\N	1	4
79	8	\N	1	4
80	18	\N	1	4
81	27	\N	1	4
82	2	\N	1	5
83	6	\N	1	5
84	7	\N	1	5
85	17	\N	1	5
86	18	\N	1	5
87	21	\N	1	5
88	1	\N	1	6
89	5	\N	1	6
90	7	\N	1	6
91	15	\N	1	6
92	21	\N	1	6
93	1	\N	1	7
94	5	\N	1	7
95	9	\N	1	7
96	16	\N	1	7
97	17	\N	1	7
98	19	\N	1	7
99	23	\N	1	7
100	2	\N	1	8
101	5	\N	1	8
102	9	\N	1	8
103	19	\N	1	8
104	21	\N	1	8
105	4	\N	1	9
106	13	\N	1	9
107	20	otro	1	9
108	27	\N	1	9
109	4	\N	1	10
110	4	\N	1	10
111	4	\N	1	10
112	1	\N	1	10
113	13	\N	1	10
114	13	\N	1	10
115	13	\N	1	10
116	5	\N	1	10
117	8	\N	1	10
53	1	\N	1	1
54	5	\N	1	1
55	9	\N	1	1
56	17	\N	1	1
57	19	\N	1	1
58	20	Omar Vizquel	1	1
59	23	\N	1	1
118	20	otro	1	10
119	20	otro	1	10
120	20	otro	1	10
121	27	\N	1	10
122	27	\N	1	10
123	27	\N	1	10
124	27	\N	1	10
125	4	\N	1	11
126	13	\N	1	11
127	20	otro	1	11
128	27	\N	1	11
129	1	\N	1	12
130	1	\N	1	12
131	1	\N	1	12
132	1	\N	1	12
133	5	\N	1	12
134	5	\N	1	12
135	5	\N	1	12
136	5	\N	1	12
137	8	\N	1	12
138	9	\N	1	12
139	9	\N	1	12
140	9	\N	1	12
141	1	\N	1	13
142	27	\N	1	12
143	16	\N	1	12
144	16	\N	1	12
145	16	\N	1	12
146	5	\N	1	13
147	9	\N	1	13
148	17	\N	1	12
149	17	\N	1	12
150	17	\N	1	12
151	16	\N	1	13
152	18	\N	1	12
153	18	\N	1	12
154	18	\N	1	12
155	17	\N	1	13
156	23	\N	1	12
157	23	\N	1	12
158	23	\N	1	12
159	18	\N	1	13
160	23	\N	1	13
161	1	\N	1	14
162	5	\N	1	14
163	8	\N	1	14
164	27	\N	1	14
\.


--
-- TOC entry 2469 (class 0 OID 0)
-- Dependencies: 223
-- Name: aplicada_encuestaresultado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('aplicada_encuestaresultado_id_seq', 164, true);


--
-- TOC entry 2404 (class 0 OID 16737)
-- Dependencies: 170
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group (id, name) FROM stdin;
1	Administrador
2	Registro
3	Consulta
4	Topologia
5	Configuraciones
6	Aplicar
\.


--
-- TOC entry 2470 (class 0 OID 0)
-- Dependencies: 171
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_id_seq', 6, true);


--
-- TOC entry 2428 (class 0 OID 16807)
-- Dependencies: 194
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	cors model	corsheaders	corsmodel
8	perfiles usuario	login	perfilesusuario
9	estado	estados	estado
10	municipio	municipios	municipio
11	parroquia	parroquias	parroquia
12	circuito	circuitos	circuito
13	grupo_ etareo	grupo_etareo	grupo_etareo
14	categoria	categoria_eleccion	categoria
15	tipo_eleccion	tipo_eleccion	tipo_eleccion
16	centros	centro_votacion	centros
17	partidos	partidos	partidos
18	eleccion	elecciones	eleccion
19	exit poll	exitpoll	exitpoll
20	candidatos	candidatos	candidatos
21	votacion	votacion	votacion
22	sector	sectores	sector
23	poligonal	poligonales	poligonal
24	encuesta	encuestas	encuesta
25	preguntas	preguntas	preguntas
26	respuestas	respuestas	respuestas
27	encuesta resultado	aplicada	encuestaresultado
\.


--
-- TOC entry 2408 (class 0 OID 16747)
-- Dependencies: 174
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
64	Can add log entry	1	add_logentry
65	Can change log entry	1	change_logentry
66	Can delete log entry	1	delete_logentry
67	Can add permission	2	add_permission
68	Can change permission	2	change_permission
69	Can delete permission	2	delete_permission
70	Can add group	3	add_group
71	Can change group	3	change_group
72	Can delete group	3	delete_group
73	Can add user	4	add_user
74	Can change user	4	change_user
75	Can delete user	4	delete_user
76	Can add content type	5	add_contenttype
77	Can change content type	5	change_contenttype
78	Can delete content type	5	delete_contenttype
79	Can add session	6	add_session
80	Can change session	6	change_session
81	Can delete session	6	delete_session
82	Can add cors model	7	add_corsmodel
83	Can change cors model	7	change_corsmodel
84	Can delete cors model	7	delete_corsmodel
85	Can add perfiles usuario	8	add_perfilesusuario
86	Can change perfiles usuario	8	change_perfilesusuario
87	Can delete perfiles usuario	8	delete_perfilesusuario
88	Can add estado	9	add_estado
89	Can change estado	9	change_estado
90	Can delete estado	9	delete_estado
91	Can add municipio	10	add_municipio
92	Can change municipio	10	change_municipio
93	Can delete municipio	10	delete_municipio
94	Can add parroquia	11	add_parroquia
95	Can change parroquia	11	change_parroquia
96	Can delete parroquia	11	delete_parroquia
97	Can add circuito	12	add_circuito
98	Can change circuito	12	change_circuito
99	Can delete circuito	12	delete_circuito
100	Can add grupo_ etareo	13	add_grupo_etareo
101	Can change grupo_ etareo	13	change_grupo_etareo
102	Can delete grupo_ etareo	13	delete_grupo_etareo
103	Can add categoria	14	add_categoria
104	Can change categoria	14	change_categoria
105	Can delete categoria	14	delete_categoria
106	Can add tipo_eleccion	15	add_tipo_eleccion
107	Can change tipo_eleccion	15	change_tipo_eleccion
108	Can delete tipo_eleccion	15	delete_tipo_eleccion
109	Can add centros	16	add_centros
110	Can change centros	16	change_centros
111	Can delete centros	16	delete_centros
112	Can add partidos	17	add_partidos
113	Can change partidos	17	change_partidos
114	Can delete partidos	17	delete_partidos
115	Can add eleccion	18	add_eleccion
116	Can change eleccion	18	change_eleccion
117	Can delete eleccion	18	delete_eleccion
118	Can add exit poll	19	add_exitpoll
119	Can change exit poll	19	change_exitpoll
120	Can delete exit poll	19	delete_exitpoll
121	Can add candidatos	20	add_candidatos
122	Can change candidatos	20	change_candidatos
123	Can delete candidatos	20	delete_candidatos
124	Can add votacion	21	add_votacion
125	Can change votacion	21	change_votacion
126	Can delete votacion	21	delete_votacion
127	Can add sector	22	add_sector
128	Can change sector	22	change_sector
129	Can delete sector	22	delete_sector
130	Can add poligonal	23	add_poligonal
131	Can change poligonal	23	change_poligonal
132	Can delete poligonal	23	delete_poligonal
133	Can add encuesta	24	add_encuesta
134	Can change encuesta	24	change_encuesta
135	Can delete encuesta	24	delete_encuesta
136	Can add preguntas	25	add_preguntas
137	Can change preguntas	25	change_preguntas
138	Can delete preguntas	25	delete_preguntas
139	Can add respuestas	26	add_respuestas
140	Can change respuestas	26	change_respuestas
141	Can delete respuestas	26	delete_respuestas
142	Can add encuesta resultado	27	add_encuestaresultado
143	Can change encuesta resultado	27	change_encuestaresultado
144	Can delete encuesta resultado	27	delete_encuestaresultado
\.


--
-- TOC entry 2406 (class 0 OID 16742)
-- Dependencies: 172
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	6	144
2	6	142
3	6	143
\.


--
-- TOC entry 2471 (class 0 OID 0)
-- Dependencies: 173
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 3, true);


--
-- TOC entry 2472 (class 0 OID 0)
-- Dependencies: 175
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_permission_id_seq', 144, true);


--
-- TOC entry 2410 (class 0 OID 16752)
-- Dependencies: 176
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
3	pbkdf2_sha256$15000$ZNSU5jEXapRz$wV60nkuEIm38K7ZfAMbffKYqSFqnPlAZQW6QAx5f7lg=	2015-03-23 14:24:00.029531-04:30	f	marcel				f	t	2015-03-23 14:17:50-04:30
2	pbkdf2_sha256$15000$jjfrbG16xAWd$A9cfF1Rb0WqRIwYwGhl+MYPR/bAU9MJekvMU5NkOomk=	2015-03-24 12:16:22.168381-04:30	f	japonte				t	t	2015-03-20 10:01:33-04:30
4	pbkdf2_sha256$15000$oeyq7taGMKT7$RCmY2vgE7OLRzRtV7d7R/ttmeUdVURNh32LQ9bd0v2w=	2015-06-04 11:00:40.725577-04:30	f	encuestador				f	t	2015-06-04 10:41:20-04:30
1	pbkdf2_sha256$15000$ijPJAhuJbEwl$enL0m1/FQjl3E84+bfa1ZaYVRwgfRdL/JpCgJxsbQO0=	2015-06-04 14:56:07.324865-04:30	t	admin				t	t	2015-03-20 09:57:37-04:30
\.


--
-- TOC entry 2411 (class 0 OID 16755)
-- Dependencies: 177
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
5	3	4
6	2	5
7	1	2
8	1	3
9	1	4
10	1	5
11	1	6
12	4	6
\.


--
-- TOC entry 2473 (class 0 OID 0)
-- Dependencies: 178
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 12, true);


--
-- TOC entry 2474 (class 0 OID 0)
-- Dependencies: 179
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_id_seq', 4, true);


--
-- TOC entry 2414 (class 0 OID 16762)
-- Dependencies: 180
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- TOC entry 2475 (class 0 OID 0)
-- Dependencies: 181
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 126, true);


--
-- TOC entry 2447 (class 0 OID 16862)
-- Dependencies: 213
-- Data for Name: partidos_partidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY partidos_partidos (id, n_partidos, siglas, foto_partido, nom_presidente, ape_presidente, correo, twitter, telefono, fecha_create, fecha_update, user_create_id, user_update_id) FROM stdin;
14	Comité de Organización Política Electoral Independ	COPEI	logo_partidos/COPEI.jpeg	Antonio Domingo	Ecarri Acosta	copei@gmail.com		02124568648	2015-04-16 15:07:42.669075-04:30	2015-04-23 14:53:17.161813-04:30	1	\N
10	Partido Socialista Unido de Venezuela	PSUV	logo_partidos/PSUV.jpeg	Nicolás	Maduro Moros	contacto@psuv.org.ve	@PartidoPSUV	02345648684	2015-04-16 14:07:46.63374-04:30	2015-05-13 09:20:17.550121-04:30	1	\N
11	Patria Para Todos	PPT	logo_partidos/PPT_YyKr71V.jpeg	Rafael	Uzcátegui	ppt@ppt.org.ve	@patriaparatodo1	02125777420	2015-04-16 14:41:19.76071-04:30	2015-05-13 09:20:42.951964-04:30	1	\N
13	Primero Justicia	PJ	logo_partidos/PJ.jpeg	Julio	Borges	primerojusticia@gmail.com	@Pr1meroJusticia	02122858391	2015-04-16 14:59:05.488302-04:30	2015-05-13 09:20:58.358011-04:30	1	\N
12	Un Nuevo Tiempo	UNT	logo_partidos/UNT_8bthzar.jpeg	Enrrique	Marquez	unt@gov.ve	@PartidoUNT	02122336644	2015-04-16 14:50:43.47289-04:30	2015-05-13 09:21:26.151106-04:30	1	\N
\.


--
-- TOC entry 2416 (class 0 OID 16767)
-- Dependencies: 182
-- Data for Name: candidatos_candidatos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY candidatos_candidatos (id, nombre, apellido, cedula, foto, sexo, edad, twitter, fecha_create, fecha_update, part_politico_id, user_create_id, user_update_id, candidato_activo, foto_binario) FROM stdin;
18	Kleydis	Moreno	18864864	foto_candidato/18864864.jpeg	1	35		2015-04-17 10:23:12.984868-04:30	2015-04-17 10:23:12.984927-04:30	14	1	\N	t	\N
19	Alejandra	Moreno	17548818	foto_candidato/17548818.jpeg	1	40		2015-04-21 09:07:41.511313-04:30	2015-04-21 09:14:59.944774-04:30	11	1	1	t	\N
25	Jose	Peña	12784848	foto_candidato/12784848.jpeg	2	25		2015-04-23 14:47:52.757439-04:30	2015-04-23 14:47:52.757496-04:30	10	1	\N	f	/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxQTEhQUEhQWEhQWFBcVFRgUFRUXFBYUFBQWFxQS\nFBQYHCggGBolHBQUITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0OGhAQGywgICQsLCwsLCwsLCws\nLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsLCwsNywsLCwsLDcrN//AABEIAQQAwgMBIgACEQED\nEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAAAQIEBQYDBwj/xAA+EAABAwIEAwYEAggGAwEAAAABAAIR\nAyEEBRIxQVFhBhMicYGRMqGxwQfwFBUjQlKS0fEkM2JyguFDc7IW/8QAGgEAAgMBAQAAAAAAAAAA\nAAAAAAIBBAUDBv/EACURAAICAgMAAgICAwAAAAAAAAABAhEDBBIhMRNBBSIyUSNCUv/aAAwDAQAC\nEQMRAD8A0xCaQnFEL0tmCNhCEKQBIUqEANFkpCRySUAIhCRxQFCpCE3UjvEE0BSJC9DiiiByCEjS\nntKmwG6ErQiU4BTYAkLUqJRYHOOX0QlSKQAhN0JyQlACaEJyEATCEieU0rigGaUkJ6JU2AxCdCaU\nwCEJpKeo2MrtY0ucdIG5Ki0vRkrHlyg4vM2MB1OaON3Becdqe2L6rnNpHRTBiRZx6rJ1sS5xk3+q\np5NxJ1FF3Hp2rZ6DmPb9oJFJurzsD5Kqf+IVbgxvqSVjSCAmEKo9nI/strWxr6NjR/EDEB3iDXDl\nER6q9wf4g03QHsLOf7wXmTUpUw2pp+kS1oP6Pc8tzqlVALKjTPCYI8wVatqSvn2hXLCCOa9B7H9s\nJIpViBwa523kSrePaUnTKeXUce0ehgpAU2m9OCuFJqmKhKAnQgDmQk0pyFNgc0J8JpCYBEJYQgCc\nmkJyFwJo5oT0EKSDmQmlPTHJrJohZnmDKLC97oA/MDqvKO1fad2JJawFjBwvfh4lM/ELO+9rd0wy\nymbxxdx81TZPlDqlzt8ysza2f9V4aunrJ9v0iYLLHVL8FY/qbk0n88lssvy4AABqucLljT+6saed\n30bUNbrs8z/UhN+HsmuyYgGQvVquQMcNoPDf5qDU7MC95tZQswPWPKqmXGFyp4Ug7fJeoMyDmFyf\n2ZA8l0WehXrnnP6vJkwoT6Tmm9l6XVycN6qnzHJgQeBTLP2c569I79iu1+kijXMtNmvM2PBpPJek\nUzZeC47BOpOg+69L/D/Pe+pd24/tGDid2jYrY1NjkuMjG2tZR/ZGzBTkxqer5nHNCcQgBSA1BTnB\nNQAIQhAEtCdCaVzHEAQUjGRxnz6pSgijmSqXtTmQoUHvNjEN8yFdlYH8UqxFKm3gXEn0Fks3UWzr\nijymkYHLsOalQE3JMnqZut7gqEQAIhZDswzxSt1g2LzWxJ2z02pBFlhGbK1wwUbC0tlYYSkCTJtG\n0cecqmaKRJpRxXYMCboZYETBldmxCKGI2IoiJG6gVtla1YUOu0ICkZ/FsVRiGdFosZT3VNiKe6lH\nOSszecYIPaR9lQ9mcd+jYpjjZs6Xf7Sd1qsTsViM3bFQxaf6rR1p8WmZe1jTR7tRqAgEcV1BVF2P\nxJq4Wm52+mP5bK8avRRdqzzUlTY5NJSohOIMQnOTUAHshCEATJSFJqRqXMcVIUhRwQA2F5z+KTf8\nr1+a9GqFeZ/ikfHSvwdb2uuWd/42d9dXkRn+zJh3rzW4wDrrz/IZ1281s8LiI815zOrZ6XWdGqpV\nuqsKDyqXBOBiStHgnsO0FVuDL3NDmtK7UmFTadMQu36PZTwYc0VdYFV9dpHArROw4CiYqkIRwZPN\nGTxDzdV1d26vMfTbeCOqzOYPgxMqODFc4tFfjDusRnB8cjmthiasgrD5gfH6q5gM7Oeu9gnzhKYj\nbV9VpQFRdiaYGEpR/CD7yr9pXpIdRSPM5Xc2IErxCR26IXRHJiEJpCeUwlSAiEIQB3lCCUwlIOdA\nUSuYKdqQAOXnP4qN/wAiObpt5cV6M5Yb8TcHqoNeN2PE+TjC5ZleNnbX6yIx/Z2iPE70U+pjn3FN\nsmYn7Jchwx7nzJVhRpim2XDqvPTas9FBOitZg8Sb39DdNbjsQxwaNdMcp381Y1c/IEtYS0EAkbAn\nYE7Lm3Fd+7SadQPhxGkTZu5soXL7RNR+mafs9ndTT4nEHibk+xW/wuZamgrxrDVHtuCSPzvyK9E7\nP1RUpzNwea5TlTLONdFvnGZ6WnTBMWWBzXtJWDXCZJHDgVZdq8dp8IO4+6xjgXGXmB1UxlYT/pFe\ncTi3mxc7pKZVdiGDxgzNpV7TzSgwWkxuYMbxvEbrm/M2P2uD5J7f9HDgv+uyBQxYf0PELOZ5Tiqe\nsFauphIdrHP5Ki7SUPE08wQuuN2zjl6iep9jh/hKJ2/ZhXar8hpaMPSbypt9LSVYr0MfEebl22Dt\n0kJUeqdCM5yhKSkTEBPVCJP5lCAOh9fkhN1I1KEhxyE3UllQ/QIGd5j3NPUPi4W2WUzSq7EYV5NQ\nuaRMQLFquO1LZ0NJ3KzuNxbW0zSaI258TJWFuZ5/I4p0jf1MEFiUmrZIyvDwxgjgPorHMctD2xeI\nTcq4BaXBYdrgs2T7NTHFUZChllM0XUKtMaTs5sBwI2N0/sxltPCPdUaTVqEFrdQhrWuNyI3Pqtoc\nC3iAmVMAOAA8gm+V1RPwQbsymJoiXEADXu1rTvzV12dkSBxTK+GAdfdd8qMPsuMnZYhFIo8/BNQ6\nrxZNyyi0VG1XMY9osA4GANjI5qb2jZFToRdcMBQ9uKmDoSUU+mZzMuzbTVdprllBx1FpDpEmdIAM\nHcpmZ5ex9VvcNLQABMRMcSOK31PLGOGyBk7W3hd3llRXWGMX0ZalgTovuqLtFhNQZa4qD52hb3GU\nA0LKZ2208iDvyKMc3ysTNBVRf088dT0h9NoYIG51DhK0jHSARsRKxGZ0xWvfwjUBzPFavJXTQZO8\nfQrX0c853GRjfkdeEEpxRMBQ4pyY9aiMhiISkpExAISShAASmykQgc6SiVyBTw5L9gVmaUddSnOw\nBPyKzeLw37KvU5aY97laTNHw4HhpInqVSVGuayo3T3jXNM6eBi0rA21WZ2em1GngQ/JakkeS2OAq\nAD+ywOQvs30+gH2WywL5jyVKa7LeJl40TEJ1SjYpMKVLJ3XIsWY7OfC4Dmm5ZOq26TNaoe9zjwsJ\nUjs93clznfdLxY6dEbtDRsP7rjkRnqrbtPWpaBBuqjs7UAdB2N+KbjQrlZpaVK3EIeYXag8HZRsa\nVKRHRTZjV57LI5qNcM4ve1n8zgFpMxesxUrtGIol2wqh0c9N11xrsqZWvC7oYEtpvbfVTJHpsR9V\noctEUmAcvrdUYxpPeVIhrp09TeyvsIyGNHJo+i0vxi5TkzP/ACzqEYo76khehNctpHn2ElJKcSml\nSQLrPRCahADCU0vMpXJiBzpKUFcyUocgCPjqWppCqjTPwxEjmrl4UapRBF1S2tVZu16XdTceF0/D\nK5WNNuTiPYrX5c+YhZ3EYcMqFoJIN5O991bZbUgrCzxcHTN3XyKStGswj13xTvCQCAYtPNVLa+lu\nomFVYrNzck2Cr9sucqIue5U14+KD52KpcLh3AFtN+l3Cdj6qRXr1q5gN8HEkwuzctraQWw4NBOkO\nDndICZdeiSlfhWY2k4w2q/W7kDDW+o3V7kGGFETJcfOYCqszyesGghove5E3vcLhgMzqUoZUA+qa\nXfhEXXp6Hh60iRsomOqKty/NZhp2ItyXfG1oE8Vzs6WUmYVlU5bJxIIAOljnX9IKl4ozJXTJMG4l\n72kAfBMeRKt4cLn1H0o5skYPlIm06OtwHCZdyHHZaCmouHohospjAt3VwfDCvtmDtbPzSv6+hTKS\nUEpFaKbFlIhKggSUJUiAOGpCYllA44lJKZqlKgB651KaeCiUAUedUiNL9rlp9Rb6JcLVU3NG6qbx\n/pJ9RdZ/CVzx+qxPyUEp2jb/ABs7jTNXUqg0wFQZuKmkaWgtnaYTxjACAePVWFYgtGm6yraNjpmb\np4bEVP3mgcGz9wujMuxLDqbpB6PIKmVcUGGdJnhCr8Rn1QfCwnzQv2H5Qh6MxeBxNy4tnmXkqCzv\np0lmuOIN4VnSzSs8XpH5KbhieIiVPLiJJKXaH4Oi6Gkt0kRA+al5hiJ9lyxztLQQYKrjWJElCVux\nZdKhuIfa6v8AJ6GmkwRvLjvufyFnMI3vKzWcJk+QutowfKy3Px+PrmYH5DJ3wHUqa66UjSnalpma\nNQhIXIFaFRKEQggJH5KEshIgCDKJTdSNSnwc66kalzBSqAHgpSYuuZdCz/aTMiGkNsIM+a55JqCs\nfHBzdFhmOa0mggvEwRAubrNPdpg8PvzWVo4kudc7kfVa8MlixNvK8kkbepiWOLONfFXCussragL3\nWOzHUyDuJXfK8xINjwVWULRbhk4s9Gp0GR4oVRmGG7w2GmDx4/7VW4bMzbUZ6Lo/NRqG3hvc7+S5\nKDRYeRS9L3DYdmmBcwN1GxVIi4jyUDF5lpE+973VPjM9Py3UfGyHljFEjMMwMETsodPF+HzVRisW\nXOgbmOKt8HhDDS7kuyikivKTkyy7OWrAm3hO/VbNpsvMM1xRp6SDfzutZ2azc1GNDuNgTz5LW0cy\n4qJk7uF8nI04KNS5NT1pmaOJTUIQK2CEIQQCEIQBBQkJTS5NY49Oamagh9QASTH2SyaXZKTugxFT\nS2fbzWW7RUf2TvJWzseKjtLZgG55nouWd4fUwgcj9FRzz5F7XhxR5nhRL2Dm4fb+i31EWWR7P4SX\n6jeDHqtvQp2WJsSTZs68f1IGLwocCCJlZnFZa+k6Wy5v08lt3NXB+GulhJUNPGmzHYfMErsbPGVo\nMbkLH3036Kqrdmo2PsunJHJxl9Ed+YcCVFNR9V2lgk/L3VxhOzU/FJWkwOUMpgAAD0Q2kHCT9KXJ\nsjDDrd4n9f3VbuZAKnNZCj1huuEpNssRx8UY/tQ3wg8AVM7JvPdzJ3skz2jLHSpHZmlpoNPO/ur+\np0ijtem+wdSWA8wP+11JWVw2eOpHQ4am7iN7rSYXFNqNDmmQVtwyKSMTJjcX2d9SUFMSgrocx6EI\nQLRzQn6UICiuTXVAo9bE8lx0km6rT2EvC3HXY9+L4BV2Y1z3Ym5dqvyawSfsrIUAFBzClLKVrO71\nn/J1Mkf/ACuEpOXpZjCK8Eyelx/1Eeyt34bUOgEe/BUmU4kX66Xj/m1sk/8AIFaNlSQbHhslSVUO\nYTB4TusRVpn+LWPIrT4dkhRu0GDgsrgHwQ1/DwO4+hUzBumCON1kbMKkaetNcUh1WhC5hitjTlqj\nupQuCZaIxpT0XRtIO3+qlU6YKcKcIXorODaTRsFzeealOPJMZSk7JmyURG0S6/BccVSgK70w3ZVW\nNKUlsy+bUS+GDdxA9OJVszD6GARYDT7JMuwpe41SI4MtaP3ip+KiBwWrrY6hb+zJzzuRnc0omGRx\n1M+Wpp92/NSMorEB2gkFobUby0u3HlMp2a1wGsFydYd5Cn4nT02C5ZNQID5tposafMkuj2KtLor0\nmX+Gzm8VGx/qHH0VrSrBwltws13Fl0Y5zCC07bhdo56/kV566f8AE0rXJSVWYTNGus7wlWQcDcbd\nFYjNSVoqyg4umO1ITUJxSgDCVJpCwn6JjWCeSkNE/mPlxWYlRqiNaOk/L2C5YylqwryI1UHioI46\nTqI9QSFJ7qLi/mkwTx3r2P2c3VA2tY/JMBlQQ18t+AkO6GjX8TT6OkLSZbiBcE/kKhqUAwaXXbTe\n7Cuvfu6pmi/0Jb81Ny9zi0T8TSWPFviaYn1iUqVAaR9IVGlpAMg7i0Hos3hm9040jHhPg6jkr/BV\nDaY258UzMMsFQAjwuFwR+brjsYfkj16dcOTg+xuHqckVj6KNgnOa6Kgg8wfn0VlVwusSPkZWVKEo\numjUjJNWVwqRsl/SnJ78ERzTHUnSooYb3hKm4VnHdMw+Cc48VbNwZaOH3UBdECu+xVTXYahDG7n4\nug4hWmJ3hvidw5DzTsPRFMEbk/EbXPRWtbA5O2V9jMo+EeowNAAERb0VTiDJ6SrLE1JJF+hUR9IM\nY6o7ZrXOPoFqLpUZj9soMU3vKhH8dRlAeXxVY9AArfLD/h69SPjqvjfYHQIjhCraQ0imXb06FTEv\n/wDZWkNHsrYYY0cHQYbOIZ6ydR+SkB5FtoQ5oLZkLr+eCQUjw59EAQalDknYXHOZvcKY9pi5tw5+\nqi1aM/2Ryce0Q0n6Tf1y3kUKp7gJU/zyOfwxLVjdt5UinPX7+hSMN7fOV2B58eUpDqAbbj6qrx9Q\n03teLkG83txCuHUwf+1CxGGDrED0QBAzljXP1AgU69Punng1/wD4nHle09VFyutpcx7hHeTRrT+7\nXp2Y48g5vFTH5XLXND4BsREjz87BcWZM4l2qqCKgaHjRuWfC+J+JAFs+s2mCXWj39AqjNe0NcsIo\nU9Lf4nAyeoCuKeCY0AmS7+J5k+y6uDCCHeLzn3UMDM9nqz32eQHO3dUJ35W2V3g3uovcw2Ju4Ay2\neDgeSiYrBNpEH4mTzMjrzUd+DIcH03EHTAY4yCOYK5ThyVMeE2nZrsOdRuFM/RWm8LJ5dmxaYeNJ\n5GT7LQ4fOqbmSDpMTe6zsmFxdI0Y51JWT7MEmAqrF5j3hLWWHEkEeyq81zwX1OnkG7n2VQc6qvtT\naGTa9zyuu2HWr9mcMuymuKOX/wCr0Vu7FIlsxLRLp4yrnDZg2qQGmTvGx9QVX5fl2kyG34m153U+\ntgWOgvaPMGHfzC6vKNFJkvuZkRPVQO0LQaTKDYms4B3Sm3xVCekBDKBa4CnWe3hvqA/mC5YnJKj3\nlzqz9Xdupg6QAA7eI2O104FbVHeSG2/SqzWNtcUMNx8jBV7m7xUqsa02YLiI8o9FDwuS1GOY8VCT\nTZoaHBsNbyAnfqrLDUA0Ekgk3P5OyAOLWc4HukqUhb/tSS9LA5oAj93A3+S5FvUeoupkDiPn/Rc3\n0wDwjzKgCAfRCklvT6oRSA7sqdYK7UHG9iZXMN3u0LrSLup9lIDnNJ4+/DzQ2ADfzuhzoFhJ8h8z\nxSa5ERJjjsgBIjh85SkTaYSUgXCP7J5w45f1QBzp1OESfdP0WvuOZ+y5VWaYItflK7NEkmZ8xI9A\ngBlNk8D62CjuwcchfwxfT0C71TG8+0fJRn19yLEIAi5hSkXPibefWPUqKKT2nQKZZPiJcPi69N9l\nNwXhdTc5uvxGqQYMxcBWdXEMqGWy6JuWRE8DK5tJsE2isw+Vnd0GReItK7twwbZrfpuutQciPKEj\naR4t35QnSoDuxluI8wuZEbyPRKDAgyimehspAfSECR9Auj3TvIS077tP2SVKc3CAG9yOfkmVHAbD\nT1hdncj/AGUZ1KSOXNACz5EfNP7ubwm6QOA8wnmSOfkgBarIFoUR5K7vPS3NcxBBm6AONuQ9j/RK\nl0fmSkQB2G3qurWhCEADdzbY/ZLUHA3uhCAHtYBpgRZdHGGkjghCAOIuJKSkbfngEIQAtSqYmxtx\nUHE0xoceOk/RKhABPhbb9wfQIwrAdx1QhJ9gdQwX8kxrjHkkQnAkU7z5JwCEIAe2lvd3HiulCnPE\n+6RCAOYdvxvx80OMEoQgDnXbslw/NCEAI6qdk11MAEoQoYHHUkQhLYH/2Q==\n
13	Francis	Medina	18646516	foto_candidato/18646516.jpeg	1	24		2015-04-16 14:08:15.536784-04:30	2015-04-23 14:54:57.704619-04:30	10	1	1	t	/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAd\nHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5Ojf/2wBDAQoKCg0MDRoPDxo3JR8lNzc3Nzc3\nNzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzf/wAARCADnALQDASIA\nAhEBAxEB/8QAHAAAAQUBAQEAAAAAAAAAAAAAAAEDBAYHAgUI/8QAPxAAAQMCBAMGBAMGBQQDAAAA\nAQACAwQRBRIhMQZBUQcTIjJhcRSBkaEVQrEjUnKSwdElM0NigjREU7Jk8PH/xAAZAQACAwEAAAAA\nAAAAAAAAAAACBAABAwX/xAAkEQACAgICAgIDAQEAAAAAAAAAAQIRAyEEMRIyIkETM1Fhcf/aAAwD\nAQACEQMRAD8A3Ermy6QoQ5siy6QoQ5slCVITZQgFIhxA3XjY1xHQYQ39vKO85Rt1JVpN9AyaXZ7N\n1y4jqstxHtBrZXEUTO4Zbcm7l4h4pxp8t218u97XWqwyM3NG1OkY3zOA9yhkzHOIa9p9isNr8exG\ndxNRVSuJ/wB1kxT4vWxP/Y1UzDys9F+FlrJs30OB5pQQdisjwrjvE6R4bVEVEY5uNirrgfGeGYsW\nxiQw1B/05NL+xQPFJF+aLOhcRyBzb305LtZMIELpIAb+igQiEpCLKFUcZAjLZdIKuyhQhAQqLFQh\nChYIQhQgLlzsouUrtAVT+OeIXYdTCkpnZZ5m6n90IoxcnRUnSsicX8ZGke6hwy3f7SSHUNHos3qa\niSolMs0r5Hnd2t03NLcnOb31uozpL310Olk5GKiqQu3b2I8nqiCSzr3Tb2OcfC026rkNds3dGgWx\n2aUOcbk3SRPAJ8Vr7pvI4G53Q64CjK/0lk3aAbHS9wm+8IduR0smHPLgHDQhOw/tNOY1urRG7L5w\ndxpJTyR0eJTF0J0bI78vutQglbKwOa4FpFwV87m8ZC0XgPidxDaCsdcDyu52S+XHe0aQlXZpN0qb\njdmF11dKjB0hIEFQgiUJEoUKFQhChYIQhQgIQkJsoQi4lVNo6OSd9srG3WIY7iMldXSVErsxkJ+i\n0XtDxMw0jKJhs6U3d/CFlVSS6QX25JnDGlZjkdkdxzHL+8dU5HD3j2jnmRBC55JA0HNephtPmqIr\n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\nfhDDzuf1QhYcr9YzxvctoFhZCELnWPH/2Q==\n
17	Jesus Gerardo	Laya Garcia	18974984	foto_candidato/18974984.jpeg	2	26		2015-04-16 15:09:33.212865-04:30	2015-05-06 09:42:26.071006-04:30	14	1	1	t	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\n+2fhSpUqID//2Q==\n
14	Jose Rafael	Solorzano Ramirez	19787549	foto_candidato/19787549.jpeg	2	27		2015-04-16 14:52:55.588506-04:30	2015-05-06 09:42:43.598048-04:30	11	1	1	t	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\n
16	Josue	Aponte	14894894	foto_candidato/14894894.jpeg	2	35		2015-04-16 14:59:47.635354-04:30	2015-05-06 09:42:59.919701-04:30	13	1	1	t	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\n30Oj9hwsTHU24mJ7o3gAT6hRmlSqk+SI/9k=\n
15	Marcel Robert	Arcuri Gomez	19363480	foto_candidato/19363480.jpeg	2	25		2015-04-16 14:53:49.353069-04:30	2015-05-06 09:43:17.68377-04:30	12	1	1	t	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\n
20	Luis	Monagas	17848484	foto_candidato/17848484.jpeg	2	28		2015-04-23 11:46:13.582863-04:30	2015-05-06 09:43:40.683553-04:30	10	1	1	f	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\n
26	Pedro	Camejo	19358484	foto_candidato/19358484.jpeg	2	45		2015-05-12 10:21:26.743111-04:30	2015-05-13 09:23:17.46121-04:30	10	1	1	f	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\nCEH/2Q==\n
\.


--
-- TOC entry 2476 (class 0 OID 0)
-- Dependencies: 183
-- Name: candidatos_candidatos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('candidatos_candidatos_id_seq', 27, true);


--
-- TOC entry 2418 (class 0 OID 16775)
-- Dependencies: 184
-- Data for Name: categoria_eleccion_categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY categoria_eleccion_categoria (id, categoria, fecha_create, fecha_update, user_create_id, user_update_id) FROM stdin;
1	Nacionales	2015-03-20 10:17:11.105458-04:30	2015-03-20 10:17:11.105533-04:30	2	\N
2	Municipales	2015-03-20 10:18:16.592247-04:30	2015-03-20 10:18:16.592304-04:30	2	\N
4	Parroquiales	2015-03-20 10:18:45.981526-04:30	2015-03-20 10:18:45.981588-04:30	2	\N
5	Por Circuitos	2015-03-20 10:19:02.114641-04:30	2015-03-20 10:19:02.114698-04:30	2	\N
9	Poligonales	2015-03-27 11:06:00.955393-04:30	2015-03-27 11:06:00.95546-04:30	1	\N
3	Estadales	2015-03-20 10:18:31.257255-04:30	2015-04-06 10:23:36.293448-04:30	2	1
\.


--
-- TOC entry 2477 (class 0 OID 0)
-- Dependencies: 185
-- Name: categoria_eleccion_categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('categoria_eleccion_categoria_id_seq', 11, true);


--
-- TOC entry 2435 (class 0 OID 16831)
-- Dependencies: 201
-- Data for Name: estados_estado; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY estados_estado (id, cod_estado, estado) FROM stdin;
1	4	Aragua
2	5	Amazonas
3	6	Carabobo
4	2	Apure
7	24	Zulia
5	3	Anzoategui
6	14	Nueva Esparta
9	12	Miranda
\.


--
-- TOC entry 2420 (class 0 OID 16780)
-- Dependencies: 186
-- Data for Name: centro_votacion_centros; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY centro_votacion_centros (id, nombre, municipio, parroquia, cod_n, direccion, fecha_create, fecha_update, estado_id, user_create_id, user_update_id) FROM stdin;
1	E.B.E.Julio Morales Laras	1	1	401010001	\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLa Barraca\r\n\t\t    \r\n\t\t    \r\n\t\t    \r\n\t\t    \r\n\t\t    	2015-03-20 10:16:02.10017-04:30	2015-04-06 10:01:45.319293-04:30	4	2	1
4	U. E. Humbolt	1	1	40101001	Av. Sucre\r\n\t\t    	2015-04-21 08:53:37.508904-04:30	2015-04-21 09:00:22.880772-04:30	4	1	1
\.


--
-- TOC entry 2478 (class 0 OID 0)
-- Dependencies: 187
-- Name: centro_votacion_centros_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('centro_votacion_centros_id_seq', 5, true);


--
-- TOC entry 2422 (class 0 OID 16788)
-- Dependencies: 188
-- Data for Name: circuitos_circuito; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY circuitos_circuito (id, n_circuito, num_max_candidatos, fecha_create, fecha_update, estado_id, user_create_id, user_update_id) FROM stdin;
1	1	10	2015-03-20 10:13:34.228943-04:30	2015-03-20 10:13:34.229005-04:30	4	2	\N
2	1	10	2015-03-20 15:42:16.006116-04:30	2015-03-20 15:42:16.006174-04:30	5	2	\N
3	2	10	2015-03-20 15:42:26.573606-04:30	2015-03-20 15:42:26.573665-04:30	5	2	\N
4	2	10	2015-03-20 15:42:48.197174-04:30	2015-03-20 15:42:48.197245-04:30	4	2	\N
5	1	5	2015-03-20 15:43:17.34559-04:30	2015-03-20 15:43:17.345648-04:30	6	2	\N
6	2	5	2015-03-20 15:43:31.32609-04:30	2015-03-20 15:43:31.32615-04:30	6	2	\N
9	12	12	2015-03-25 11:22:06.433982-04:30	2015-04-20 10:49:39.007555-04:30	4	1	1
\.


--
-- TOC entry 2479 (class 0 OID 0)
-- Dependencies: 189
-- Name: circuitos_circuito_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('circuitos_circuito_id_seq', 10, true);


--
-- TOC entry 2424 (class 0 OID 16793)
-- Dependencies: 190
-- Data for Name: corsheaders_corsmodel; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY corsheaders_corsmodel (id, cors) FROM stdin;
\.


--
-- TOC entry 2480 (class 0 OID 0)
-- Dependencies: 191
-- Name: corsheaders_corsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('corsheaders_corsmodel_id_seq', 1, false);


--
-- TOC entry 2426 (class 0 OID 16798)
-- Dependencies: 192
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
3	2015-03-23 10:33:23.989968-04:30	1	admin	2	Modifica groups.	4	1
4	2015-03-23 14:17:51.127419-04:30	3	marcel	1		4	1
5	2015-03-23 14:18:02.815002-04:30	3	marcel	2	Modifica groups.	4	1
6	2015-03-23 14:18:25.887545-04:30	2	japonte	2	Modifica groups.	4	1
7	2015-06-03 15:34:52.045686-04:30	6	Aplicar	1		3	1
8	2015-06-03 15:35:04.687543-04:30	1	admin	2	Modifica groups.	4	1
9	2015-06-04 10:41:20.687906-04:30	4	encuestador	1		4	1
10	2015-06-04 10:41:28.210785-04:30	4	encuestador	2	Modifica groups.	4	1
\.


--
-- TOC entry 2481 (class 0 OID 0)
-- Dependencies: 193
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 10, true);


--
-- TOC entry 2482 (class 0 OID 0)
-- Dependencies: 195
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_content_type_id_seq', 27, true);


--
-- TOC entry 2430 (class 0 OID 16812)
-- Dependencies: 196
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2015-03-20 18:54:41.075378-04:30
2	auth	0001_initial	2015-03-20 18:54:41.692552-04:30
3	admin	0001_initial	2015-03-20 18:54:41.860395-04:30
4	partidos	0001_initial	2015-03-20 18:54:42.39325-04:30
5	candidatos	0001_initial	2015-03-20 18:54:42.718675-04:30
6	categoria_eleccion	0001_initial	2015-03-20 18:54:42.911724-04:30
7	estados	0001_initial	2015-03-20 18:54:43.045166-04:30
8	centro_votacion	0001_initial	2015-03-20 18:54:43.386186-04:30
9	circuitos	0001_initial	2015-03-20 18:54:43.629174-04:30
10	elecciones	0001_initial	2015-03-20 18:54:43.870772-04:30
11	exitpoll	0001_initial	2015-03-20 18:54:44.196577-04:30
12	grupo_etareo	0001_initial	2015-03-20 18:54:44.455057-04:30
13	login	0001_initial	2015-03-20 18:54:44.571885-04:30
14	municipios	0001_initial	2015-03-20 18:54:44.737689-04:30
15	parroquias	0001_initial	2015-03-20 18:54:44.879504-04:30
16	sessions	0001_initial	2015-03-20 18:54:45.022492-04:30
17	tipo_eleccion	0001_initial	2015-03-20 18:54:45.26577-04:30
18	votacion	0001_initial	2015-03-20 18:54:45.506493-04:30
19	sectores	0001_initial	2015-03-24 08:59:57.19608-04:30
28	poligonales	0001_initial	2015-04-06 08:46:43.001232-04:30
29	candidatos	0002_candidatos_foto_binario	2015-04-23 11:47:05.599337-04:30
30	votacion	0002_votacion_sexo	2015-04-24 11:52:36.250431-04:30
31	aplicada	0001_initial	2015-06-02 09:03:22.519418-04:30
32	aplicada	0002_encuestaresultado_otras	2015-06-02 09:03:22.599578-04:30
33	encuestas	0001_initial	2015-06-02 09:03:23.049798-04:30
34	encuestas	0002_auto_20150530_2120	2015-06-02 09:03:23.127584-04:30
35	preguntas	0001_initial	2015-06-02 09:03:23.380548-04:30
36	respuestas	0001_initial	2015-06-02 09:03:23.660493-04:30
37	sectores	0002_auto_20150530_1927	2015-06-02 09:03:23.795379-04:30
38	aplicada	0003_auto_20150603_1438	2015-06-03 15:20:07.086038-04:30
\.


--
-- TOC entry 2483 (class 0 OID 0)
-- Dependencies: 197
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('django_migrations_id_seq', 38, true);


--
-- TOC entry 2432 (class 0 OID 16820)
-- Dependencies: 198
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
0ww9j4gfi23nvw0pi3apohcvg48cjak1	ZjQxMTg1NjA2NjIxYmRlNmYyOWRjZDRmMzVkZjFhM2ZiNmRlODRiMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImE2YTZlMDU2NmY4MGNiODIxMWM2ZTNjMmQzYzM0NWI0ZWYxMDUyYWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9	2015-04-03 19:03:44.720291-04:30
d6436jwapeq3nm96caff85k74w4fpthe	ZjQxMTg1NjA2NjIxYmRlNmYyOWRjZDRmMzVkZjFhM2ZiNmRlODRiMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImE2YTZlMDU2NmY4MGNiODIxMWM2ZTNjMmQzYzM0NWI0ZWYxMDUyYWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9	2015-04-03 10:02:32.164467-04:30
we78n2h82tuugg3hsr09ly9hpafnak56	ZjQxMTg1NjA2NjIxYmRlNmYyOWRjZDRmMzVkZjFhM2ZiNmRlODRiMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImE2YTZlMDU2NmY4MGNiODIxMWM2ZTNjMmQzYzM0NWI0ZWYxMDUyYWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9	2015-04-03 10:12:02.12545-04:30
poq7ofzfe2kzsmsukvimbc9696ryfxcg	ZjQxMTg1NjA2NjIxYmRlNmYyOWRjZDRmMzVkZjFhM2ZiNmRlODRiMzp7Il9hdXRoX3VzZXJfaGFzaCI6ImE2YTZlMDU2NmY4MGNiODIxMWM2ZTNjMmQzYzM0NWI0ZWYxMDUyYWEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjJ9	2015-04-03 15:16:11.59436-04:30
dcmcinm143iuj4oslnkk5eq1zrsp5bk1	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-09 15:05:17.134183-04:30
irgawc9jp5mth4t4djpb2z6419bcd891	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-06 11:28:05.429627-04:30
pak2raf8tnatr26ae4y79z5fe8suje9h	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-06 11:37:33.284901-04:30
7gdbkcihnfl4fg0vwi6ggdivy2ja82t4	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-06 11:41:03.275839-04:30
l2piawo8lr5m9qszglup13l43uw9nypn	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-06 13:57:06.685156-04:30
ka7iaqbj8x5b1ypj6hh98v68jk4pc9cw	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-06 14:28:41.257538-04:30
cd4b4g6tykwq1ctwtvk45egpfyx4nduk	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-04-06 16:21:25.252502-04:30
wio95yqpziycjk3h3k290r9g3fx151kn	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-07 11:24:22.424137-04:30
iuryt109bjy6o6fleejjcnbptc68d73i	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-07 12:16:35.201346-04:30
ap9sy8j99h6mewfuxy3ya3g7slmojgl1	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-08 08:27:50.310237-04:30
nnakj9yh6k8nnmv209y6b0c2pyeztihm	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-27 11:27:17.651096-04:30
pi636i6l3dnfpspsrn1eaav3mbp1h06g	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-27 14:34:41.087294-04:30
z193h2ydw80ohvrrefmcfm2d27kiyoam	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-04 11:55:56.76934-04:30
j928h4n03di5lfhrjj52ugnicpunrgz2	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-05 12:42:40.607396-04:30
itf0889wa4quwjf4jp9cjf1fsgvi30cy	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-09 14:48:05.093571-04:30
yenhozgxi5ihtsvewd02hclvifxaa3cv	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-09 14:48:47.857947-04:30
8qfjnodskozqsjld0ufjyxn60cf6rf5s	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-04-09 15:02:44.249955-04:30
8zl2zi5pv96nmvagiyzdex16is6zld1t	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-05-05 13:17:20.805245-04:30
zmr5164cqgrua2yb0zmb9omvjw1m4o4m	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-05-07 13:55:23.482591-04:30
h6jdv7dh6x2hq8a4n3qw0a66g2qsofir	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-11 13:32:03.824178-04:30
xt5hic8yomuh3zx4kb5j07bh8a0gvj7s	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-12 10:31:22.852581-04:30
ropvxhn6pie2ly9rdzohcv86yavkhtaa	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-05-14 13:25:38.359114-04:30
br3k8q84zj9n1qpt5q2evp1p14mb8v1v	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-05-14 14:43:19.611135-04:30
mtpka01himh64bzqpnbycix36vmyg8po	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-05-18 10:05:35.919057-04:30
ifpemmnstpcomled2i8zhskvn3mouv1b	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-19 08:46:02.110229-04:30
e5cne5hf4ehq2bsq4e0o5wxox4toy1wa	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-19 10:32:25.952172-04:30
62nvxy7pcqo5zk0bfdrda0xr9nnuu4uk	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-20 13:53:59.28934-04:30
3kmyg4dro73psn66i7flq13aklum8t3x	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-25 13:44:07.079606-04:30
k4u6z23fqxdejlssjc8i6d6er50h52qq	ZGQ4MDM3ZTE0N2MzODM3Nzg4MTg5Njk3MjU4YTkxZTYxY2E4NmZjYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIyYWJiZDc2NWU2ZWQzNTUwMzlmZjIyZGJmZDg5NjM2Nzk5OTM1OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9	2015-06-18 10:49:32.180228-04:30
jc1hqrpvepqn75u6ngroxlhfw9b6oqsd	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-05-27 09:17:45.218965-04:30
66ta9serbf7t7y01kcsg06aw95a9jiqh	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-18 10:51:32.294562-04:30
65mhzwkpnmsvlmgxjzuyfcbhgyh411yq	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-08 08:44:04.883377-04:30
b65i6eankqshkcvfzebjqz6yb9e0bs1b	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-09 08:32:40.704774-04:30
oc5qx6wvkd8wa99qboq3l1bramolu8g3	ZGQ4MDM3ZTE0N2MzODM3Nzg4MTg5Njk3MjU4YTkxZTYxY2E4NmZjYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIyYWJiZDc2NWU2ZWQzNTUwMzlmZjIyZGJmZDg5NjM2Nzk5OTM1OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9	2015-06-18 11:00:36.925621-04:30
lhxz3bqam9ezp3f878i83jqwim06i6ja	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-16 10:16:34.486731-04:30
f8kgymg0ylqudfbxv0ny3fwj1k090cg2	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-18 11:07:46.287027-04:30
gw4owqtzq1sd3iazis6ls8l5n8le33zm	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-16 10:30:44.573246-04:30
htwehfclblr0fyxmkoywmtykbrirpnm0	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-16 13:46:33.524927-04:30
y215hu5jgr8rvjsoqbitephgybc5hopj	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-18 11:12:06.015094-04:30
afpjtp3uttnf39alavd8bzpizoz3xn43	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-16 14:11:21.359861-04:30
bn65nhciie7jwowt7hn9d2pu87d0k66f	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-18 11:12:39.705051-04:30
cfezq34nzxis3fpokbbc89162q2qwkmr	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-18 11:13:06.605983-04:30
74npt5vfdfihn6n6bchzj5pq6wnz64le	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-18 12:04:38.209023-04:30
3axg6ju91pfuzmx7r7hy56vhgtn7kxc0	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-18 13:21:27.085598-04:30
2ectzp8ob2jstkdr8rhx85onbr1fnznt	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-16 15:10:48.403842-04:30
hva5lnpxlcy2gj8k8wu3l504lwljtk57	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-18 14:56:07.333049-04:30
ier3gpqfj6llrrrdjqw9vxzbz7r6hw20	NWU2M2QzOTI1MWMxYzkwOGEzNmNmYTljNzA2NTNjZjcyMWY1MDI4YTp7fQ==	2015-06-17 16:10:13.036676-04:30
mbpri322pnkvgxa3gtjk51mmxpl4ftft	OTI4MzRhY2MzYWQ2ODQ4MjU0MGQ4NmM3N2M4YWJmYjU2MTZhNzMyMTp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4Njg5YjYzMmNiMzNkMjBiM2YyMWIxYjRhMjIzMWIzNGU0ZTEyM2EiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9	2015-06-17 16:16:34.48398-04:30
oxv17bmz56tmusq7kz954x0a5ftge9ai	ZGQ4MDM3ZTE0N2MzODM3Nzg4MTg5Njk3MjU4YTkxZTYxY2E4NmZjYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIyYWJiZDc2NWU2ZWQzNTUwMzlmZjIyZGJmZDg5NjM2Nzk5OTM1OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9	2015-06-18 10:44:22.957631-04:30
qse7ic8tekobw0gx3pzwz3gm7mu8xvks	ZGQ4MDM3ZTE0N2MzODM3Nzg4MTg5Njk3MjU4YTkxZTYxY2E4NmZjYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIyYWJiZDc2NWU2ZWQzNTUwMzlmZjIyZGJmZDg5NjM2Nzk5OTM1OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9	2015-06-18 10:46:47.198243-04:30
goym1hjct6frwciuoc2tlkzlxv3g4mh6	ZGQ4MDM3ZTE0N2MzODM3Nzg4MTg5Njk3MjU4YTkxZTYxY2E4NmZjYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIyYWJiZDc2NWU2ZWQzNTUwMzlmZjIyZGJmZDg5NjM2Nzk5OTM1OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9	2015-06-18 10:46:47.339086-04:30
9nzhvx2u0rk36kb5by6tmf3jlm4vrcfr	ZGQ4MDM3ZTE0N2MzODM3Nzg4MTg5Njk3MjU4YTkxZTYxY2E4NmZjYTp7Il9hdXRoX3VzZXJfaGFzaCI6ImIyYWJiZDc2NWU2ZWQzNTUwMzlmZjIyZGJmZDg5NjM2Nzk5OTM1OTUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjR9	2015-06-18 10:47:51.242108-04:30
\.


--
-- TOC entry 2433 (class 0 OID 16826)
-- Dependencies: 199
-- Data for Name: elecciones_eleccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY elecciones_eleccion (id, nombre, tipo_eleccion, ele_activa, fecha_create, fecha_update, categoria_eleccion_id, user_create_id, user_update_id) FROM stdin;
2	Exit Poll Gobernaciones 2015	5	t	2015-03-20 10:27:26.28939-04:30	2015-03-20 10:27:39.002796-04:30	3	2	\N
1	Exit Poll Presidenciales 2015	1	t	2015-03-20 10:27:01.000392-04:30	2015-04-13 11:53:50.613819-04:30	1	\N	1
9	Comunal	3	f	2015-04-13 11:50:04.593-04:30	2015-04-30 13:15:14.511157-04:30	4	\N	1
3	Exit Poll Circuitos 2015	4	f	2015-03-20 10:29:02.309201-04:30	2015-04-30 13:15:21.246271-04:30	5	\N	1
4	Exit Poll Municipal 2015	2	f	2015-03-20 10:29:34.822168-04:30	2015-04-30 13:15:28.604528-04:30	2	\N	1
5	Exit Poll Parroquias 2015	3	f	2015-03-20 10:30:04.808199-04:30	2015-04-30 13:15:34.283359-04:30	4	\N	1
\.


--
-- TOC entry 2484 (class 0 OID 0)
-- Dependencies: 200
-- Name: elecciones_eleccion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('elecciones_eleccion_id_seq', 11, true);


--
-- TOC entry 2460 (class 0 OID 26248)
-- Dependencies: 226
-- Data for Name: encuestas_encuesta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY encuestas_encuesta (id, cod_encuesta, nombre, estatus, fecha_create, fecha_update, user_create_id, user_update_id) FROM stdin;
1	1	Encuesta de Beisbol Venezolano	2	2015-06-02	2015-06-02	1	\N
3	3	Encuestra de Prueba 2	1	2015-06-02	2015-06-02	1	\N
2	2	Encuestra de Prueba	2	2015-06-02	2015-06-02	\N	\N
5	5	Encuesta Real	2	2015-06-02	2015-06-02	1	\N
4	4	E3	3	2015-06-02	2015-06-02	1	\N
6	6	Encuesta Nueva	1	2015-06-03	2015-06-03	1	\N
7	7	nueva pregunta	1	2015-06-03	2015-06-03	1	\N
8	8	Nueva encuesta 2	1	2015-06-03	2015-06-03	1	\N
\.


--
-- TOC entry 2485 (class 0 OID 0)
-- Dependencies: 225
-- Name: encuestas_encuesta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('encuestas_encuesta_id_seq', 8, true);


--
-- TOC entry 2486 (class 0 OID 0)
-- Dependencies: 202
-- Name: estados_estado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('estados_estado_id_seq', 13, true);


--
-- TOC entry 2437 (class 0 OID 16836)
-- Dependencies: 203
-- Data for Name: exitpoll_exitpoll; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY exitpoll_exitpoll (id, municipio, parroquia, circuito, fecha_create, fecha_update, candidatos_id, eleccion_id, estado_id, user_create_id, user_update_id, sector, poligonal, centro) FROM stdin;
21	\N	\N	\N	2015-04-16 15:00:06.967118-04:30	2015-04-16 15:00:06.967178-04:30	13	1	\N	1	\N	\N	\N	\N
22	\N	\N	\N	2015-04-16 15:00:23.033082-04:30	2015-04-16 15:00:23.033139-04:30	14	1	\N	1	\N	\N	\N	\N
23	\N	\N	\N	2015-04-16 15:00:34.44251-04:30	2015-04-16 15:00:34.442571-04:30	16	1	\N	1	\N	\N	\N	\N
24	\N	\N	\N	2015-04-16 15:00:44.027264-04:30	2015-04-16 15:00:44.027322-04:30	15	1	\N	1	\N	\N	\N	\N
25	\N	\N	\N	2015-04-16 15:09:59.657571-04:30	2015-04-16 15:09:59.657633-04:30	17	1	\N	1	\N	\N	\N	\N
26	\N	\N	\N	2015-04-27 14:40:48.679345-04:30	2015-04-27 14:40:48.679403-04:30	20	2	4	1	\N	\N	\N	\N
27	\N	\N	\N	2015-04-30 13:16:29.794493-04:30	2015-04-30 13:16:29.79455-04:30	15	2	4	1	\N	\N	\N	\N
28	\N	\N	\N	2015-04-30 13:16:51.929872-04:30	2015-04-30 13:16:51.929929-04:30	13	2	4	1	\N	\N	\N	\N
29	\N	\N	\N	2015-04-30 13:17:10.14427-04:30	2015-04-30 13:17:10.144329-04:30	14	2	4	1	\N	\N	\N	\N
30	\N	\N	\N	2015-04-30 13:17:37.424818-04:30	2015-04-30 13:17:37.424874-04:30	17	2	4	1	\N	\N	\N	\N
31	\N	\N	\N	2015-04-30 13:17:55.329683-04:30	2015-04-30 13:17:55.329756-04:30	16	2	4	1	\N	\N	\N	\N
\.


--
-- TOC entry 2487 (class 0 OID 0)
-- Dependencies: 204
-- Name: exitpoll_exitpoll_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('exitpoll_exitpoll_id_seq', 32, true);


--
-- TOC entry 2439 (class 0 OID 16842)
-- Dependencies: 205
-- Data for Name: grupo_etareo_grupo_etareo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY grupo_etareo_grupo_etareo (id, descripcion, grupo_etareo, fecha_create, fecha_update, user_create_id, user_update_id) FROM stdin;
3	Adulto Mayor	65-80	2015-03-25 14:22:42.441182-04:30	2015-03-25 14:22:42.441242-04:30	\N	\N
2	Adulto	35-55	2015-03-23 11:32:24.673599-04:30	2015-03-25 14:54:31.104477-04:30	1	1
1	Grupo Joven	18-35	2015-03-20 10:16:47.834491-04:30	2015-04-21 08:37:40.269292-04:30	2	1
\.


--
-- TOC entry 2488 (class 0 OID 0)
-- Dependencies: 206
-- Name: grupo_etareo_grupo_etareo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('grupo_etareo_grupo_etareo_id_seq', 4, true);


--
-- TOC entry 2441 (class 0 OID 16847)
-- Dependencies: 207
-- Data for Name: login_perfilesusuario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY login_perfilesusuario (id, tlf, user_accion, user_id) FROM stdin;
\.


--
-- TOC entry 2489 (class 0 OID 0)
-- Dependencies: 208
-- Name: login_perfilesusuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('login_perfilesusuario_id_seq', 1, false);


--
-- TOC entry 2443 (class 0 OID 16852)
-- Dependencies: 209
-- Data for Name: municipios_municipio; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY municipios_municipio (id, circuito, cod_municipio, municipio, estado_id) FROM stdin;
1	1	1	Girardot	4
2	1	2	Mario Briceño	4
3	8	1	Bolívar	3
4	3	10	Caroní	5
8	1	8	Acacias	4
6	8	12	Nuevo Pueblo	3
\.


--
-- TOC entry 2490 (class 0 OID 0)
-- Dependencies: 210
-- Name: municipios_municipio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('municipios_municipio_id_seq', 9, true);


--
-- TOC entry 2445 (class 0 OID 16857)
-- Dependencies: 211
-- Data for Name: parroquias_parroquia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY parroquias_parroquia (id, parroquia, cod_parroquia, municipio, estado_id) FROM stdin;
1	Madre María de San José	1	1	4
4	Carmen Sofia	1	10	5
2	Mi Señora del Carmen	1	1	3
5	El Limon	13	8	4
6	Prueba 	0	8	4
\.


--
-- TOC entry 2491 (class 0 OID 0)
-- Dependencies: 212
-- Name: parroquias_parroquia_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('parroquias_parroquia_id_seq', 6, true);


--
-- TOC entry 2492 (class 0 OID 0)
-- Dependencies: 214
-- Name: partidos_partidos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('partidos_partidos_id_seq', 16, true);


--
-- TOC entry 2449 (class 0 OID 16870)
-- Dependencies: 215
-- Data for Name: poligonales_poligonal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY poligonales_poligonal (id, municipio, parroquia, poligonal, fecha_create, fecha_update, estado_id, user_create_id, user_update_id, sector, cod_pol) FROM stdin;
6	1	1	Poligonal Norte	2015-03-27 15:29:20.143138-04:30	2015-03-30 10:35:48.237983-04:30	4	1	1	14	14
12	1	1	Poligonal H	2015-03-27 15:49:46.013359-04:30	2015-03-31 13:32:58.258024-04:30	4	1	1	14	12
4	1	1	Poligonal 1A	2015-03-26 12:00:26.643528-04:30	2015-04-06 10:32:57.210456-04:30	4	1	1	1	1
14	1	1	Poligonal H	2015-04-20 15:09:00.596714-04:30	2015-04-20 15:09:00.596773-04:30	4	1	\N	1	44
13	1	1	Poligonal H	2015-04-20 15:09:00.11489-04:30	2015-04-20 15:10:16.089189-04:30	4	1	1	1	11
5	1	1	Jesus P	2015-03-27 15:11:17.676393-04:30	2015-04-20 15:16:20.859848-04:30	4	1	1	8	8
\.


--
-- TOC entry 2493 (class 0 OID 0)
-- Dependencies: 216
-- Name: poligonales_poligonal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('poligonales_poligonal_id_seq', 14, true);


--
-- TOC entry 2462 (class 0 OID 26270)
-- Dependencies: 228
-- Data for Name: preguntas_preguntas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY preguntas_preguntas (id, cod_encuesta, cod_pregunta, pregunta, tipo, fecha_create, fecha_update, user_create_id, user_update_id) FROM stdin;
1	1	1	¿Te gusta el Beisbol?	1	2015-06-02	2015-06-02	1	\N
2	1	2	¿Vez Beisbol Nacional?	1	2015-06-02	2015-06-02	1	\N
3	1	3	¿Cuál Equipo te gusta más?	1	2015-06-02	2015-06-02	1	\N
5	1	5	¿Cuál de los Estadios actuales de nuestro Beisbol Nacional le gusta más?	1	2015-06-02	2015-06-02	1	\N
4	1	4	¿De los jugadores historicos de nuestro Beisbol Nacional con cual(es) te quedas?	2	2015-06-02	2015-06-02	1	\N
6	2	1	Pregunta numero 1	1	2015-06-02	2015-06-02	1	\N
7	2	2	Pregunta Número 2	2	2015-06-02	2015-06-02	1	\N
8	3	1	P1	1	2015-06-02	2015-06-02	1	\N
9	4	1	p1	2	2015-06-02	2015-06-02	1	\N
10	5	1	Pregunta Excluyente	1	2015-06-02	2015-06-02	1	\N
11	5	2	Pregunta No excluyente	2	2015-06-02	2015-06-02	1	\N
13	5	3	pregunta excluyente	1	2015-06-02	2015-06-02	1	\N
14	6	1	pregunta numero 1	1	2015-06-03	2015-06-03	1	\N
15	6	2	pregunta numero 1	1	2015-06-03	2015-06-03	1	\N
16	6	3	p1	1	2015-06-03	2015-06-03	1	\N
18	7	2	p2	1	2015-06-03	2015-06-03	1	\N
19	7	3	p3	1	2015-06-03	2015-06-03	1	\N
20	7	4	p1	1	2015-06-03	2015-06-03	1	\N
21	8	1	Pregunta nueva	1	2015-06-03	2015-06-03	1	\N
\.


--
-- TOC entry 2494 (class 0 OID 0)
-- Dependencies: 227
-- Name: preguntas_preguntas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('preguntas_preguntas_id_seq', 21, true);


--
-- TOC entry 2464 (class 0 OID 26292)
-- Dependencies: 230
-- Data for Name: respuestas_respuestas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY respuestas_respuestas (id, cod_pregunta, cod_respuesta, respuesta, tipo, fecha_create, fecha_update, user_create_id, user_update_id) FROM stdin;
1	1	1	Si	1	2015-06-02	2015-06-02	1	\N
2	1	2	Un poco	1	2015-06-02	2015-06-02	1	\N
3	1	3	No mucho	1	2015-06-02	2015-06-02	1	\N
4	1	4	No	1	2015-06-02	2015-06-02	1	\N
5	2	1	Si	1	2015-06-02	2015-06-02	1	\N
6	2	2	No	1	2015-06-02	2015-06-02	1	\N
7	3	1	Leones del Caracas	1	2015-06-02	2015-06-02	1	\N
8	3	2	Navegantes del Magallanes	1	2015-06-02	2015-06-02	1	\N
9	3	3	Tigres de Aragua	1	2015-06-02	2015-06-02	1	\N
10	3	4	Aguilas del Zulia	1	2015-06-02	2015-06-02	1	\N
11	3	5	Cardenales de Lara	1	2015-06-02	2015-06-02	1	\N
12	3	6	Caribes de Anzoategui	1	2015-06-02	2015-06-02	1	\N
13	3	7	Tiburones de la Guaira	1	2015-06-02	2015-06-02	1	\N
14	3	8	Bravos de Margarita	1	2015-06-02	2015-06-02	1	\N
15	4	1	Andrés Galarraga	1	2015-06-02	2015-06-02	1	\N
16	4	2	Luis Sojo	1	2015-06-02	2015-06-02	1	\N
17	4	3	David Concepción 	1	2015-06-02	2015-06-02	1	\N
18	4	4	Luis Aparicio	1	2015-06-02	2015-06-02	1	\N
19	4	5	Miguel Cabrera	1	2015-06-02	2015-06-02	1	\N
20	4	6	Otro	2	2015-06-02	2015-06-02	1	\N
21	5	1	Universitario de Caracas - (Leones del Caracas y Tiburones de la Guaira)	1	2015-06-02	2015-06-02	1	\N
22	5	2	Luis Aparicio 'El Grande' - (Aguilas del Zulia)	1	2015-06-02	2015-06-02	1	\N
24	5	4	Nueva Esparta 'Guatamare' - (Bravos de Margarita)	1	2015-06-02	2015-06-02	1	\N
25	5	5	Antonio Herrera Gutiérrez - (Cardenales de Lara)	1	2015-06-02	2015-06-02	1	\N
26	5	6	Alfonso Carrasquel - (Caribes de Anzoátegui)	1	2015-06-02	2015-06-02	1	\N
27	5	7	José Bernardo Peréz - (Navegantes de Magallenes)	1	2015-06-02	2015-06-02	1	\N
23	5	3	José Pérez Colmenares - (Tigres de Aragua)	1	2015-06-02	2015-06-02	1	1
28	6	1	Respuesta número 1	1	2015-06-02	2015-06-02	1	\N
29	7	1	Respuesta Número 2	2	2015-06-02	2015-06-02	1	\N
30	8	1	R1	1	2015-06-02	2015-06-02	1	\N
31	9	1	r1	1	2015-06-02	2015-06-02	1	\N
32	8	2	r2	2	2015-06-02	2015-06-02	1	\N
33	8	3	r3	1	2015-06-02	2015-06-02	1	\N
34	10	1	r1 cerrada	1	2015-06-02	2015-06-02	1	\N
35	10	2	r2 abierta	2	2015-06-02	2015-06-02	1	\N
36	10	3	r3 cerrada	1	2015-06-02	2015-06-02	1	\N
37	11	1	r1 cerrada	1	2015-06-02	2015-06-02	1	\N
38	11	2	resp2 abierta	2	2015-06-02	2015-06-02	1	\N
39	11	3	respuesta abierta	2	2015-06-02	2015-06-02	1	\N
40	12	1	resp 1 cerrada	1	2015-06-02	2015-06-02	1	\N
41	12	2	respue 2 abierta	2	2015-06-02	2015-06-02	1	\N
43	13	2	res 2 abierta	2	2015-06-02	2015-06-02	1	\N
42	13	1	res 1 cerrada	1	2015-06-02	2015-06-02	1	1
45	13	3	resp 3	1	2015-06-02	2015-06-02	1	\N
\.


--
-- TOC entry 2495 (class 0 OID 0)
-- Dependencies: 229
-- Name: respuestas_respuestas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('respuestas_respuestas_id_seq', 45, true);


--
-- TOC entry 2451 (class 0 OID 16875)
-- Dependencies: 217
-- Data for Name: sectores_sector; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY sectores_sector (id, sector, municipio, parroquia, fecha_create, fecha_update, estado_id, user_create_id, user_update_id, cod_s) FROM stdin;
11	Calicanto	1	1	2015-03-27 15:26:18.372618-04:30	2015-03-27 15:26:18.372677-04:30	4	1	\N	14
6	La Barraca	1	1	2015-03-26 11:58:24.893982-04:30	2015-04-06 10:33:06.120196-04:30	4	1	1	1
10	El Manchon	1	1	2015-03-27 14:36:36.474242-04:30	2015-04-17 11:15:56.06128-04:30	4	1	1	8
12	La soledad	1	1	2015-04-20 15:27:05.642707-04:30	2015-04-20 15:38:05.413608-04:30	4	1	1	22
9	casas	1	1	2015-03-27 14:33:59.281397-04:30	2015-05-12 14:17:34.459555-04:30	4	1	1	12
\.


--
-- TOC entry 2496 (class 0 OID 0)
-- Dependencies: 218
-- Name: sectores_sector_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('sectores_sector_id_seq', 12, true);


--
-- TOC entry 2453 (class 0 OID 16880)
-- Dependencies: 219
-- Data for Name: tipo_eleccion_tipo_eleccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY tipo_eleccion_tipo_eleccion (id, tipo, niveles, fecha_create, fecha_update, categoria_id, user_create_id, user_update_id) FROM stdin;
1	Presidenciales	5	2015-03-20 10:17:48.36601-04:30	2015-03-20 10:17:48.366069-04:30	1	2	\N
2	Alcaldias	2	2015-03-20 10:19:56.679662-04:30	2015-03-20 10:19:56.679719-04:30	2	2	\N
3	Parroquias	1	2015-03-20 10:20:32.604308-04:30	2015-03-20 10:20:32.604369-04:30	4	2	\N
4	Circuitos	3	2015-03-20 10:20:56.172554-04:30	2015-03-20 10:20:56.172611-04:30	5	2	\N
7	municipitos	2	2015-03-25 15:38:02.885407-04:30	2015-03-25 15:38:02.885464-04:30	2	1	\N
9	Poligonales	6	2015-03-27 11:06:32.241819-04:30	2015-03-27 11:06:32.241877-04:30	9	1	\N
10	UBCH	7	2015-03-27 11:15:10.038331-04:30	2015-03-27 11:15:10.038394-04:30	9	1	\N
5	Gobernaciones	4	2015-03-20 10:21:42.167952-04:30	2015-04-06 10:29:18.054499-04:30	3	2	1
6	Prueba xy	4	2015-03-25 15:37:47.148179-04:30	2015-04-06 10:37:20.611733-04:30	3	1	1
\.


--
-- TOC entry 2497 (class 0 OID 0)
-- Dependencies: 220
-- Name: tipo_eleccion_tipo_eleccion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('tipo_eleccion_tipo_eleccion_id_seq', 12, true);


--
-- TOC entry 2455 (class 0 OID 16885)
-- Dependencies: 221
-- Data for Name: votacion_votacion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY votacion_votacion (id, candidatos_id, eleccion_id, grupo_etareo_id, sexo) FROM stdin;
49	15	1	2	2
37	15	1	1	1
38	13	1	2	2
39	14	1	3	2
40	16	1	2	2
41	13	1	1	1
42	15	1	2	2
43	15	1	2	1
44	14	1	1	2
46	17	1	3	1
45	13	1	3	1
47	15	1	2	2
48	15	1	1	1
50	13	1	2	2
51	15	2	1	2
52	17	2	1	1
53	14	2	2	1
54	15	2	1	2
55	13	2	2	2
56	17	2	2	2
57	15	2	3	1
58	20	2	2	1
59	14	2	3	2
60	14	2	1	2
61	14	2	2	1
62	20	2	3	1
63	13	2	2	1
64	13	2	1	1
65	13	2	1	2
66	15	2	1	2
67	17	2	1	2
68	16	2	1	2
69	13	2	1	2
70	20	2	1	2
71	14	2	3	1
72	15	2	1	2
73	15	2	3	2
74	20	2	1	1
75	13	2	2	1
76	13	2	2	2
77	20	2	2	1
78	13	2	3	2
79	15	2	3	2
80	20	2	2	1
81	15	2	2	2
82	20	2	1	1
83	15	2	1	1
84	13	2	2	1
85	15	2	2	1
86	13	2	2	2
87	15	2	2	2
88	15	2	2	1
89	15	2	1	1
90	13	2	3	1
91	13	1	3	1
92	15	2	2	1
93	13	1	3	2
94	16	1	1	1
95	20	2	1	2
96	20	2	2	2
97	17	1	1	1
\.


--
-- TOC entry 2498 (class 0 OID 0)
-- Dependencies: 222
-- Name: votacion_votacion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('votacion_votacion_id_seq', 97, true);


-- Completed on 2015-06-05 15:25:17 VET

--
-- PostgreSQL database dump complete
--

