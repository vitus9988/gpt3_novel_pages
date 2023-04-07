#-*- coding:utf-8 -*-
import base64
from flask import Flask, render_template, request, redirect, url_for
import openai
import secure


app = Flask(__name__)
    
    
def makeGptSentence(topic, mt, tmp, topp, fpty, ppty):
    prompt = fr"Write a novel of moderate length. Finish the story by writing to the end, with no interruptions. In the header and footer, remove any stories that are not relevant to the novel.Topics: {topic}"
    
    openai.api_key = secure.access_token
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user", 
            "content": prompt,
            }],
        max_tokens = mt,
        temperature = tmp,
        top_p = topp,
        frequency_penalty = fpty,
        presence_penalty = ppty,
    )
    result = completion['choices'][0]['message']['content']
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