from flask import Flask                                                                                             
import requests
import os
import socket                                                                                                       

app = Flask(__name__)

@app.route('/V2')
def get_data():
    url=os.environ["VAR1"]
    return requests.get(url).content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)