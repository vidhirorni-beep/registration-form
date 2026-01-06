from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        return render_template(
            "success.html",
            name=name,
            email=email,
            phone=phone
        )
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
