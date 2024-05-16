# Export commit as patch
A patch is littrelly a commit-diff in textual form
so that it can be `applied` to a commit tree.

To generate a patch:
``` sh
git show $COMMIT_HASH > your_file.diff
```

