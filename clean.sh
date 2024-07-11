docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

docker network rm traffic_monitor_default