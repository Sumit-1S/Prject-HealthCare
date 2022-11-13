from flask import Flask,render_template,request
import insur

app = Flask(__name__)

@app.route("/")
def hello():
  if request.method=="POST":
    age = request.form["age"]
    bmi = request.form["bmi"]
    sex = request.form["sex"]
    children = request.form["children"]
    smoker = request.form["smoker"]
    data = [age,bmi,sex,children,smoker]

    pred = insur.insurance(data)
    print(pred)
  return render_template("index.html")


if __name__ == '__main__':
  app.run(debug=True)