# Return a value from a json file
Let us say foo.json contains:
``` json
{
    "field1": "hello",
}
```

Then the following:
``` sh
cat foo.json | jq '.field1'
```
Returns `"hello"`.

