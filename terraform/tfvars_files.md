# Tfvars files
These files contain sensitive values such as tokens.
They are meant to be ignored by your VCS.

They are a list of key values. Here are a few examples:
```
token = "64-character-long-token"
foo = "sensitive foo value"
...
```

Note: values contained in tfvars can also be provided
as CLI arguments.

