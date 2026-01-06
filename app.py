from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store registrations in memory
registrations = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'father': request.form['father'],
            'mother': request.form['mother'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'gender': request.form['gender']
        }
        registrations.append(data)
        # Redirect to ID card page after registration
        return redirect(url_for('id_card', index=len(registrations)-1))
    return render_template('register.html')

@app.route('/id_card/<int:index>')
def id_card(index):
    if 0 <= index < len(registrations):
        data = registrations[index]
        return render_template('id_card.html', data=data)
    return "Invalid ID"

if __name__ == '__main__':
    app.run(debug=True)
