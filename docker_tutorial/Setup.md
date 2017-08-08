#https://docs.docker.com/get-started/
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
docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 IP>:2377"
docker-machine ssh myvm1 "docker swarm join-token"
docker-machine ssh myvm2 "<docker swarm join-token>"
docker-machine ssh myvm1 "docker node ls"
docker-machine scp docker-compose.yml myvm1:~
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"
docker-machine ssh myvm1
docker stack deploy -c docker-compose.yml getstartedlab
exit
docker-machine ssh myvm1 "docker stack rm getstartedlab"

# Tutorial 05
docker-machine ssh myvm1 "mkdir ./data"
docker-machine scp docker-compose.yml myvm1:~
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"
docker-machine ls
http://<myvm1 IP>:8080/

# Full Stack Init (1 by 1)
docker-machine create --driver virtualbox myvm1
docker-machine create --driver virtualbox myvm2
docker-machine ls
#docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 IP>:2377"
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100:2377"
docker-machine ssh myvm1 "docker swarm join-token"
#docker-machine ssh myvm2 "<docker swarm join-token>"
docker-machine ssh myvm2 ""

# Full Stack 
docker-machine ssh myvm1 "mkdir ./data"
docker build -t friendlyhello .
rm /tmp/friendlyhello.img
docker save -o /tmp/friendlyhello.img friendlyhello
docker-machine scp /tmp/friendlyhello.img myvm1:~
docker-machine scp docker-compose.yml myvm1:~
docker-machine ssh myvm1 "docker load -i friendlyhello.img"
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"
#http://<myvm1 IP>:8080/
http://192.168.99.100:8080/
#http://<myvm1 IP>/
http://192.168.99.100/
http://192.168.99.101/
docker-machine ssh myvm1 "docker stack ps getstartedlab"

# Cleanup (1 by 1)
docker-machine ls -q
docker-machine stop $(docker-machine ls -q)               # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images
docker rm $(docker ps -a -q)           # Remove all containers from this machine
docker rmi $(docker images -q)             # Remove all images from this machine



# Useful Diagnostics
docker exec -i -t <ID> /bin/bash
