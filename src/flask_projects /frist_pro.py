from flask import Flask

app = Flask(__name__)

from colorama import Fore,Style,init
init(autoreset=True)

@app.route("/")
def hello_world():
    return f"{Fore.CYAN}<p>sachin masti</p>"
app.run(debug=True)
