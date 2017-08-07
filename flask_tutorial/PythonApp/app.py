from flask import Flask, render_template
import os
import socket

app = Flask(__name__)

@app.route("/")
def main():

    visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)
    #return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)