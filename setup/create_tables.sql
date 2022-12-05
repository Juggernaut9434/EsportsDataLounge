-- DROP TABLE IF EXISTS public."esportsearnings";

CREATE TABLE IF NOT EXISTS public."esportsearnings"
(
    "Game" character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "ReleaseDate" integer,
    "Genre" character varying(50) COLLATE pg_catalog."default",
    "TotalEarnings" money,
    "OnlineEarnings" money,
    "TotalPlayers" integer,
    "TotalTournaments" integer,
    CONSTRAINT "EsportsEarnings_pkey" PRIMARY KEY ("Game")
)

TABLESPACE pg_default;

--ALTER TABLE IF EXISTS public."esportsearnings"
--    OWNER to mike;
