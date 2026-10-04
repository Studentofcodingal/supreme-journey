from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    Units = int(request.form["Units"])
    Bill = units * 5

    if Units <= 100:
        message = "Energy Saver"
    elif Units <= 200:
        message = "Energy User"
    else:
        messgae = "Energy Waster"
    
    return render_template("index.html", Units=Units, Bill=Bill, message=message)

if __name__ == "__main__":
    app.run(debug=True)