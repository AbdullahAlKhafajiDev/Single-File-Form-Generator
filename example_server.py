from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    # Get the POST parameters
    params = request.form.to_dict()
    
    # Prepare the response message
    response = f"Switching relay..."
    # Send the response back to the requester as JSON
    responseObject = jsonify(message=response)
    responseObject.headers.add('Access-Control-Allow-Origin', '*')
    return responseObject

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
