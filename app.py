from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = 'your_openai_api_key'
@app.route('/')
def homepage():
    return render_template('homepage.html')  
@app.route('/api', methods=['POST'])
def api():
    message=request.form.get("message")
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
    {"role": "user", "content": message}
    ]
    )
    return completion.choices[0].message

if __name__ == '__main__':
    app.run()