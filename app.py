from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key'

# Default route to serve the homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')  # This will render the homepage.html file

# API route to handle chat requests
@app.route('/api', methods=['POST'])
def api():
    # Get the message from the request
    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'response': 'No message provided'})

    # Use OpenAI API to generate a response
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # or whichever engine you prefer
            prompt=user_message,
            max_tokens=100  # Adjust the token limit as needed
        )

        # Extract the response from OpenAI API
        bot_response = response.choices[0].text.strip()

    except Exception as e:
        bot_response = f"Error: {str(e)}"

    # Return the response as JSON
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
