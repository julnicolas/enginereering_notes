# Interactive rebase
``` sh
git rebase -i $from_commit_hash
```

Four actions are possible:
- `reword`: change commit name
- `drop`: remove commit from history
    (equivalently - suppress it from the listing)
- `fixup`: meld commit into previous commit, keeping
    the previous commit message
- `squash`: meld commit into previous, leaving the user
    pick what commit name to keep

Finally, it is possible to rearange commit order, simply
by modifying the order in the displayed listing.

