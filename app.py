import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Sample data: list of products
products = [
    {"id": 1, "name": "Abstract Print Patchwork shirt (multicolor)", "price": 59, "image": "feature-pro/f1.jpg",  "small_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f4.jpg",
        "feature-pro/f5.jpg"
    ],
        "featured_images": [
        "feature-pro/f6.jpg",
        "feature-pro/f8.jpg",
        "feature-pro/n7.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 2, "name": "Abstract Print Patchwork shirt (Green)", "price": 65, "image": "feature-pro/f2.jpg", "small_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f4.jpg",
        "feature-pro/f5.jpg"
    ],
        "featured_images": [
        "feature-pro/f6.jpg",
        "feature-pro/f8.jpg",
        "feature-pro/n4.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 3, "name": "Abstract Print Patchwork shirt (Red)", "price": 55, "image": "feature-pro/f3.jpg", "small_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f4.jpg",
        "feature-pro/f5.jpg"
    ],
        "featured_images": [
        "feature-pro/f6.jpg",
        "feature-pro/f8.jpg",
        "feature-pro/n4.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 4, "name": "Abstract Print Patchwork shirt (Pink)", "price": 49, "image": "feature-pro/f4.jpg", "small_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f4.jpg",
        "feature-pro/f5.jpg"
    ],
        "featured_images": [
        "feature-pro/f6.jpg",
        "feature-pro/f8.jpg",
        "feature-pro/n1.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 5, "name": "Abstract Print Patchwork shirt (Dark Blue)", "price": 70, "image": "feature-pro/f5.jpg", "small_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f4.jpg",
        "feature-pro/f5.jpg"
    ],
        "featured_images": [
        "feature-pro/f6.jpg",
        "feature-pro/n1.jpg",
        "feature-pro/n4.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 6, "name": "Block Button Down Loose Corduroy Shirt Jacket", "price": 69, "image": "feature-pro/f6.jpg", "small_images": [
        "feature-pro/f6.jpg"],
     "featured_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f6.jpg",
        "feature-pro/f2.jpg",]},
    {"id": 7, "name": "Capri Pants for Women", "price": 59, "image": "feature-pro/f7.jpg", "small_images": [
        "feature-pro/f7.jpg",
        "feature-pro/f8.jpg"],
     "featured_images": [
        "feature-pro/f6.jpg",
        "feature-pro/n6.jpg",
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",]},
    {"id": 8, "name": "Cute Print Crew Neck Top", "price": 57, "image": "feature-pro/f8.jpg", "small_images": [
        "feature-pro/f7.jpg",
        "feature-pro/f8.jpg"],
     "featured_images": [
        "feature-pro/f1.jpg",
        "feature-pro/f2.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/f4.jpg",]},
    {"id": 9, "name": "Regular Fit Linen-blend grandad shirt", "price": 59, "image": "feature-pro/n1.jpg", "small_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n5.jpg"],
     "featured_images": [
        "feature-pro/n4.jpg",
        "feature-pro/f1.jpg",
        "feature-pro/n7.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 10, "name": "Linen shirt Slim Fit", "price": 65, "image": "feature-pro/n2.jpg", "small_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n5.jpg",],
     "featured_images": [
        "feature-pro/n4.jpg",
        "feature-pro/f3.jpg",
        "feature-pro/n7.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 11, "name": "Linen shirt (White)", "price": 55, "image": "feature-pro/n3.jpg", "small_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n5.jpg"],
     "featured_images": [
        "feature-pro/n4.jpg",
        "feature-pro/n6.jpg",
        "feature-pro/n7.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 12, "name": "Palm Tree Jacquard Shirt", "price": 49, "image": "feature-pro/n4.jpg", "small_images": [
        "feature-pro/n4.jpg",
        "feature-pro/n8.jpg"],
     "featured_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n5.jpg",]},
    {"id": 13, "name": "Regular-fit Denim Shirt", "price": 70, "image": "feature-pro/n5.jpg", "small_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n5.jpg"],
     "featured_images": [
        "feature-pro/n4.jpg",
        "feature-pro/n6.jpg",
        "feature-pro/n7.jpg",
        "feature-pro/n8.jpg",]},
    {"id": 14, "name": "Cotton Blend Yarn Dye Chino Shorts", "price": 69, "image": "feature-pro/n6.jpg", "small_images": [
        "feature-pro/n6.jpg"],
     "featured_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n4.jpg",]},
    {"id": 15, "name": "Shacket Shirt with 2 Patch Pockets", "price": 59, "image": "feature-pro/n7.jpg", "small_images": [
        "feature-pro/n7.jpg",
        "feature-pro/n3.jpg"],
     "featured_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n4.jpg",
        "feature-pro/n5.jpg",]},
    {"id": 16, "name": "Cotton Shirt Muscle Fit", "price": 57, "image": "feature-pro/n8.jpg", "small_images": [
        "feature-pro/n4.jpg",
        "feature-pro/n8.jpg"],
     "featured_images": [
        "feature-pro/n1.jpg",
        "feature-pro/n2.jpg",
        "feature-pro/n3.jpg",
        "feature-pro/n5.jpg",]}
]

# Configure session to use instead of signed cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///user.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Home-page"""

    user_id = session["user_id"]
    if request.method == "POST":
        quantity = request.form.get("quantity")
        size = request.form.get("size")
        product_id = request.form.get("product_id")
        image = request.form.get("product_image")
        price = request.form.get("product_price")
        name = request.form.get("product_name")

        if quantity.isnumeric() and int(quantity) <= 0:
            flash("Quantity should be greater than 0.")
            return redirect("/")

        db.execute("INSERT INTO cart (user_id, product_id, name, size, quantity, image, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   user_id, product_id, name, size, quantity, image, price)

        flash("Added to Cart!")
        return redirect("/")

    else:
        cart_items = db.execute("""
        SELECT product_id, name, size, SUM(quantity) as quantity, price, image
        FROM cart
        WHERE user_id = ?
        GROUP BY product_id, name, size, price, image
        """, user_id)

        cart_item_count = len(cart_items)

        product = products
        return render_template("index.html", active_page='index', products=product, cart_item_count=cart_item_count)


@app.route("/about-us", methods=["GET", "POST"])
@login_required
def about():
    """About Us"""

    user_id = session["user_id"]
    cart_items = db.execute("""
        SELECT product_id, name, size, SUM(quantity) as quantity, price, image
        FROM cart
        WHERE user_id = ?
        GROUP BY product_id, name, size, price, image
        """, user_id)

    cart_item_count = len(cart_items)

    return render_template("about-us.html", active_page='about', cart_item_count=cart_item_count)


@app.route("/contact-us", methods=["GET", "POST"])
@login_required
def contact():
    """Contact Us"""
    if request.method == "POST":
        flash("Thank You! We Will Contact Back You Soon")

        return redirect("/contact-us")
    else:
        user_id = session["user_id"]
        cart_items = db.execute("""
            SELECT product_id, name, size, SUM(quantity) as quantity, price, image
            FROM cart
            WHERE user_id = ?
            GROUP BY product_id, name, size, price, image
            """, user_id)

        cart_item_count = len(cart_items)

        return render_template("Contact-us.html", active_page='contact', cart_item_count=cart_item_count)


@app.route("/shop", methods=["GET", "POST"])
@login_required
def shop():
    """Where all the products can be find"""

    user_id = session["user_id"]
    if request.method == "POST":
        quantity = request.form.get("quantity")
        size = request.form.get("size")
        product_id = request.form.get("product_id")
        image = request.form.get("product_image")
        price = request.form.get("product_price")
        name = request.form.get("product_name")

        if quantity.isnumeric() and int(quantity) <= 0:
            flash("Quantity should be greater than 0.")
            return redirect("/shop")

        db.execute("INSERT INTO cart (user_id, product_id, name,  size, quantity, image, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   user_id, product_id, name, size, quantity, image, price)

        flash("Added to Cart!")

        return redirect("/shop")
    else:
        cart_items = db.execute("""
        SELECT product_id, name, size, SUM(quantity) as quantity, price, image
        FROM cart
        WHERE user_id = ?
        GROUP BY product_id, name, size, price, image
        """, user_id)

        cart_item_count = len(cart_items)
        per_page = 8  # Number of products per page
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * per_page  # Calculate the start index
        end = start + per_page  # Calculate the end index
        paginated_products = products[start:end]
        return render_template('shop.html', active_page='shop', products=paginated_products, page=page, total_pages=(len(products) - 1) // per_page + 1, cart_item_count=cart_item_count)


@app.route('/product/<int:product_id>', methods=["GET", "POST"])
@login_required
def product(product_id):
    """Single Product Page"""

    user_id = session["user_id"]

    if request.method == "POST":
        quantity = request.form.get("quantity")
        size = request.form.get("size")
        product_id = request.form.get("product_id")
        image = request.form.get("product_image")
        price = request.form.get("product_price")
        name = request.form.get("product_name")
        redirect_url = request.form.get("redirect_url")

        if not size:
            flash("Please select a size.")
            print("Size not selected")
            return redirect(f"/product/{product_id}")
        if quantity.isnumeric() and int(quantity) <= 0:
            flash("Quantity should be greater than 0.")
            return redirect(f"/product/{product_id}")

        db.execute("INSERT INTO cart (user_id, product_id, name, size, quantity, image, price) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   user_id, product_id, name, size, quantity, image, price)

        flash("Added to Cart!")
        if redirect_url:
            return redirect(redirect_url)
        else:
            return redirect(f"/product/{product_id}")

    else:

        product = next((item for item in products if item["id"] == product_id), None)
        if product is None:
            return apology("Product Not Found", 404)

        cart_items = db.execute("""
        SELECT product_id, name, size, SUM(quantity) as quantity, price, image
        FROM cart
        WHERE user_id = ?
        GROUP BY product_id, name, size, price, image
        """, user_id)

        cart_item_count = len(cart_items)

        return render_template(
            'product.html', active_page='shop',
            product=product,
            products=products,
            cart_item_count=cart_item_count
        )


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    """User's cart to buy product"""

    user_id = session["user_id"]

    if request.method == "POST":
        product_id = request.form.get("product_id")
        size = request.form.get("size")

        db.execute("DELETE FROM cart WHERE user_id = ? AND product_id = ? AND size = ?", user_id, product_id, size)

        flash("Removed from Cart!")

        return redirect("/cart")
    else:
        cart_items = db.execute("""
        SELECT product_id, name, size, SUM(quantity) as quantity, price, image
        FROM cart
        WHERE user_id = ?
        GROUP BY product_id, name, size, price, image
        """, user_id)

        cart_total = sum(item["price"] * item["quantity"] for item in cart_items)
        cart_item_count = len(cart_items)
        return render_template("cart.html", active_page='cart', cart_items=cart_items, cart_item_count=cart_item_count,  cart_total=cart_total)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)

        elif not request.form.get("password"):
            return apology("must provide password", 403)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username:
            return apology("Plz give a username")

        if not password:
            return apology("Plz give a password")

        if not confirmation:
            return apology("Plz confirm the password")

        if confirmation != password:
            return apology("Password does not match")

        hash_pass = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users (username, hash) VALUES (?,?)", username, hash_pass)
        except:
            return apology("username already exist")

        session["user_id"] = new_user

        return redirect("/")

    else:
        return render_template("register.html")


@app.route('/faq')
@login_required
def faq():
    user_id = session["user_id"]

    # FAQ data (questions and answers)
    faq_data = [
        {"question": "What payment methods do you accept?",
         "answer": "We accept major credit cards (Visa, MasterCard, American Express) and PayPal."},
        {"question": "How can I track my order?",
         "answer": "Once your order is shipped, you will receive a tracking number via email."},
        {"question": "Do you offer international shipping?",
         "answer": "Yes, we offer international shipping to most countries."},
        {"question": "What is your return policy?",
         "answer": "We offer a 30-day return policy on all items. If you're not satisfied with your purchase, you can return it for a full refund within 30 days of receipt."},
        {"question": "How can I change or cancel my order?",
            "answer": "If you need to change or cancel your order, please contact our customer service team as soon as possible. We will do our best to accommodate your request."}
    ]

    cart_items = db.execute("""
        SELECT product_id, name, size, SUM(quantity) as quantity, price, image
        FROM cart
        WHERE user_id = ?
        GROUP BY product_id, name, size, price, image
        """, user_id)

    cart_item_count = len(cart_items)
    return render_template('faq.html', active_page='faq', faq_data=faq_data, cart_item_count=cart_item_count)
