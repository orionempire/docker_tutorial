docker-machine create --driver virtualbox myvm1
docker-machine ls
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100:2377"