from flask import Flask, render_template_string, request
from ques81 import Question81
app = Flask(__name__)
func = Question81()
html = """
  		      <div class="form">
              <form action="{{url_for('sent')}}" method="POST">
  			        <input title="Your email address will be safe with us." placeholder="Enter username" type="text" name="username" required> <br>
  			        <input title="Your email address will be safe with us." placeholder="Enter password" type="text" name="password" required> <br>
                    {{message|safe}}
                <button class="go-button" type="submit"> Submit </button>
  		        </form>
          </div>
"""

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        while True:
            usr = request.form['username']
            if not func.username_checker(usr):
                return render_template_string(html, message="Username exists!"+"<br>")
                continue
            else:
                print("Username is fine!")
                break
        while True:
            psw = request.form['password']
            if not func.password_validator(psw):
                return render_template_string(html, message="Please check password!")
            else:
                print("Password is fine" + "<br>")
                break
        return render_template_string(html, message="Success"+"<br>")
if __name__ == "__main__":
    app.run(debug=True)
