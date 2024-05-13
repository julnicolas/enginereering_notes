# Push force with lease
Needed in case of a rebase. The lease
option is safer that a force when changes
occur concurently. However I do not remember
the specifics.

Any ways, it is better to rebase on a work branch
of your own to avoid problems.

``` sh
git push --force-with-lease
```

