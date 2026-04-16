from flask import Flask, request

app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    return {"message": "Welcome to Flask cohort#65"}

@app.route("/cohort-65", methods=["GET"])
def get_students_65():
    students_list = ["Sergio", "Leomar", "Charles", "Aymen", "Dejanirra", "Freysy", "Trishon"]
    return students_list

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

@app.route("/api/products", methods=["GET"])
def get_products():
    return {"data": products}

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return {"data": coupons}

@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return {"count": len(coupons)}

@app.route("/api/coupons", methods=["POST"])
def add_coupon():
    data = request.get_json()
    if not data or "code" not in data or "discount" not in data:
        return {"error": "Invalid data"}, 400

    new_id = max([c["_id"] for c in coupons]) + 1 if coupons else 1
    new_coupon = {
        "_id": new_id,
        "code": data["code"],
        "discount": data["discount"]
    }

    coupons.append(new_coupon)
    return new_coupon, 201

@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return coupon, 200
    return {"error": "Coupon not found"}, 404

if __name__ == "__main__":
    app.run()

    # this is a comment gg