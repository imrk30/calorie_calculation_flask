from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def calorie():
    if request.method == 'POST':
        foodName = request.form['foodName']
        carbs = request.form['carbs']
        proteins = request.form['proteins']
        fats = request.form['fats']

        cc = float(carbs) * 4
        cp = float(proteins) * 4
        cf = float(fats) * 9
        ct = round(cc+cp+cf)

        return render_template('result.html',foodName=foodName,cc=cc,cp=cp,cf=cf,ct=ct)
    else:
        return 'Sorry !!'

if __name__ == '__main__':
   app.run(debug=True)