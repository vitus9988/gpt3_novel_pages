from flask import Flask, render_template, request, redirect, url_for
import openai
import secure


app = Flask(__name__)


def makeGptSentence(topic,mt, tmp, topp, fpty, ppty):
    
    openai.api_key = secure.access_token
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{topic} novel short write",
        temperature=tmp,
        max_tokens=mt,
        top_p=topp,
        frequency_penalty=fpty,
        presence_penalty=ppty
    )

    result = response['choices'][0]['text']
    
    return result


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/paramset-page', methods=['POST'])
def paramset():
    return render_template('paramset.html')


@app.route('/novel-page', methods=['GET','POST'])
def novel():
    if request.method == "POST":
        topic = str(request.form['NovelTheme'])
        mt = int(request.form['mt'])
        tmp = float(request.form['tmp'])
        topp = float(request.form['topp'])
        fpty = float(request.form['fpty'])
        ppty = float(request.form['ppty'])
        
        data = makeGptSentence(topic, mt, tmp, topp, fpty, ppty)
    
    return render_template('novel.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)