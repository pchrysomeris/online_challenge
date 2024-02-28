# online_challenge

The objective is to create 2 services with the following communication behaviour:
1. Service A sends to Service B a request with the message "Hello".
2. Service B:
   - has 90% chance to successfully respond with message "World".
   - has 10% chance to respond with a failure message.
     
The messages sent and received may change in the future.
The services may run in separate computers.

## Steps:
1. start service A: python3 service_a.py
2. start service B: python3 service_b.py
3. start communication: curl -X 'POST' 'http://localhost:5030/api/service_a'
