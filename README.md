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

<Mysql 초기세팅>
----------------------------------------------------
sudo apt-cache policy mysql-server # Linux Repo에 저장되어있는 버전 확인

sudo apt-get purge mysql*
sudo apt-get autoremove
sudo apt-get autoclean
sudo apt-get dist-upgrade # 완전히 지우고 재설치

grant all privileges on 디비.* to root@'%' identified by '비번' with grant option;
flush privileges;         # 해당DB에root추가('%')

grant all privileges on 디비.* to 아이디@'%' identified by '비번' with grant option;
flush privileges;         # 해당DB에ID추가('%')

select host, user from mysql.user; # 계정권한보기

root는 host가 %로만들어지면 보안상 매우 취약해진다. 외부에서 접근이 가능해지기 때문이다

그렇기때문에 root는 localhost로만 넣어두고 다른계정으로 조작을하는것

<django 초기셋팅>
----------------------------------------------------
settings.py에서 

name -> DB명

user -> hostid

password -> 설정한것

django는 project밑에 여러개의 application으로 이루어진다.

ex>
mroom (프로젝트)
- mroom (어플)
- happy (어플)
- share (어플)

mroom (어플)로 이동해서 urls.py 수정.

초반에 IP:PORT로 접속을하면

path('', views.index, name='index') 로직을 타게 된다.

from . import views 현재 urls.py가 있는 디렉토리 위치에서 views.py로 연결

urls.py 소스에서

path('', views.index, name='index'),

#IP:PORT/ 주소로 들어오면 views.py에 def index함수를 실행시켜라 라는 뜻.

이후 파이썬 코드가 실행되고 연산된 값만 html로 던져주는데

return render(request, 'mroom/index.html', context)

'mroom/index.html' 그래서 이부분 연산을 python으로 짜고 결과값만 html에다가 던져주면 표시 할 수 있게된다. 그래서 django가 쉽다라는 것이다.

우선 urls -> views -> html 을 만들고

여기까지 하면

urls -> views -> html -> css, js 까지 오면 끝이난다.

DB처리는 views.py에서 전부 처리한다

urls

views <-> DB

html

<참고자료>
---------
http://luckyyowu.tistory.com/184

https://tutorial.djangogirls.org/ko/django_models/
