#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE example_db;
	GRANT ALL PRIVILEGES ON DATABASE example_db TO postgres;
EOSQL
