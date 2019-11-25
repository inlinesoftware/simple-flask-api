# simple-flask-api
simple flask api 

## Installation

### Requirements:

   - Python 2.7+ or 3.4+
   - Flask 0.12.3+
   - Mysql Connector

```pip install Flask-API```

```pip install mysql-connector```

### Starting
```python app.py```

## script_conf.json

Should create the file ```script_conf.json``` no diretório ```/config``` with the ```bot_id``` and the ```chat_id``` from the telegram, to broadcast some msg when the methods configured for.

```json
{
    "script-conf":{
        "telegram":{
            "bot_id"       : "bot_id", 
            "chat_id"      : "chat_id"
         }
    }
}
```

### CURL example to POST request  for directly message broadcast to telegram
```curl -i -H "Content-Type: application/json" -X POST -d '{"bot":"bot_id", "chat_id":"chat_id", "msg":"Message here..."}' http://localhost:5000/broadcast```
