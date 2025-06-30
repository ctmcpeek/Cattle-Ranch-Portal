from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Cattle Ranch Portal is working!"
app = Flask(__name__)
 Entry point for the Flask app
 if __name__ == "__main__":
    app.run(debug=True)

