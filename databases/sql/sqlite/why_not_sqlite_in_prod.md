# Why not using sqlite in prod
Limited support of `ALTER table`:
- alter constraint is not supported, migration clients
  need to implement a copy and move strategy

By default, foreign key constraints are not supported.
To do so, each connection must connect with a `pragma strict
table argument`.

