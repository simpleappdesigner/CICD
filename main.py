from flask import Flask
import os

os.environ["no_proxy"] = "*"
           
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World : Flask in Docker"

'''
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)
'''