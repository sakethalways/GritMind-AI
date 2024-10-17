from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")  # Get the OpenAI API key from environment variables

@app.route('/')
def homepage():
    creator_name = "Saketh Muthyapuwar"  # Define the creator's full name
    short_name = "Saketh"  # Define the short name
    return render_template('homepage.html', creator_name=creator_name, short_name=short_name)

@app.route('/api', methods=['POST'])
def api():
    data = request.json  # Receive JSON data
    message = data.get("message")  # Get the 'message' key from JSON data
    if not message:  # Check if the message is None or empty
        return jsonify({"error": "Message is required"}), 400

    try:
        system_prompt = {
            "role": "system",
            "content": "You are GritMind-AI, a motivational and knowledgeable chatbot created to help users with advice, support, and information on mental resilience, fitness, and other inquiries. Always be encouraging, supportive, and informative."
        }
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[system_prompt,
                {"role": "user", "content": message}
            ]
        )
        if completion.choices and completion.choices[0].message:
            response = completion.choices[0].message['content']  # Extract the response
            return jsonify({"response": response})  # Return the response as JSON
        else:
            return jsonify({"response": "Sorry, I didn't understand that. Can you try again?"}), 400
    except openai.error.InvalidRequestError as e:
        return jsonify({"error": str(e)}), 400
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode for easier troubleshooting
