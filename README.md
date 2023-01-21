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

cd .venv
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
