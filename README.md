# vontor-cz

## venv
- windows

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate

#start server
daphne -b 0.0.0.0 -p 8000 vontor_cz.asgi:application
```




## docker compose
 spuštění dockeru pro lokální hosting, s instantníma změnami během editace ve vscodu.
 ```docker-compose up --build```
