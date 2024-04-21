--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2 (Postgres.app)
-- Dumped by pg_dump version 16.2 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: appointment; Type: TABLE; Schema: public; Owner: juho
--

CREATE TABLE public.appointment (
    id integer NOT NULL,
    doctor_id integer,
    appointment_date date,
    appointment_time time without time zone,
    reserved boolean
);


ALTER TABLE public.appointment OWNER TO juho;

--
-- Name: appointment_id_seq; Type: SEQUENCE; Schema: public; Owner: juho
--

CREATE SEQUENCE public.appointment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.appointment_id_seq OWNER TO juho;

--
-- Name: appointment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: juho
--

ALTER SEQUENCE public.appointment_id_seq OWNED BY public.appointment.id;


--
-- Name: cities; Type: TABLE; Schema: public; Owner: juho
--

CREATE TABLE public.cities (
    id integer NOT NULL,
    city_name text
);


ALTER TABLE public.cities OWNER TO juho;

--
-- Name: cities_id_seq; Type: SEQUENCE; Schema: public; Owner: juho
--

CREATE SEQUENCE public.cities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.cities_id_seq OWNER TO juho;

--
-- Name: cities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: juho
--

ALTER SEQUENCE public.cities_id_seq OWNED BY public.cities.id;


--
-- Name: doctors; Type: TABLE; Schema: public; Owner: juho
--

CREATE TABLE public.doctors (
    id integer NOT NULL,
    doctor_name text,
    city_id integer
);


ALTER TABLE public.doctors OWNER TO juho;

--
-- Name: doctor_id_seq; Type: SEQUENCE; Schema: public; Owner: juho
--

CREATE SEQUENCE public.doctor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.doctor_id_seq OWNER TO juho;

--
-- Name: doctor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: juho
--

ALTER SEQUENCE public.doctor_id_seq OWNED BY public.doctors.id;


--
-- Name: doctor_specialization; Type: TABLE; Schema: public; Owner: juho
--

CREATE TABLE public.doctor_specialization (
    doctor_id integer NOT NULL,
    specialization_id integer NOT NULL
);


ALTER TABLE public.doctor_specialization OWNER TO juho;

--
-- Name: specialization; Type: TABLE; Schema: public; Owner: juho
--

CREATE TABLE public.specialization (
    id integer NOT NULL,
    specialization_name text
);


ALTER TABLE public.specialization OWNER TO juho;

--
-- Name: specialization_id_seq; Type: SEQUENCE; Schema: public; Owner: juho
--

CREATE SEQUENCE public.specialization_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.specialization_id_seq OWNER TO juho;

--
-- Name: specialization_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: juho
--

ALTER SEQUENCE public.specialization_id_seq OWNED BY public.specialization.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: juho
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text,
    password text
);


ALTER TABLE public.users OWNER TO juho;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: juho
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.users_id_seq OWNER TO juho;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: juho
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: appointment id; Type: DEFAULT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.appointment ALTER COLUMN id SET DEFAULT nextval('public.appointment_id_seq'::regclass);


--
-- Name: cities id; Type: DEFAULT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.cities ALTER COLUMN id SET DEFAULT nextval('public.cities_id_seq'::regclass);


--
-- Name: doctors id; Type: DEFAULT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.doctors ALTER COLUMN id SET DEFAULT nextval('public.doctor_id_seq'::regclass);


--
-- Name: specialization id; Type: DEFAULT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.specialization ALTER COLUMN id SET DEFAULT nextval('public.specialization_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: appointment appointment_pkey; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_pkey PRIMARY KEY (id);


--
-- Name: cities cities_pkey; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (id);


--
-- Name: doctors doctor_pkey; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctor_pkey PRIMARY KEY (id);


--
-- Name: doctor_specialization doctor_specialization_pkey; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.doctor_specialization
    ADD CONSTRAINT doctor_specialization_pkey PRIMARY KEY (doctor_id, specialization_id);


--
-- Name: specialization specialization_pkey; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.specialization
    ADD CONSTRAINT specialization_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: appointment appointment_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.appointment
    ADD CONSTRAINT appointment_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(id);


--
-- Name: doctors doctor_city_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctor_city_id_fkey FOREIGN KEY (city_id) REFERENCES public.cities(id);


--
-- Name: doctor_specialization doctor_specialization_doctor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.doctor_specialization
    ADD CONSTRAINT doctor_specialization_doctor_id_fkey FOREIGN KEY (doctor_id) REFERENCES public.doctors(id);


--
-- Name: doctor_specialization doctor_specialization_specialization_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: juho
--

ALTER TABLE ONLY public.doctor_specialization
    ADD CONSTRAINT doctor_specialization_specialization_id_fkey FOREIGN KEY (specialization_id) REFERENCES public.specialization(id);


--
-- PostgreSQL database dump complete
--

