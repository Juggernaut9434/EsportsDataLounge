USERNAME=$(whoami)
DATABASE="esports"

psql -c "CREATE DATABASE $DATABASE with owner=$USERNAME"
psql $DATABASE -a -f ./create_tables.sql

psql $DATABASE -c "\\copy esportsearnings from 'esportsdata.csv' DELIMITER ',' CSV HEADER QUOTE '\"' NULL '\\N' ESCAPE ';'"
