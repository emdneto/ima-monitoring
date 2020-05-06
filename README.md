# IMA-Monitoring 


## Running virtualenv for development
```
$ pip3 install virtualenv
$ virtualenv .venvs/ima
$ source .venvs/ima/bin/activate
```

```shell
$ (ima) pip install -r requirements.txt
```

## Running rabbitmq 

```shell
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

## Running IMA-Monitoring (Controller)
```shell
$ (ima) python3 main.py
```