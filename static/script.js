document.addEventListener('DOMContentLoaded', () => {
    const homeButton = document.getElementById('home-btn');
    const cartButton = document.getElementById('cart-btn');
    const addToCartButton = document.querySelectorAll('.add-to-cart');
    const removeFromCartButton = document.querySelectorAll('.remove-from-cart');
    const loginForm = document.getElementById('login-form');
    const signUpForm = document.getElementById('sign-up-form');
    
    //HOME
    homeButton.addEventListener('click', (event) => {
        event.preventDefault();
        window.location.href = '/';
    });
    
    //PRODUCTS
    document.addEventListener('DOMContentLoaded', async () => {
        const productList = document.getElementById('product-list');
    
        try {
            // Fetch products from Fake Store API
            const response = await fetch('https://fakestoreapi.com/products');
            if (!response.ok) {
                throw new Error('Failed to fetch products');
            }
            const products = await response.json();
    
            // Clear existing content
            productList.innerHTML = '';
    
            // Create product cards
            products.forEach(product => {
                const productCard = document.createElement('div');
                productCard.classList.add('product-card');
                productCard.innerHTML = `
                    <img src="${product.image}" alt="${product.title}">
                    <h3>${product.title}</h3>
                    <p>Price: $${product.price}</p>
                `;
                productList.appendChild(productCard);
            });
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while fetching products.');
        }
    });
    
    
    //CART
    cartButton.addEventListener('click', (event) => {
        event.preventDefault();
        window.location.href = '/cart';
    });
    if (document.getElementById('cart')) {
        displayCart();
    }
    
    //ADD TO CART
    addToCartButton.forEach(button => { 
        //as soon as you click on 'add to cart' btn JS detects this click
        button.addEventListener('click', async () => {
            const productId = button.dataset.id;
            try {
                const response = await fetch('/add_to_cart', { 
                    //The JavaScript code sends a POST request to the Flask server at the /add_to_cart endpoint using the fetch API.
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({
                        'product_id': productId
                    })
                });
    
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
    
                const data = await response.json();
                if (data.success) {
                    alert('1 item added to cart');
                } else {
                    alert('Failed to add item to cart');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred while adding the item to the cart.');
            }
        });
    });
    
    //DISPLAY CART
    async function displayCart() {
        try {
            const response = await fetch('/cart', {
                method: 'GET'
            });
            if (!response.ok) {
                throw new Error('Failed to fetch cart data');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while displaying or updating the cart.');
        }
    }
    
    //REMOVE FROM CART
    removeFromCartButton.forEach(button => {
        button.addEventListener('click', async (event) => {
            event.preventDefault();
            const productId = button.dataset.id;
            await removeFromCart(productId);
        });
    });
    async function removeFromCart(productId) {
        try {
            //Goes to Flask to handle the GET request for '/remove_from_cart' URL
            const response = await fetch('/remove_from_cart', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'product_id': productId
                })
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            if (data.success) {
                await displayCart(); // Refresh cart display after successful removal
                window.location.reload(); // Refresh the browser                
            } else {
                alert('Failed to remove item from cart');
            }
        } catch (error) {
            alert('An error occurred while removing the item from the cart.');
        }
    }

    //LOGIN SUBMIT
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(loginForm);

            try {
                const response = await fetch('/loginsubmit', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (data.success) {
                    alert('Logged in successfully');
                    window.location.href = '/user'; // Redirect to the user page
                } else {
                    alert(data.message || 'Failed to log in');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during login.');
            }
        });
    }
    
    //SIGN UP SUBMIT
    if (signUpForm) {
        signUpForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(signUpForm);

            try {
                const response = await fetch('/signupsubmit', {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (data.success) {
                    alert('Signed up successfully');
                    window.location.href = '/login'; // Redirect to the login page
                } else {
                    alert(data.message || 'Failed to sign up');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during sign-up.');
            }
        });
    }       
    document.addEventListener('DOMContentLoaded', function() {
        const paymentMethodRadios = document.querySelectorAll('input[name="payment_mode"]');
        const debitCardDetails = document.getElementById('debit-card-details');
    
        paymentMethodRadios.forEach(radio => {
            radio.addEventListener('change', function() {
                if (this.value === 'Debit Card') {
                    debitCardDetails.style.display = 'block';
                } else {
                    debitCardDetails.style.display = 'none';
                }
            });
        });
    });
    document.getElementById('checkout-form').addEventListener('submit', async function(event) {
        event.preventDefault();
        
        const paymentMode = document.querySelector('input[name="payment_mode"]:checked').value;
        print("Hello")
        if (paymentMode === 'Debit Card') {
            const cardNumber = document.getElementById('card_number').value;
            const expiryMonth = document.getElementById('expiry_month').value;
            const expiryYear = document.getElementById('expiry_year').value;
            const cvv = document.getElementById('cvv').value;
            const expiryDate = `${expiryMonth}-${expiryYear}`;

            const response = await fetch('./debit_card_details.json'); 
            //Now the cursor goes to our own API debit_card_details.json
            const response_data = await response.json();

            if (
                cardNumber === response_data.data.card_number &&
                expiryDate === response_data.data.expiry_date &&
                parseInt(cvv) === response_data.data.cvv
            ) {
                alert('Card verified successfully!');
                window.location.href = '/your_orders';
            } else {
                alert('Card verification failed. Please check your card details and try again.');
            }
        } else {
            this.submit();
        }
    });     
});
