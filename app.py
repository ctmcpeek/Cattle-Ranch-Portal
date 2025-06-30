
from flask import Flask

# Entry point for the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Cattle Ranch Portal is working!"

if __name__ == "__main__":
    app.run(debug=True)


