#Service A
from flask import Flask, request
import requests

#ip address of Service B
#ip_service_b = "147.102.37.77"
ip_service_b = "0.0.0.0"

#flask service
app = Flask(__name__)

@app.route("/api/service_a", methods=['GET', 'POST'])
def service_a():
    #send a request to Service B with the message "Hello"
    message = "Hello"
    response = requests.get(f'http://{ip_service_b}:5031/api/service_b?message={message}')
    #print the response from Service B
    
    #JSON
    #print(response.json())
    #return response.json()
    
    #Text
    print(response.text)
    #print("response status: ", response.status_code)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5030)