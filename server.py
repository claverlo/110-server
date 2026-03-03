from flask import Flask

app = Flask(__name__)  # Instance of Flask

# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework Cohort#64 !!!"

# http://127.0.0.1:5000/cohort-99     get students cohort 99
@app.route("/cohort-99", methods=["GET"])
def students():
    students_list = ["michael", "dwight", "jenn", "stephanie"]
    return students_list

# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def get_contact_information():
    contact_information = {
        "email": "lmiranda@sdgku.edu",
        "phone": "619 123 45 67"
    }
    return contact_information

#-----------Products-------------------
products = [

{

    "_id": 1, 

    "title": "Nintendo Switch", 

    "price": 499.99, 

    "category": "Electronics", 

    "image": "https://picsum.photos/seed/1/300/300"

  },

  {

    "_id": 2, 

    "title": "Smart Refrigerator", 

    "price": 999.99, 

    "category": "Kitchen", 

    "image": "https://picsum.photos/seed/2/300/300"

  },

  {

    "_id": 3, 

    "title": "Bluetooth Speaker", 

    "price": 79.99, 

    "category": "Electronics", 

    "image": "https://picsum.photos/seed/3/300/300"

  },

]

# GET http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])
def get_products():
    return {"data": products}


# ------------ COUPONS ------------

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]


@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons
# http://127.0.0.1:5000/api/coupons


@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return {"count": len(coupons)}

#http://127.0.0.1:5000/api/coupons/count





@app.route("/hello", methods=["GET"])
def hello():
    return "Welcome to Flask"

if __name__ == "__main__":
    app.run(debug=True)

# When this file is run directly: __name__ == "__main__"
# When this file is imported as a module: __name__ == "server"

