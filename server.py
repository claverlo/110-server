from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__) # Instance of Flask


# http://127.0.0.1:5000/
@app.route("/", methods=["GET"])
def index():
    return "Welcome to Flask Framework Cohort#64 !!!"


# http://127.0.0.1:5000/hello
@app.route("/hello", methods=["GET"])
def hello():
    return "this is the hello path..."


# http://127.0.0.1:5000/cohort-64
@app.route("/cohort-64", methods=["GET"])
def get_students_64():
    student_list = ["leomar", "ronald", "pam", "angela"]
    return student_list


# http://127.0.0.1:5000/cohort-99
@app.route("/cohort-99", methods=["GET"])
def students():
    students_list = ["michael", "dwigth", "jenn", "stephanie"]
    return students_list


# http://127.0.0.1:5000/contact
@app.route("/contact", methods=["GET"])
def get_contact_information():
    contact_information = {
      "email": "lmiranda@sdgku.edu",
      "phone": "619 123 45 67"
    }
    return contact_information


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

@app.route('/greet/<string:name>', methods=["GET"])
def greet(name):
    return {"message": f"hello {name}"}, HTTPStatus.OK # 200


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
    return jsonify({"data": products}), HTTPStatus.OK # 200


# POST http://127.0.0.1:5000/api/products
@app.route("/api/products", methods=["POST"])
def create_product():
    print(request.get_json())
    new_product = request.get_json()
    new_product["_id"] = len(products) + 1
    products.append(new_product)
    return jsonify({
        "success": True, 
        "message": "Product successfully created",
        "data": new_product
    }), HTTPStatus.CREATED # 201


# GET http://127.0.0.1:5000/api/products/3
@app.route("/api/products/<int:product_id>")
def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
              "success": True,
              "message": "Product retrieved successfully",
              "data": product    
            }), HTTPStatus.OK # 200
        
    return jsonify({
      "success": False,
      "message": "Product not found"    
    }), HTTPStatus.NOT_FOUND # 404

# PUT - update a product by Id
@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product_by_id(product_id):
    updated_product = request.get_json()
    for product in products:
        if product["_id"] == product_id:
            product["title"] = updated_product["title"]
            product["price"] = updated_product["price"]
            product["category"] = updated_product["category"]
            product["image"] = updated_product["image"]

            return jsonify({
                "success": True,
                "message": "Product Updated Successfully"
            }), HTTPStatus.OK  # 200

    return jsonify({
        "success": False,
        "message": "Product Not Updated"
    }), HTTPStatus.NOT_FOUND  # 404



# DELETE -- delete a product by id
# DELETE http://127.0.0.1:5000/api/products/<int:product_id>
@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            products.remove(product)

            return jsonify({
                "success": True,
                "message": "Product deleted successfully"
            }), HTTPStatus.OK # 200

    return jsonify({
        "success": False,
        "message": "product Not Found"
    }), HTTPStatus.NOT_FOUND # 404


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
@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return {"count": len(coupons)}


# POST /api/coupons endpoint that adds a new coupon in coupons list.
#http://127.0.0.1:5000/api/coupons
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()
    new_coupon["_id"] = len(coupons) + 1
    coupons.append(new_coupon)

    return jsonify({
        "success": True,
        "message": "Coupon successfully created",
        "data": new_coupon
    }), HTTPStatus.CREATED  # 201

# GET /api/coupons/<int:id> endpoint that returns a coupon that matches the given id..
#http://127.0.0.1:5000/api/coupons/2
@app.route("/api/coupons/<int:coupon_id>", methods=["GET"])
def get_coupon_by_id(coupon_id):

    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            return jsonify({
                "success": True,
                "message": "Coupon retrieved ",
                "data": coupon
            }), HTTPStatus.OK  # 200

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND  # 404



    #  Final Report 
#Put /api/coupons/<int:id>   endpoint that allows editing an existing coupon by its id.
#if the coupon is not found, return an appropriate error message and status code.

#http://127.0.0.1:5000/api/coupons/1
@app.route("/api/coupons/<int:coupon_id>", methods=["PUT"])
def update_coupon_by_id(coupon_id):
    updated_coupon = request.get_json()

    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupon["code"] = updated_coupon["code"]
            coupon["discount"] = updated_coupon["discount"]

            return jsonify({
                "success": True,
                "message": "Coupon updated successfully",
                "data": coupon
            }), HTTPStatus.OK

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND



#Delete /api/coupons/<int:id>  endpoint that allows deleting an existing coupon by its id.
#if the coupon is not found, return an appropriate error message and status code.

#http://127.0.0.1:5000/api/coupons/1
@app.route("/api/coupons/<int:coupon_id>", methods=["DELETE"])
def delete_coupon_by_id(coupon_id):

    for coupon in coupons:
        if coupon["_id"] == coupon_id:
            coupons.remove(coupon) 

            return jsonify({
                "success": True,
                "message": "Coupon deleted successfully"
            }), HTTPStatus.OK

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND



if __name__ == "__main__":
  app.run(debug=True)
# When this file is run directly: __name__ == "__main__"
# When this file is imported as module: __name__ == "server.py"