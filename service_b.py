#Service B
from flask import Flask, request, Response
import random

#flask service
app = Flask(__name__)

@app.route("/api/service_b", methods=['GET', 'POST'])
def service_b():
    #receive the message from Service A
    message = request.args.get('message')
    #print the message
    print(message)
    
    #generate a random number between 0 and 9
    num = random.randint(0, 9)
    #if the number is less than 9, respond with "World" and status 200
    if num < 9:
        response = "World"
        status = 200
    #else, respond with a failure message and status 500
    else:
        response = "Something went wrong"
        status = 500
    
    #JSON
    #from flask import make_response, jsonify
    #return make_response(jsonify({'response': response}), status)
    
    #Text
    return Response(response=response, status=status, mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5031)