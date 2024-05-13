# Show reflog
The reflog contains a log of all previous
operations changing the commit tree (commit, rebase, merge...).
It only contains local operations.

It is a great last resort tool in case of disaster recovery.

``` sh
git reflog
```

or equivalent:

``` sh
git reflog show
```

