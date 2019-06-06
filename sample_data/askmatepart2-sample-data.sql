--
-- PostgreSQL database dump
--

-- Dumped from database version 11.2
-- Dumped by pg_dump version 11.2

-- Started on 2019-06-06 13:51:18 CEST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 199 (class 1259 OID 33010)
-- Name: answer; Type: TABLE; Schema: public; Owner: shadyhu1
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text,
    username text,
    user_id integer
);


ALTER TABLE public.answer OWNER TO shadyhu1;

--
-- TOC entry 198 (class 1259 OID 33008)
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: shadyhu1
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO shadyhu1;

--
-- TOC entry 3236 (class 0 OID 0)
-- Dependencies: 198
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shadyhu1
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- TOC entry 201 (class 1259 OID 33019)
-- Name: comment; Type: TABLE; Schema: public; Owner: shadyhu1
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer
);


ALTER TABLE public.comment OWNER TO shadyhu1;

--
-- TOC entry 200 (class 1259 OID 33017)
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: shadyhu1
--

CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO shadyhu1;

--
-- TOC entry 3237 (class 0 OID 0)
-- Dependencies: 200
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shadyhu1
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- TOC entry 197 (class 1259 OID 33001)
-- Name: question; Type: TABLE; Schema: public; Owner: shadyhu1
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text,
    username text,
    user_id integer
);


ALTER TABLE public.question OWNER TO shadyhu1;

--
-- TOC entry 196 (class 1259 OID 32999)
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: shadyhu1
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO shadyhu1;

--
-- TOC entry 3238 (class 0 OID 0)
-- Dependencies: 196
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shadyhu1
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- TOC entry 202 (class 1259 OID 33026)
-- Name: question_tag; Type: TABLE; Schema: public; Owner: shadyhu1
--

CREATE TABLE public.question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.question_tag OWNER TO shadyhu1;

--
-- TOC entry 204 (class 1259 OID 33031)
-- Name: tag; Type: TABLE; Schema: public; Owner: shadyhu1
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.tag OWNER TO shadyhu1;

--
-- TOC entry 203 (class 1259 OID 33029)
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: shadyhu1
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO shadyhu1;

--
-- TOC entry 3239 (class 0 OID 0)
-- Dependencies: 203
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shadyhu1
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- TOC entry 206 (class 1259 OID 33040)
-- Name: users; Type: TABLE; Schema: public; Owner: shadyhu1
--

CREATE TABLE public.users (
    id integer NOT NULL,
    user_name text,
    password text NOT NULL,
    email text,
    registration_time timestamp without time zone,
    reputation integer DEFAULT 0 NOT NULL
);


ALTER TABLE public.users OWNER TO shadyhu1;

--
-- TOC entry 205 (class 1259 OID 33038)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: shadyhu1
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO shadyhu1;

--
-- TOC entry 3240 (class 0 OID 0)
-- Dependencies: 205
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: shadyhu1
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3071 (class 2604 OID 33013)
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- TOC entry 3072 (class 2604 OID 33022)
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- TOC entry 3070 (class 2604 OID 33004)
-- Name: question id; Type: DEFAULT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- TOC entry 3073 (class 2604 OID 33034)
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- TOC entry 3074 (class 2604 OID 33043)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3223 (class 0 OID 33010)
-- Dependencies: 199
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: shadyhu1
--

COPY public.answer (id, submission_time, vote_number, question_id, message, image, username, user_id) FROM stdin;
1	2017-04-28 16:49:00	4	1	You need to use brackets: my_list = []	\N	admin	1
2	2017-04-25 14:42:00	35	1	Look it up in the Python docs	images/image2.jpg	admin	2
\.


--
-- TOC entry 3225 (class 0 OID 33019)
-- Dependencies: 201
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: shadyhu1
--

COPY public.comment (id, question_id, answer_id, message, submission_time, edited_count) FROM stdin;
1	0	\N	Please clarify the question as it is too vague!	2017-05-01 05:49:00	\N
2	\N	1	I think you could use my_list = list() as well.	2017-05-02 16:55:00	\N
\.


--
-- TOC entry 3221 (class 0 OID 33001)
-- Dependencies: 197
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: shadyhu1
--

COPY public.question (id, submission_time, view_number, vote_number, title, message, image, username, user_id) FROM stdin;
2	2017-05-01 10:41:00	1379	61	Drawing canvas with an image picked with Cordova Camera Plugin	I'm getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I'm on IOS, it throws errors such as cross origin issue, or that I'm trying to use an unknown format.\n	\N	admin	2
1	2017-04-29 09:19:00	19	9	Wordpress loading multiple jQuery Versions	I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();\n\nI could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.\n\nBUT in my theme i also using jquery via webpack so the loading order is now following:\n\njquery\nbooklet\napp.js (bundled file with webpack, including jquery)	images/image1.png	admin	1
6	2019-06-06 13:39:20	1	0	asdasdasdasdasdasdas	dasdasdasdasdasdasd		admin1	\N
0	2017-04-28 08:29:00	29	7	How to make lists in Python?	I am totally new to this, any hints?	\N	admin	0
\.


--
-- TOC entry 3226 (class 0 OID 33026)
-- Dependencies: 202
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: shadyhu1
--

COPY public.question_tag (question_id, tag_id) FROM stdin;
0	1
1	3
\.


--
-- TOC entry 3228 (class 0 OID 33031)
-- Dependencies: 204
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: shadyhu1
--

COPY public.tag (id, name) FROM stdin;
1	python
2	sql
3	css
\.


--
-- TOC entry 3230 (class 0 OID 33040)
-- Dependencies: 206
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: shadyhu1
--

COPY public.users (id, user_name, password, email, registration_time, reputation) FROM stdin;
0	admin	admin	admin@admin.com	2019-06-03 13:00:00	0
1	teszt	$2b$12$YDyd0EGt/cIDwTCUdpuOFunqSIC5wn8hfDoBaZty2CW68i2mvP936	asfdasfafasf@sdfsdf.com	2019-06-06 10:54:05	0
2	admin1	$2b$12$T9KyvWti3lB/ZhG62ORHrujTTWIOc5TYeJ1XbLbVquRSNWuHELKTO	yxcyxcyxc@sdfsdf.com	2019-06-06 11:23:10	21
\.


--
-- TOC entry 3241 (class 0 OID 0)
-- Dependencies: 198
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shadyhu1
--

SELECT pg_catalog.setval('public.answer_id_seq', 5, true);


--
-- TOC entry 3242 (class 0 OID 0)
-- Dependencies: 200
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shadyhu1
--

SELECT pg_catalog.setval('public.comment_id_seq', 2, true);


--
-- TOC entry 3243 (class 0 OID 0)
-- Dependencies: 196
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shadyhu1
--

SELECT pg_catalog.setval('public.question_id_seq', 6, true);


--
-- TOC entry 3244 (class 0 OID 0)
-- Dependencies: 203
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shadyhu1
--

SELECT pg_catalog.setval('public.tag_id_seq', 3, true);


--
-- TOC entry 3245 (class 0 OID 0)
-- Dependencies: 205
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: shadyhu1
--

SELECT pg_catalog.setval('public.users_id_seq', 2, true);


--
-- TOC entry 3079 (class 2606 OID 33052)
-- Name: answer pk_answer_id; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);


--
-- TOC entry 3081 (class 2606 OID 33054)
-- Name: comment pk_comment_id; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);


--
-- TOC entry 3077 (class 2606 OID 33056)
-- Name: question pk_question_id; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);


--
-- TOC entry 3083 (class 2606 OID 33058)
-- Name: question_tag pk_question_tag_id; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);


--
-- TOC entry 3085 (class 2606 OID 33060)
-- Name: tag pk_tag_id; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);


--
-- TOC entry 3087 (class 2606 OID 33062)
-- Name: users pk_users_id; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT pk_users_id PRIMARY KEY (id);


--
-- TOC entry 3089 (class 2606 OID 33050)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 3091 (class 2606 OID 33048)
-- Name: users users_user_name_key; Type: CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_user_name_key UNIQUE (user_name);


--
-- TOC entry 3095 (class 2606 OID 33063)
-- Name: comment fk_answer_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES public.answer(id) ON DELETE CASCADE;


--
-- TOC entry 3093 (class 2606 OID 33068)
-- Name: answer fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id) ON DELETE CASCADE;


--
-- TOC entry 3097 (class 2606 OID 33073)
-- Name: question_tag fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id) ON DELETE CASCADE;


--
-- TOC entry 3096 (class 2606 OID 33078)
-- Name: comment fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id) ON DELETE CASCADE;


--
-- TOC entry 3098 (class 2606 OID 33083)
-- Name: question_tag fk_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES public.tag(id) ON DELETE CASCADE;


--
-- TOC entry 3092 (class 2606 OID 33089)
-- Name: question user_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- TOC entry 3094 (class 2606 OID 33095)
-- Name: answer user_id; Type: FK CONSTRAINT; Schema: public; Owner: shadyhu1
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT user_id FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


-- Completed on 2019-06-06 13:51:18 CEST

--
-- PostgreSQL database dump complete
--

