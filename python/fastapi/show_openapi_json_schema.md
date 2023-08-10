# Show OpenAPI JSON schema

An OpenAPI schema defines all the endpoints exposed by an API along with
all required or optional values and return values and codes.

OpenAPI are defined in `json` following the `JSON format` standard.

Here is how to show one's API schema, considering default settings
(host == localhost and port == 8000):
```
http://localhost:8000/openapi.json
```

Note - OpenAPI is a standard to define API schemas. OpenAPI originated
from swagger works that's why several tools such as swagger UI are well
suited to interact with OpenAPI schemas.

Note - Json Schema is a standard on how to validate json data structures
       by defining a json file with a certain set of reserved words to
       describe such data structures (name of attributes, their types,
       are they mandatory, optional...)

