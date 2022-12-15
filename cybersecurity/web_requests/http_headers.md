# HTTP Headers

* Allow information to be passed between client and server.

## Types of Headers

1 General Headers
2 Entity Headers
3 Request Headers
4 Response Headers
5 Security Headers


## General Headers
* Used to describe context and message rather than its contents. Meta information.

| Header     | Example                             | Description                                                                                                                                       |
|:-----------|:------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| Date       | Date: Wed, 16 Feb 2022 10:38:44 GMT | Holds date and time message originated from                                                                                                       |
| Connection | Connection: close                   | Specify if the current network connection should stay alive after the request finishes. Commonly values for this header are close and keep-alive. |


## Entity Headers
These headers are used to describe the content (entity) transferred by a message. They are usually found in responses and POST or PUT requests.


| Header           | Example                     | Description                                                                                                                        |
|:-----------------|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| Content-Type     | Content-Type: text/html     | Used to describe the type of resource being transferred                                                                            |
| Media-Type       | Media-Type: application/pdf | The media-type is similar to Content-Type, and describes the data being transferred.                                               |
| Boundary         | boundary="b4e4fbd93540"     | Acts as a maker to separate content when there is more than one in the same message.                                               |
| Content-Length   | Content-Length: 385         | Holds the size of the entity being passed.                                                                                         |
| Content-Encoding | Content-Encoding: gzip      | Data can undergo multiple transformations before being passed. Large amounts of data can be compressed to reduce the message size. |



## Request Headers
The client sends Request Headers in an HTTP transaction. These headers are used in an HTTP request and do not relate to the content of the message. The following headers are commonly seen in HTTP requests.

| Header        | Example                               | Description                                                                                                                                                 |
|:--------------|:--------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Host          | Host: www.inlanefreight.com           | Used to specify the host being queried for the resource.                                                                                                    |
| User-Agent    | User-Agent	User-Agent: curl/7.77.0 | The User-Agent header is used to describe the client requesting resources (resources, operating system).                                                    |
| Referer       | Referer: http://www.google.com        | Denotes where the current request is coming from. The previous web page                                                                                     |
| Accept        | Accept: application/json              | The Accept header describes which media types the client can understand.                                                                                    |
| Cookie        | Cookie: PHPSESSID=b4e4fbd93540        | Contains cookie-value pairs in the format name=value. A cookie is a piece of data stored on the client-side and on the server, which acts as an identifier. |
| Authorization | Authorization: BASIC cGFzc3dvcmQK     | Another method for the server to identify clients.                                                                                                          |

## Response Headers

| Header           | Example                                   | Description                                                                                     |
|:-----------------|:------------------------------------------|:------------------------------------------------------------------------------------------------|
| Server           | Server: Apache/2.2.14 (Win32)             | Contains information about the HTTP server, which processed the request.                        |
| Set-Cookie       | Set-Cookie: PHPSESSID=b4e4fbd93540        | Contains the cookies needed for client identification                                           |
| WWW-Authenticate | WWW-Authenticate: BASIC realm="localhost" | Notifies the client about the type of authentication required to access the requested resource. |

## Security Headers

With the increase in the variety of browsers and web-based attacks, defining certain headers that enhanced security was necessary. HTTP Security headers are a class of response headers used to specify certain rules and policies to be followed by the browser while accessing the website.

| Header                    | Example                                     | Description                                                                                                                                                                                                                                                                                   |
|:--------------------------|:--------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Content-Security-Policy   | Content-Security-Policy: script-src 'self'  | Dictates the website's policy towards externally injected resources. This could be JavaScript code as well as script resources. This header instructs the browser to accept resources only from certain trusted domains, hence preventing attacks such as Cross-site scripting (XSS).         |
| Strict-Transport-Security | Strict-Transport-Security: max-age=31536000 | Prevents the browser from accessing the website over the plaintext HTTP protocol, and forces all communication to be carried over the secure HTTPS protocol. This prevents attackers from sniffing web traffic and accessing protected information such as passwords or other sensitive data. |
| Referrer-Policy           | Referrer-Policy: origin                     | Dictates whether the browser should include the value specified via the Referer header or not. It can help in avoiding disclosing sensitive URLs and information while browsing the website.                                                                                                  |







