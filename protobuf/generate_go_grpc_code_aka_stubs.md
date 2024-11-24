# Generate GO GRPC Stubs

This generates go grpc stubs:

``` sh
protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    helloworld/helloworld.proto
```

It uses the protobuf file located in `helloworld` and called
`helloworld.proto`.

The `--go-out` generates code to serialize request and response
messages. They need to be serialised as they are sent over the
network in binary format.

The `--go-grpc_out` generates the code to query a grpc server
or serve a grpc query. It uses the generated code for the serialisation.

