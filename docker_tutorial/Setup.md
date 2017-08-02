# Initialize Host
docker rm $(docker ps -a -q)           # Remove all containers from this machine
docker rmi $(docker images -q)             # Remove all images from this machine

# Tutorial 01
docker build -t friendlyhello .
docker run -d -p 4000:80 friendlyhello
curl http://localhost:4000
docker stop <CONTAINER ID>
