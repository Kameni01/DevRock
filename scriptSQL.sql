CREATE USER admin password admin WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION; GRANT postgres TO admin;
ALTER USER admin PASSWORD 'admin';
ALTER USER admin WITH PASSWORD 'admin';

CREATE DATABASE devrock WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default CONNECTION LIMIT = -1;
