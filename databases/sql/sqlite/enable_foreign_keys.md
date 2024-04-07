# Enabled Foreign Keys Per Connection
By default foreign key constraints are disabled. Also,
because of legacy considerations, such constraints must
be enabled on a per connection basis (file format cannot
tell if foreign key constraints are enabled).

To enable them, issue the following sqlite command:
```
PRAGMA foreign_keys = ON;
```

