# Docker Commands


## Common Commands

docker pull
docker images
docker ps
docker ps -a
docker run -d -p3000:6794
docker run -p3000:6794
docker start [id_of_instance]
docker stop [id_of_instance]
docker logs
docker run -d -p6001:6379 --name redis-older redis
docker exec -it [container_id] /bin/bash

env

#  LocalWords:  ps

docker-compose -f mongo.yaml up >> docker_compose_log2.txt



* MongoDB
** Start mongodb
#+begin_src bash
docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
--net mongo-network \
mongo \

#+end_src bash


** Start mongodb-express
#+begin_src bash
docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
--net mongo-network \
--name mongo-express \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
mongo-express
#+end_src bash
