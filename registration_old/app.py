from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']

        return render_template(
            'success.html',
            name=name,
            email=email,
            phone=phone,
            gender=gender
        )

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
