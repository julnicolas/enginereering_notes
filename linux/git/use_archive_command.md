# Use Archive Command
The archive command is similar to `git clone` in the sense that it fetches
a repository and all its history from a specific commit hash.

The major difference though is that the `.git` folder will not be downloaded.
Meaning it won't be possible to contribute to the repository from an archive.

``` sh
git archive --format=tar --remote=$REPO $HASH > $OUTPUT_FILE
```

`$HASH` can also be a tag or a branch name as with `git checkout`.
