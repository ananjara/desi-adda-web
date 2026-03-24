from flask import Flask, render_template # Notice we added render_template here

app = Flask(__name__)

@app.route('/')
def home():
    # This tells Python to look in the templates folder and send this file
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)