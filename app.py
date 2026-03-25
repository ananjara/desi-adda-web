from flask import Flask, render_template

app = Flask(__name__)

# The Complete Desi Adda Menu Database
menu_data = {
    "Curry Street Style": [
        {"name": "Mumbai Misal Pav", "price": "12.99"},
        {"name": "Shahi Paneer w/ Paratha", "price": "12.99"},
        {"name": "Sindhi Dal Pakwaan", "price": "10.99"},
        {"name": "Chole w/ Amritsari Kulcha", "price": "12.99"}
    ],
    "Frankies": [
        {"name": "Street Frankie", "price": "9.99"},
        {"name": "Bombay Frankie", "price": "10.99"},
        {"name": "Chinese Frankie - Cold", "price": "10.99"},
        {"name": "Manchurian Frankie", "price": "10.99"},
        {"name": "Peri Peri Frankie", "price": "11.99"},
        {"name": "Tandoori Frankie", "price": "11.99"}
    ],
    "Sandwiches": [
        {"name": "Grilled Cheese", "price": "5.99"},
        {"name": "Grilled Cheese (Amul)", "price": "7.49"},
        {"name": "Veggie Amul Cheese", "price": "11.99"},
        {"name": "Bombay Club", "price": "11.99"},
        {"name": "Samosa", "price": "11.99"},
        {"name": "Masala", "price": "11.49"},
        {"name": "Chilli Cheese Corn", "price": "11.99"},
        {"name": "Veg Paneer Sandwich", "price": "11.99"},
        {"name": "Peri-Peri Sandwich", "price": "11.99"},
        {"name": "Cheese Chutney (Non-Grilled)", "price": "7.49", "muted": True},
        {"name": "Amul Cheese Jam (Non-Grilled)", "price": "7.49", "muted": True},
        {"name": "Bombay Masala Veg Butte (Non-Grilled)", "price": "7.99", "muted": True}
    ],
    "Maggie": [
        {"name": "Regular Maggie", "price": "4.99"},
        {"name": "Amul Cheese Maggie", "price": "7.99"},
        {"name": "Double Masala Cheese Maggie", "price": "9.99"},
        {"name": "Adda Spl Maggie", "price": "9.99"},
        {"name": "Hot & Sour Maggie", "price": "9.99"},
        {"name": "Manchow Maggie", "price": "9.99"}
    ],
    "Kathi Rolls": [
        {"name": "Paneer Tikka Roll", "price": "9.99"},
        {"name": "Cheesey Aloo Roll", "price": "9.99"},
        {"name": "Channa Roll", "price": "9.99"},
        {"name": "ANY 2 ABOVE", "price": "17.99", "highlight": "red"},
        {"name": "Cheese Samosa Roll", "price": "10.49"},
        {"name": "Schezwan Samosa Roll", "price": "10.49"}
    ],
    "Pavs": [
        {"name": "Regular Wada Pav (1)", "price": "3.99"},
        {"name": "Bombay Wada Pav (1)", "price": "5.99"},
        {"name": "Dabang Wada Pav (1)", "price": "5.99"},
        {"name": "Regular Dabeli (1)", "price": "4.50"},
        {"name": "Kutchi Dabeli (1)", "price": "5.99"},
        {"name": "Bombay Wada Plate (2pcs)", "price": "9.99"},
        {"name": "Kutchi Dabeli Plate (2pcs)", "price": "10.99"}
    ],
    "Chaats": [
        {"name": "Sev Puri", "price": "6.99"},
        {"name": "Dahi Puri", "price": "7.99"},
        {"name": "Bhel Puri", "price": "8.49"},
        {"name": "Peanut Chaat", "price": "7.00"},
        {"name": "Dehli Chaat", "price": "9.99"},
        {"name": "Bombay Chaat", "price": "7.99"},
        {"name": "Samosa Chaat", "price": "9.99"},
        {"name": "Surti Ragda Samosa", "price": "9.99"},
        {"name": "Papadi Chaat", "price": "8.49"}
    ],
    "Samosas & Shakes": [
        {"name": "Punjabi Samosa (2 for)", "price": "5.00"},
        {"name": "Hyderabadi Samosa", "price": "6.00"},
        {"name": "Jalapeno Cheese Samosa", "price": "6.00"},
        {"name": "Milkshakes", "is_subheader": True},
        {"name": "Vanilla / Chocolate", "price": "7.99"},
        {"name": "Sitafal / Chikoo", "price": "8.49"},
        {"name": "Rose Strawberry", "price": "9.99"},
        {"name": "Ferrero Chocolate", "price": "9.99"}
    ],
    "Masala Sodas": [
        {"name": "Lime / Rose / Green Mango / Orange", "price": "3.99 - 4.99"},
        {"name": "Fresh Sugarcane Juice", "price": "8.00", "highlight": "yellow"}
    ],
    "Ice Golas": [
        {"name": "On Stick (2 flavors)", "price": "4.00"},
        {"name": "On Bowl (3 flavors)", "price": "6.00"},
        {"name": "Rajwadi Gola Dish", "price": "7.00"},
        {"name": "Flavors: Rose, Orange, Kala Khata, Jeera, Kachie Karie, Pineapple, Mango", "is_flavor_list": True}
    ],
    "Lassi & Coffee": [
        {"name": "Mango Lassi", "price": "5.99"},
        {"name": "Rajwadi Mango Lassi", "price": "6.99"},
        {"name": "Sweet / Salted Lassi", "price": "5.99"},
        {"name": "Indian Cold Coffee", "is_subheader": True},
        {"name": "Reg Cold Coffee", "price": "4.99"},
        {"name": "Cold Foam / Hazelnut / Mocha", "price": "5.99 - 6.99"},
        {"name": "Vanilla / Caramel Cold Foam", "price": "6.99"}
    ],
    "Adda Special": [
        {"name": "Cold-Coco", "price": "6.99"},
        {"name": "Kitkat / Oreo Coffee", "price": "8.99"},
        {"name": "Sakinaka- Vadapav", "price": "5.99"},
        {"name": "Meetha Paan", "price": "2.00", "highlight": "yellow"},
        {"name": "Singoda / Chocolate Paan", "price": "3.00 - 4.00"},
        {"name": "Rose / Kesar Pista Falooda", "price": "8.00 - 9.00"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', menu_categories=menu_data)

if __name__ == '__main__':
    app.run(debug=True)