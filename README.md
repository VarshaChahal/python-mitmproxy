# python-mitmproxy
How to use:

Install requirements
```
  pip install -r requirements.txt
```
Run mitm proxy:
```
  py ./start_mitm.py
```
Shut the proxy down:
```
  py ./shutdown_mitm.py
```
You can also use curl to shut the proxy down:
```
  curl -H "shutdown: shutdown" localhost:8085
```
