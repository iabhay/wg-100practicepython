import flask
from flask import Flask, render_template_string, request
app = Flask(__name__)

html = """
    <div class="form">
        <form action="{{url_for('sent')}}" method="POST">
            <input title="Your email is safe." placeholder="Enter Text" type="text" name="line" required> <br>
            <button class="go-button" type="submit">Submit</button>
        </form>
    </div>
"""


@app.route('/')
def index():
    return render_template_string(html)


@app.route('/sent', methods=['GET','POST'])
def sent():
    line = None
    if request.method == 'POST':
        line = request.form['line']
        with open("output99.txt", "a+") as f:
            f.write(line + "\n")
        return render_template_string(html)


if __name__ == '__main__':
    app.run(debug=True)
