from flask import Flask
import os
import time

os.environ["no_proxy"] = "*"

def log_file(log_item):
    with open("./Runlog/log.txt","a") as fh:
        fh.write(log_item + "\n")

app = Flask(__name__)

@app.route("/")
def home():
    response=f"Hello World : Flask in Docker. Current Time:{time.strftime('%B %d, %Y %I:%M:%S %p')}"
    log_file(response)
    return response

'''
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5000)
'''