docker run -d \
   --rm \
   --hostname rabbit-z620 \
   --name rabbit-z620 \
   -p 15672:15672  \
   -p 5672:5672  \
   -p 1883:1883  \
   -e RABBITMQ_DEFAULT_USER=user \
   -e RABBITMQ_DEFAULT_PASS=password \
   -v $(pwd)/enabled_plugins:/etc/rabbitmq/enabled_plugins  \
   rabbitmq:3-management
