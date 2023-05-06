BEGIN;
--
-- Create model Persona
--
CREATE TABLE "persona_persona" ("page_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES "wagtailcore_page" ("id") DEFERRABLE INITIALLY DEFERRED, "nombre" varchar(100) NOT NULL, "apellidos" varchar(100) NOT NULL, "fecha_nacimiento" date NOT NULL, "lugar_nacimiento" varchar(100) NOT NULL, "biografia" text NOT NULL, "foto" varchar(100) NOT NULL, "twitter" varchar(200) NOT NULL, "facebook" varchar(200) NOT NULL, "instagram" varchar(200) NOT NULL, "linkedin" varchar(200) NOT NULL, "body" text NOT NULL, "into" text NOT NULL);
COMMIT;
