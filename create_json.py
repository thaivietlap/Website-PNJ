import json

# Danh sách nhẫn
ringss = [
    {
        "id": 1,
        "title": "Elegant Gold Ring",
        "price": 109.95,
        "description": "A beautiful gold ring designed for everyday elegance. Perfect for any occasion and can be worn alone or stacked.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.5,
            "count": 120
        }
    },
    {
        "id": 2,
        "title": "Classic Silver Ring",
        "price": 22.3,
        "description": "A classic silver ring that complements any outfit. Lightweight and comfortable for daily wear.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.1,
            "count": 259
        }
    },
    {
        "id": 3,
        "title": "Diamond Accent Ring",
        "price": 55.99,
        "description": "A stunning ring with diamond accents, suitable for formal occasions. A perfect gift for loved ones.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.7,
            "count": 500
        }
    },
    {
        "id": 4,
        "title": "Simple Band Ring",
        "price": 15.99,
        "description": "A simple yet elegant band ring. Perfect for stacking or wearing alone.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 2.1,
            "count": 430
        }
    },
    {
        "id": 5,
        "title": "Rose Gold Ring",
        "price": 695,
        "description": "An exquisite rose gold ring inspired by nature. A stunning piece to add to any jewelry collection.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.6,
            "count": 400
        }
    },
    {
        "id": 6,
        "title": "Vintage Style Ring",
        "price": 168,
        "description": "A vintage-inspired ring with intricate designs. Perfect for collectors and enthusiasts.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 3.9,
            "count": 70
        }
    },
    {
        "id": 7,
        "title": "Stackable Gemstone Ring",
        "price": 9.99,
        "description": "A colorful gemstone ring perfect for stacking with other rings. Adds a pop of color to any outfit.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 3,
            "count": 400
        }
    },
    {
        "id": 8,
        "title": "Modern Art Ring",
        "price": 10.99,
        "description": "A modern art-inspired ring that makes a statement. Unique and stylish for the fashion-forward.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 1.9,
            "count": 100
        }
    },
    {
        "id": 9,
        "title": "Gold Plated Ring",
        "price": 64,
        "description": "A beautifully crafted gold plated ring. Ideal for both casual and formal wear.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 3.3,
            "count": 203
        }
    },
    {
        "id": 10,
        "title": "Swarovski Crystal Ring",
        "price": 109,
        "description": "A sparkling Swarovski crystal ring that catches the light beautifully. Perfect for special occasions.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 2.9,
            "count": 470
        }
    },
    {
        "id": 11,
        "title": "Handmade Artisan Ring",
        "price": 109,
        "description": "A unique handmade artisan ring with intricate details. Perfect for those who appreciate craftsmanship.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.8,
            "count": 319
        }
    },
    {
        "id": 12,
        "title": "Elegant Birthstone Ring",
        "price": 114,
        "description": "A personalized birthstone ring that makes a thoughtful gift. Customize it with your choice of stone.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.8,
            "count": 400
        }
    },
    {
        "id": 13,
        "title": "Art Deco Style Ring",
        "price": 599,
        "description": "An exquisite Art Deco style ring with geometric patterns. A timeless piece for any jewelry collection.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 2.9,
            "count": 250
        }
    },
    {
        "id": 14,
        "title": "Custom Engraved Ring",
        "price": 999.99,
        "description": "A custom engraved ring that captures a special moment. Ideal for anniversaries and celebrations.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 2.2,
            "count": 140
        }
    },
    {
        "id": 15,
        "title": "Boho Style Ring Set",
        "price": 56.99,
        "description": "A beautiful set of boho style rings, perfect for layering. Each piece adds a unique touch to your style.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 2.6,
            "count": 235
        }
    },
    {
        "id": 16,
        "title": "Stackable Band Rings",
        "price": 29.95,
        "description": "A set of stackable band rings that can be worn in various combinations. Versatile and stylish.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 2.9,
            "count": 340
        }
    },
    {
        "id": 17,
        "title": "Minimalist Design Ring",
        "price": 39.99,
        "description": "A minimalist ring that emphasizes simplicity and elegance. Perfect for daily wear.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 3.8,
            "count": 679
        }
    },
    {
        "id": 18,
        "title": "Colorful Enamel Ring",
        "price": 9.85,
        "description": "A playful ring featuring colorful enamel designs. Adds a fun touch to any outfit.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.7,
            "count": 130
        }
    },
    {
        "id": 19,
        "title": "Twisted Band Ring",
        "price": 7.95,
        "description": "A unique twisted band ring that stands out. Perfect for those who love contemporary designs.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 4.5,
            "count": 146
        }
    },
    {
        "id": 20,
        "title": "Vintage Floral Ring",
        "price": 12.99,
        "description": "A vintage floral ring that adds a touch of romance. Perfect for gifts and special occasions.",
        "category": "jewelry",
        "images": "E:\\python\\python_web\\static\\1.jpg",
        "rating": {
            "rate": 3.8,
            "count": 92
        }
    }
]


# Tạo file JSON
with open('rings.json', 'w') as f:
    json.dump(ringss, f, indent=4)

print("File rings.json đã được tạo thành công!")
