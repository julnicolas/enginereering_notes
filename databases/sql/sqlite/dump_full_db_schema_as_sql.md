# Dump full DB schema to raw SQL Data Definition Language
This dumps a whole DB as `create..., drop table` sql instructions.

``` sh
sqlite3 "$PATH_TO_DB" -- '.fullschema' > schema.sql
```

Note - I developped a tool to show tables and foreign key dependencies from
raw sql.

