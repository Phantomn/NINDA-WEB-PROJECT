# NIMDA Web Project
NIMDA Web Project

Apache - django+Python - MySQL
----------------------------------------------------
<파이썬 3.6 설치>
sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update

sudo apt-get install python3.6

sudo apt-get install libmysqlclient-dev 

sudo apt-get install python3.6-dev

pip install mysqlclient

<가상환경 및 프로젝트 구축>
----------------------------------------------------
mkdir project

cd project

virtualenv -p python3.6 venv

. venv/bin/activate

git clone http://mroom.iptime.org:10003/blackguest/mroom.git

cd mroom

pip install -r requirements.txt
