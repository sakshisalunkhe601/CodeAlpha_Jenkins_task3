from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Remoting Success! This Flask app is running on an Azure VM."

if __name__ == "__main__":
    # host='0.0.0.0' makes it accessible via the VM's Public IP
    app.run(host='0.0.0.0', port=5000)