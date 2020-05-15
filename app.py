from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import codecs


app = Flask(__name__)

@app.route('/sympy/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    exp = request.args.get("exp", None)

    if(exp == "simplification"):
        file = codecs.open("output/simplification.html", 'r', 'utf-8')
        document= BeautifulSoup(file.read(),'html.parser')
    else:
        file = codecs.open("output/integrate.html", 'r', 'utf-8')
        document= BeautifulSoup(file.read(),'html.parser')

    # For debugging
    print(f"{exp} Functionality")

    response = {}
    response[0] = {}
    response[1] = {}
    response[0]["input"] = f"{exp}"
    response[0]["title"] = "Sympy" 
    response[1]["output"] = str(document) 
    response[1]["title"] = "documentation"
    response[1]["value"] = str(document) 

    # Check if user sent a name at all
    if not exp:
        response["ERROR"] = " please send a valid URL"
    
    # Now the Retrive for data for valid URL
    else:
        response["message"] = f"We have to perform {exp} operations"

    # Return the response in json format
    return jsonify(response)



# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
