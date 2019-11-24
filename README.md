# simple-flask-api
simple flask api 

## Installation

### Requirements:

   - Python 2.7+ or 3.4+
   - Flask 0.12.3+

```pip install Flask-API```

### Starting
```python app.py```

### CURL example to POST request
```curl -i -H "Content-Type: application/json" -X POST -d '{"bot":"bot_id", "chat_id":"chat_id", "msg":"Message here..."}' http://localhost:5000/broadcast```
