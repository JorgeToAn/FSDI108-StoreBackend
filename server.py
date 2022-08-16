from flask import Flask
import json
from data import me
from data import catalog

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

@app.get("/api/catalog")
def get_catalog():
    # return list of products
    return json.dumps(catalog)

@app.get("/api/product/<id>")
def get_product_by_id(id):
    product = "Product not found"
    for item in catalog:
        if(id == item["_id"]):
            product = item
            break
    
    return json.dumps(product)

@app.get("/api/products/<category>")
def get_products_by_category(category):
    products = []
    for item in catalog:
        if(category.lower() == item["category"].lower()):
            products.append(item)

    return json.dumps(products)

@app.get("/api/count")
def get_catalog_count():
    # returns the number of items in the catalog
    count = len(catalog)
    return json.dumps(count)

@app.get("/api/catalog/total")
def get_catalog_total():
    total = 0
    for item in catalog:
        total += item["price"]
    
    return json.dumps(total)

@app.get("/api/catalog/cheapest")
def get_cheapest():
    cheapest = catalog[0]
    for item in catalog:
        if(item["price"] < cheapest["price"]):
            cheapest = item

    return json.dumps(cheapest)






# debug=True allows code to be loaded without needing to kill and restart the server
# app.run(debug=True)