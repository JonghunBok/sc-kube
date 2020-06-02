docker build -f dockerfile_server --tag jonghunbok/dummy-game:server .
docker build -f dockerfile_client --tag jonghunbok/dummy-game:client .

docker push jonghunbok/dummy-game:server
docker push jonghunbok/dummy-game:client

