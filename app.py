from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the root URL ('/') that responds to GET requests
@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
