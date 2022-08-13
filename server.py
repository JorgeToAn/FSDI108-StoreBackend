from flask import Flask
import json
from data import me

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask"

@app.get("/test")
def test():
    return "Testing endpoint"

@app.get("/about")
def about():
    return "Jorge Tostado"

#--------------------------------------------------------#
#---------------------- API PRODUCTS --------------------#
#--------------------------------------------------------#

@app.get("/api/test")
def test_api():
    return json.dumps("OK")

# get /api/about return the me dictionary as json
@app.get("/api/about")
def about_api():
    return json.dumps(me)







# debug=True allows code to be loaded without needing to kill and restart the server
app.run(debug=True)