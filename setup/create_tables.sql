-- DROP TABLE IF EXISTS public."esportsearnings";

CREATE TABLE IF NOT EXISTS public."esportsearnings"
(
    "game" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "releasedate" integer,
    "genre" character varying(50) COLLATE pg_catalog."default",
    "totalearnings" money,
    "onlineearnings" money,
    "totalplayers" integer,
    "totaltournaments" integer,
    CONSTRAINT "esportsearnings_pkey" PRIMARY KEY ("game")
)

TABLESPACE pg_default;

--ALTER TABLE IF EXISTS public."esportsearnings"
--    OWNER to mike;

-- NOTE: CREATE VIEWS

CREATE OR REPLACE VIEW "group_genre" AS
SELECT SUM(totalearnings) earnings, SUM(totalplayers) players, 
    SUM(totaltournaments) tournaments, genre 
FROM esportsearnings 
GROUP BY genre;
