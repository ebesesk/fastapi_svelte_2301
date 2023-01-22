'''
node-js 인스톨
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
node-js 언인스톨
sudo apt-get purge nodejs &&\
sudo rm -r /etc/apt/sources.list.d/nodesource.list

python3 -m venv .venv
source .venv/bin/activate
deactivate
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirement.txt

npm create vite@latest frontend -- --template svelte
cd frontend
npm install

vscode svelte for vscode 설치

스벨트는 자바스크립트의 타입을 체크하는 것이 디폴트로 설정되어 있다. 
하지만 파이보 프로젝트는 타입스크립트를 사용하지 않기 때문에 해당 설정을 끄고 진행
vscode .venv/frontend/jsconfig.json

{
  "compilerOptions": {
    (... 생략 ...)
    /**
     * Typecheck JS in `.svelte` and `.js` files by default.
     * Disable this if you'd like to use dynamic types.
     */
    "checkJs": false
  },
  (... 생략 ...)
}

frontend % npm run dev


nginx svelte 설정
server {
        listen 7080 default_server;
        listen [::]:7080 default_server;
        server_name svelte2301.ebesesk.synology.me;

        location / {
                include proxy_params;
                limit_except GET POST {
                        deny all;
                }
                proxy_pass http://localhost:5173;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection upgrade;
                proxy_set_header Host $host;
                proxy_set_header Accept-Encoding gzip;
                proxy_set_header X-Forwarded-Proto $scheme;
        }
}



if ps ax | grep -v grep | grep nginx > /dev/null                                                       
then                                                                                                   
        echo "nginx service running"                                                                   
else                                                                                                   
        echo "kds11918" | sudo -S service nginx start                                                                            
fi 

'''
##alembic 설치 db 생성
설치후
alembic init migrations

/ 하위에 migrations 라는 디렉토리와 alembic.ini 파일이 생성된다.
migrations 디렉토리는 alembic 도구를 사용할 때 생성되는 리비전 파일들을
저장하는 용도로 사용되고 alembic.ini파일은 alembic 환경파일 설정이다.

alembic을 이용하여 테이블을 생성 또는 변경할 때마다 파일이 생성되는데 
이 작업 파일을 리비전 파일이라고 한다. 그리고 이리비전 파일은 
migrations 디렉토리에 저장된다

/alembic.ini 수정

sqlalchemy.url = sqlite:///./myapi.db

/migrations/env.py 수정

import models
target_metadata = models.Base.metadata

alembic revision --autogenerate 실행
alembic upgrade head
