import webbrowser
from threading import Timer
from flask import Flask, render_template, url_for

app = Flask(__name__)
port = "8080"

@app.route('/')
def index():
    return render_template("1.html")

def open_browser():
      webbrowser.open_new('http://127.0.0.1:' + port + '/')

if __name__ == "__main__":
      app.config['TEMPLATES_AUTO_RELOAD']=True
      Timer(1, open_browser).start()
      app.run(port=port, debug=False,use_reloader=False)