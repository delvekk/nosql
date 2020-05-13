#!/bin/sh

docker network create --subnet=10.100.100.0/24 cluster
wait $!
docker-compose -f lab1.yml up -d
wait $!
echo "WAITING FOR MARIADB..."
sleep 30s

docker exec -it mariadb bash -c "mysql -u root -proot -e 'source /DATA/lab1.sql'"
wait $!

docker exec -it python bash -c "virtualenv --no-site-packages --python=python3 PY3"
wait $!

docker exec -it python bash -c "cd PY3/; source bin/activate; pip install pymongo; pip install mysql-connector; python lab1.py"
wait $!

docker-compose -f lab1.yml down
wait $!
docker network rm cluster
wait $!