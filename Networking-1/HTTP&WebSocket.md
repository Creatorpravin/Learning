# What is web socket and how it is different from the HTTP?

 * HTTP and WebSocket both are communication protocols used in client-server communication. 

 **HTTP protocol:** HTTP is unidirectional where the client sends the request and the server sends the response.

 * HTTP message information encoded in ASCII, each HTTP request message composed HTTP protocol version(HTTP/1.1, HTTP/2), HTTP methods (GET/POST etc.), HTTP headers (content type, content length), host information, etc. and the body which contain the actual message which is being transferred to the server. 
![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20191203183429/HTTP-Connection.png)

**WebSocket:** WebSocket is bidirectional, a full-duplex protocol that is used in the same scenario of client-server communication, unlike HTTP it starts from ws:// or wss://. 
 
 * It is a stateful protocol, which means the connection between client and server will keep alive until it is terminated by either party (client or server). 
  
  * after closing the connection by either of the client and server, the connection is terminated from both the end. 

![alt](https://media.geeksforgeeks.org/wp-content/uploads/20191203183648/WebSocket-Connection.png)

# Real time web application

* Chat application: Chat application uses WebSocket to establish the connection only once for exchange, publishing and broadcasting the message among the subscriber. it reuses the same WebSocket connection, for sending and receiving the message and one to one message transfer.

* Gaming application: In a Gaming application, you might focus on that, data is continuously receiving by the server and without refreshing the UI, it will take effect on the screen, UI gets automatically refreshed without even establishing the new connection, so it is very helpful in a Gaming application.
