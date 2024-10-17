from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = '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'
@app.route('/')
def homepage():
    return render_template('homepage.html')  
@app.route('/api', methods=['POST'])
def api():
    message=request.form.get("message")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
    {"role": "user", "content": message}
    ]
    )
    if completion.choices[0].message!=None:
        return completion.choices[0].message
    else:
        return "Sorry, I didn't understand that. Can you try again?"

if __name__ == '__main__':
    app.run()