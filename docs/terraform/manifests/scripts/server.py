from flask import Flask

app = Flask(__name__)

# Define a custom route
@app.route('/')
def home():
    return "Hello, World! This is the home page."

@app.route('/greet')
def greet():
    return "Greetings from your custom route!"

if __name__ == '__main__':
    # Listen on all interfaces, port 8080 (requires sudo/root privileges)
    app.run(host='0.0.0.0', port=8080)
