# Initialize Host
Install Virtual box
docker rm $(docker ps -a -q)           # Remove all containers from this machine
docker rmi $(docker images -q)             # Remove all images from this machine

# Tutorial 02
docker build -t friendlyhello .
docker run -d -p 4000:80 friendlyhello
curl http://localhost:4000
docker stop <CONTAINER ID>

# Tutorial 03
docker swarm init
docker stack deploy -c docker-compose.yml getstartedlab
docker stack ps getstartedlab
curl http://localhost
docker stack rm getstartedlab
docker swarm leave --force

# Tutorial 04
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2
docker-machine ls
docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 IP:2377>"
docker-machine ssh myvm1 "docker swarm join-token"
docker-machine ssh myvm2 "docker swarm join --token SWMTKN-1-2gx5bjdq5f2884ck4tfx2z17t7822auba7byf1bquud96kmv35-73f4fyy2u2h7dw6rfiyfnpcfl 192.168.99.100:2377"
docker-machine ssh myvm1 "docker node ls"
docker-machine scp docker-compose.yml myvm1:~
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"
docker-machine ssh myvm1
docker stack deploy -c docker-compose.yml getstartedlab
exit
docker-machine ssh myvm1 "docker stack rm getstartedlab"

# Tutorial 05
docker-machine scp docker-compose.yml myvm1:~
docker-machine ls
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"
http://<myvm1 IP:8080>/
