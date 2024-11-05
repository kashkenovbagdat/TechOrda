docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline

docker ps

docker stop jsn-dkr-run

docker ps -a

chmod +x tester-docker-run.sh
./tester-docker-run.sh
