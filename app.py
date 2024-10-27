import json
from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import hashlib, requests, mysql.connector, sqlite3
from datetime import datetime

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Database configuration
db_config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'loginapp'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

#Navigating to the Home Page
@app.route('/')
def index():
    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM products")
            products = cursor.fetchall()
        connection.close()
        return render_template('index.html', products=products)
    else:
        return "Error connecting to the database", 500

#Navigating to the Products Page
# @app.route('/products')
# def products():
#     try:
#         # Fetch products from Fake Store API
#         response = requests.get('E://python/python_web/rings.json')
#         response.raise_for_status()  # Raise an HTTPError for bad responses
#         products = response.json()
#         return render_template('products.html', products=products)
#     except Exception as e:
#         print(f"Error: {e}")
#         return "An error occurred while fetching products.", 500
@app.route('/products')
def products():
    try:
        # Đọc sản phẩm từ file rings.json
        with open('E://python//python_web//rings.json', 'r') as file:
            products = json.load(file)  # Tải dữ liệu JSON từ file
        
        return render_template('products.html', products=products)
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while fetching products.", 500


#Navigating to the Cart Page
@app.route('/cart', methods=['GET'])
def show_cart():
    cart = session.get('cart', [])
    total = sum(float(item['price']) for item in cart)
    return render_template('cart.html', cart=cart, total=total)

#Triggered when an item is added to cart
# @app.route('/add_to_cart', methods=['POST'])
# def add_to_cart():
#     try:
#         product_id = request.form.get('product_id')
#         if not product_id:
#             return jsonify(success=False, message="Product ID is missing"), 400

#         # Fetch product data from Fake Store API
#         response = requests.get(f'https://fakestoreapi.com/products/{product_id}')
#         response.raise_for_status()
#         product = response.json()

#         # Add product to cart session
#         cart = session.get('cart', [])
#         cart.append(product)
#         session['cart'] = cart
#         return jsonify(success=True, message="Item added to cart")
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify(success=False, message="An error occurred"), 500
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        product_id = request.form.get('product_id')
        if not product_id:
            return jsonify(success=False, message="Product ID is missing"), 400

        # Đọc sản phẩm từ file rings.json
        with open('E://python//python_web//rings.json', 'r') as file:
            products = json.load(file)  # Tải dữ liệu JSON từ file

        # Tìm sản phẩm theo product_id
        product = next((p for p in products if p['id'] == int(product_id)), None)
        if not product:
            return jsonify(success=False, message="Product not found"), 404

        # Thêm sản phẩm vào giỏ hàng
        cart = session.get('cart', [])
        cart.append(product)
        session['cart'] = cart

        return jsonify(success=True, message="Item added to cart")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False, message="An error occurred"), 500


#Triggered when an item is removed from the cart
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    try:
        product_id = int(request.form.get('product_id'))
        cart = session.get('cart', [])

        # Find and remove only the first instance of the product with the given ID
        for item in cart:
            if item['id'] == product_id:
                cart.remove(item)
                break  # Stop after removing the first matching item

        session['cart'] = cart
        return jsonify(success=True)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False, message="An error occurred"), 500

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/loginsubmit', methods=['POST'])
def loginsubmit():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            return jsonify(success=False, message="Email and password are required")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, hashed_password))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user:
                session['user_id'] = user['id']
                return jsonify(success=True)
            else:
                return jsonify(success=False, message="Invalid email or password")
        else:
            return jsonify(success=False, message="Database connection error")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False, message="An error occurred"), 500


@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user_id from the session
    return redirect('/')


@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@app.route('/signupsubmit', methods=['POST'])
def signupsubmit():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        if not name or not email or not password:
            return jsonify(success=False, message="All fields are required")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        connection = get_db_connection()
        if connection:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                               (name, email, hashed_password))
                connection.commit()
            connection.close()
            return jsonify(success=True)
        else:
            return jsonify(success=False, message="Database connection error")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(success=False, message="An error occurred"), 500

@app.route('/user')
def user_page():
    user_id = session.get('user_id')
    if not user_id:
        return redirect('/login')

    connection = get_db_connection()
    if connection:
        with connection.cursor(dictionary=True) as cursor:
            # Fetch user information
            cursor.execute("SELECT username, email FROM users WHERE id = %s", (user_id,))
            user = cursor.fetchone()

            # Fetch user orders
            cursor.execute("""
                SELECT id, date_purchased, image, title, description, price
                FROM orders
                WHERE user_email = %s
            """, (user['email'],))
            orders = cursor.fetchall()
        
        connection.close()

        if user:
            user_name = user['username']
            capitalized_name = user_name.capitalize()
            return render_template('user.html', user_name=capitalized_name, orders=orders)
        else:
            return redirect('/login')
    else:
        return "Database connection error", 500

#Inserts Order
def insert_order(email, date_purchased, image, title, description, price):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders(user_email,date_purchased,image,title,description,price) values(%s, %s, %s, %s, %s, %s)",(email,date_purchased,image,title,description,price))
        conn.commit()
        conn.close()

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        state = request.form.get('state')
        country = request.form.get('country')
        pincode = request.form.get('pincode')
        payment_mode = request.form.get('payment_mode')

        if payment_mode == 'debit_card':
            card_number = request.form.get('card_number')
            card_expiry_month = request.form.get('expiry_month')
            card_expiry_year = request.form.get('expiry_year')
            card_cvv = request.form.get('card_cvv')

            # Full URL for the JSON file
            json_url = url_for('static', filename='debit_card_details.json', _external=True)
            response = requests.get(json_url)
            if response.ok:
                card_details = response.json().get('data')
                if (card_number == card_details['card_number'] and
                        f"{card_expiry_month}-{card_expiry_year}" == card_details['expiry_date'] and
                        int(card_cvv) == card_details['cvv']):
                    # Card verified successfully
                    date_purchased = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    cart = session.get('cart', [])
                    for item in cart:
                        insert_order(email, date_purchased, item['image'], item['title'], item['description'], item['price'])
                    
                    session['order_details'] = {
                        'name': name, 'email': email, 'phone': phone, 'address1': address1, 'address2': address2,
                        'city': city, 'state': state, 'country': country, 'pincode': pincode, 'payment_mode': payment_mode,
                        'message': "Your order is accepted and it will be delivered to you in 3 business days.",
                        'cart': cart
                    }
                    session.pop('cart', None)  # Clear the cart
                    return redirect(url_for('your_orders'))
                else:
                    # Card verification failed
                    return render_template('checkout.html', cart=session.get('cart', []), total=sum(float(item['price']) for item in session.get('cart', [])), error="Card verification failed.")
            else:
                return render_template('checkout.html', cart=session.get('cart', []), total=sum(float(item['price']) for item in session.get('cart', [])), error="Error fetching card details.")
        else:
            # Cash on Delivery selected
            date_purchased = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print("DATE:::::",date_purchased)
            cart = session.get('cart', [])
            for item in cart:
                insert_order(email, date_purchased, item['images'], item['title'], item['description'], item['price'])
            
            session['order_details'] = {
                'name': name, 'email': email, 'phone': phone, 'address1': address1, 'address2': address2,
                'city': city, 'state': state, 'country': country, 'pincode': pincode, 'payment_mode': payment_mode,
                'message': "Your order is accepted and it will be delivered to you in 3 business days.",
                'cart': cart
            }
            session.pop('cart', None)  # Clear the cart
            return redirect(url_for('your_orders'))
    cart = session.get('cart', [])
    total = sum(float(item['price']) for item in cart)
    return render_template('checkout.html', cart=cart, total=total)


@app.route('/your_orders')
def your_orders():
    order_details = session.get('order_details', {})
    if not order_details:
        return redirect(url_for('index'))
    return render_template('your_orders.html', order=order_details)

if __name__ == '__main__':
    app.run(debug=True)
