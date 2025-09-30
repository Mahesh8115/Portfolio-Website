from flask import Flask, render_template, request

# Tell Flask to use "public" instead of "static"
app = Flask(__name__, static_folder="public")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you could save the data or send via email
        return render_template("contact.html", success=True, name=name)
    return render_template('contact.html', success=False)


if __name__ == "__main__":
    app.run(debug=True)
