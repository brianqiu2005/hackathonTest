from flask import Flask, render_template, request

##app = Flask(__name__)
app = Flask(__name__, template_folder = '../templates')


@app.route('/', methods=['GET', 'POST'])
def home():
    user_input = None
    if request.method == 'POST':
        user_input = request.form['user-input']  # Get user input from form
    return render_template('index.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
