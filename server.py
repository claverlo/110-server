
#flask (small f) → the Flask library / package  Flask (big F) → the Flask class (tool) inside the library
# 1. “Python, go inside the flask library and bring me three tools so I can use them in this file.” 1. Flask 2.jsonfy 3. and request 


from flask import Flask, jsonify, request

# You put `from http import HTTPStatus` so you can use readable names like `HTTPStatus.OK` instead of numbers like `200` for HTTP response codes.
from http import HTTPStatus 

#“Use the Flask tool to create the web application (the server).A server is a program that waits for requests and sends back responses.
#For example, the browser asks http://127.0.0.1:5000/hello
#, the server receives it, and the server sends back "this is the hello path...".
app = Flask(__name__) # Instance of Flask/ without it this would should images= no app = Flask(__name__).png




# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])   # 1️ Route = "/"   | 2️ Method = GET
def index():                       # 3️ Function = index()
    return "Welcome to Flask Framework Cohort#64 !!!"  # 4️ Response


# http://127.0.0.1:5000/whatup
@app.route("/whatup", methods=["GET"])
def whatup():
    return "this is the what up path..."


# http://127.0.0.1:5000/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "this is the hello path..."


# http://127.0.0.1:5000/cohort-64
@app.route("/cohort-64", methods=["GET"])   # 1️ Route = "/cohort-64" | 2️ Method = GET
def get_students_64():                      # 3️ Function = get_students_64()
    student_list = ["leomar", "ronald", "pam", "angela"]
    return student_list                     # 4️ Response = the student list


# http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods=["GET"])
def students():
    students_list = ["michael", "dwigth", "jenn", "stephanie"]
    return students_list


# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])   # 1️ Route = "/contact" | 2️ Method = GET
def get_contact_information():            # 3️ Function = get_contact_information()
    contact_information = {
    "email": "lmiranda@sdgku.edu",
    "phone": "619 123 45 67"
    }
    return contact_information            # 4️ Response = contact information


# GET http://127.0.0.1:5000/course-information
@app.route("/course-information", methods=["GET"])
def get_course_information():
    course_info = {
    "title": "Python",
    "duration": "4 sessions",
    "level": "Very hard"    
    }

    return course_info


# Minichallenge
# Create a /user endpoint
# Return a dictionary with: name, role, is_active and favorite_technologies
# Test it by visiting <GET> http://127.0.0.1:5000/user
@app.route("/user", methods=["GET"])
def get_user():
    user_information = {
    "name": "Leo",
    "role": "Tutor",
    "is_active": True,
    "favorite_technologies": ["Vue.js", "Flask", "Django", "FastAPI"]
    }
    return user_information


# ---- PATH PARAMETERS ----


#<string:name> is basically a placeholder.
@app.route('/greet/<string:name>', methods=["GET"])   # 1️ Route = /greet/<string:name> | 2️ Method = GET
def greet(name):                                      # 3️ Function = greet()
    return {"message": f"hello {name}"}, HTTPStatus.OK # 4️ Response = message + status code 200


@app.route('/api/users/<int:user_id>', methods=["GET"])
def get_user_by_id(user_id):
    return jsonify({"user_id": user_id}), HTTPStatus.OK # 200


# ------------ PRODUCTS ------------
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
},{
    "_id": 3, 
    "title": "Bluetooth Speaker", 
    "price": 79.99, 
    "category": "Electronics", 
    "image": "https://picsum.photos/seed/3/300/300"
},
]

# GET http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["GET"])   # 1️ Route = /api/products | 2️ Method = GET
def get_products():                            # 3️ Function = get_products()
    return jsonify({"data": products}), HTTPStatus.OK  # 4️ Response = JSON data + status code 200



# POST http://127.0.0.1:5000/api/products   # 1️ Method = POST | Route = /api/products
@app.route("/api/products", methods=["POST"])  # Route + Method
def create_product():                          # 2️ Function
    print(request.get_json())                  # 3️ Read client data (JSON sent by client)
    new_product = request.get_json()           # 4️ Store the JSON data in a variable
    new_product["_id"] = len(products) + 1     # 5️ Create a new ID for the product
    products.append(new_product)               # 6️ Save the product to the products list
    return jsonify({                           # 7️ Response (send JSON back to client)
        "success": True, 
        "message": "Product successfully created",
        "data": new_product
    }), HTTPStatus.CREATED                     # 8️ Status Code = 201 (created)



# PUT - update a product by Id
@app.route("/api/products/<int:product_id>", methods=["PUT"])   # 1️ Route = /api/products/<id> | Method = PUT
def update_product_by_id(product_id):                           # 2️ Function
    updated_product = request.get_json()                        # 3️ Read client JSON data
    for product in products:                                    # 4️ Loop through products
        if product["_id"] == product_id:                        # 5️ Check if ID matches
            product["title"] = updated_product["title"]         # 6️ Update title
            product["price"] = updated_product["price"]         # 6️ Update price
            product["category"] = updated_product["category"]   # 6️ Update category
            product["image"] = updated_product["image"]         # 6️ Update image
            return jsonify({                                    # 7️ Response (success)
                "success": True,
                "message": "Product Updated Successfully"
            }), HTTPStatus.OK  # 200                            # 8️ Status Code
    return jsonify({                                            # 9️ Response if not found
        "success": False,
        "message": "Product Not Updated"
    }), HTTPStatus.NOT_FOUND  # 404                             # 10 Status Code




# DELETE -- delete a product by id
# DELETE http://127.0.0.1:5000/api/products/<int:product_id>

@app.route("/api/products/<int:product_id>", methods=["DELETE"])   # 1️ Route | Method = DELETE
def delete_product_by_id(product_id):                              # 2️ Function
    for product in products:                                       # 3️ Loop through products
        if product["_id"] == product_id:                           # 4️ Check if ID matches
            products.remove(product)                               # 5️ Delete product
            return jsonify({                                       # 6️ Response
                "success": True,
                "message": "Product deleted successfully"
            }), HTTPStatus.OK  # 200                               # 7️ Status Code
    return jsonify({                                               # 8️ Response if not found
        "success": False,
        "message": "product Not Found"
    }), HTTPStatus.NOT_FOUND  # 404                                # 9️ Status Code

# ------------ COUPONS ------------
coupons = [
{"_id": 1, "code": "WELCOME10", "discount": 10},
{"_id": 2, "code": "SPOOKY25", "discount": 25},
{"_id": 3, "code": "VIP50", "discount": 50}
]

# GET /api/coupons endpoint that returns a list of coupons.
# http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons


# GET /api/coupons/count returns the number of coupons in the system.
# http://127.0.0.1:5000/api/coupons/count
# GET /api/coupons/count returns the number of coupons in the system.
# http://127.0.0.1:5000/api/coupons/count

@app.route("/api/coupons/count", methods=["GET"])   # 1️ Route = /api/coupons/count | Method = GET
def get_coupons_count():                            # 2️ Function
    return {"count": len(coupons)}                  # 3️ Response (returns number of coupons)


# POST /api/coupons endpoint that adds a new coupon in coupons list.
# http://127.0.0.1:5000/api/coupons

@app.route("/api/coupons", methods=["POST"])   # 1️ Route = /api/coupons | Method = POST
def create_coupon():                           # 2️ Function
    new_coupon = request.get_json()            # 3️ Read client JSON data
    new_coupon["_id"] = len(coupons) + 1       # 4️ Create coupon ID
    coupons.append(new_coupon)                 # 5️ Save coupon to coupons list
    return jsonify({                           # 6️ Response
        "success": True,
        "message": "Coupon successfully created",
        "data": new_coupon
    }), HTTPStatus.CREATED  # 201              # 7️ Status Code



# GET /api/coupons/<int:id> endpoint that returns a coupon that matches the given id.
# http://127.0.0.1:5000/api/coupons/2

@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])   # 1️ Route = /api/coupons/<id> | Method = GET
def get_coupon_by_id(coupon_id):                              # 2️ Function
    for coupon in coupons:                                    # 3️ Loop through coupons
        if coupon["_id"] == coupon_id:                        # 4️ Check if ID matches
            return jsonify({                                  # 5️ Response (success)
                "success": True,
                "message": "Coupon retrieved",
                "data": coupon
            }), HTTPStatus.OK  # 200                          # 6️ Status Code
    return jsonify({                                          # 7️ Response if not found
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND  # 404                           # 8️ Status Code



    #  Final Report 
#Put /api/coupons/<int:id>   endpoint that allows editing an existing coupon by its id.
#if the coupon is not found, return an appropriate error message and status code.

# http://127.0.0.1:5000/api/coupons/1

@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])   # 1️ Route = /api/coupons/<id> | Method = PUT
def update_coupon_by_id(coupon_id):                           # 2️ Function
    updated_coupon = request.get_json()                       # 3️ Read client JSON data
    for coupon in coupons:                                    # 4️ Loop through coupons
        if coupon["_id"] == coupon_id:                        # 5️ Check if ID matches
            coupon["code"] = updated_coupon["code"]           # 6️ Update code
            coupon["discount"] = updated_coupon["discount"]   # 6️ Update discount
            return jsonify({                                  # 7️ Response (success)
                "success": True,
                "message": "Coupon updated successfully",
                "data": coupon
            }), HTTPStatus.OK  # 200                          # 8️ Status Code
    return jsonify({                                          # 9️ Response if not found
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND  # 404                           # 10 Status Code


#Delete /api/coupons/<int:id>  endpoint that allows deleting an existing coupon by its id.
#if the coupon is not found, return an appropriate error message and status code.

# http://127.0.0.1:5000/api/coupons/1

@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])   # 1️ Route = /api/coupons/<id> | Method = DELETE
def delete_coupon_by_id(coupon_id):                              # 2️ Function

    for coupon in coupons:                                       # 3️ Loop through coupons
        if coupon["_id"] == coupon_id:                           # 4️ Check if ID matches
            coupons.remove(coupon)                               # 5️ Delete coupon from list
            return jsonify({                                     # 6️ Response (success)
                "success": True,
                "message": "Coupon deleted successfully"
            }), HTTPStatus.OK  # 200                             # 7️ Status Code
    return jsonify({                                             # 8️ Response if not found
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND  # 404                              # 9️ Status Code



if __name__ == "__main__":   # 1️ Check if this file is run directly
    app.run(debug=True)     # 2️ Start the Flask server

# When this file is run directly: __name__ == "__main__"   # 3️⃣ Python runs the server
# When this file is imported as module: __name__ == "server.py"   # 4️⃣ Server does NOT start automatically