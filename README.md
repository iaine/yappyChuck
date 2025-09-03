# yappyChuck

Yet another Python link to Chuck using Open SOund Control (OSC). 

The library has two classes: Server and Client

Server stops and starts a server, if you want to run one. 

Client sends messages via OSC to an address, defined as part of initialisation. 

send_once sends a message and does not expect a reply. 

request_response sends a message and waits for a response. 

These are based on simple messaging patterns that might be extended through use. 
