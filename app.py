from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/paramset-page', methods=['GET','POST'])
def paramset():
    if request.method == "POST":
        value = request.form['paramsform']
        value = str(value)
        print(value)
    return render_template('paramset.html')


@app.route('/novel-page', methods=['GET','POST'])
def novel():
    
    return render_template('novel.html')





if __name__ == "__main__":
    app.run(debug=True)