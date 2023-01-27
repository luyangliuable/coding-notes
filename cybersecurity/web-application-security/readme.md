# Web Application Safety

## Basics Of Web

### Web and HTTP (HTTPS)
* Requests (user clicks) contain:
    * The **URL** of the resource the client wishes to obtain.
    * Header describing what the browser can do.

* [More info](../web-requests/HTTP_Requests_and_Responses.md)

### URL
* http://stanford.edu:81/class?name=cs155#homework

```
 -----------------------------------------------------------------
| http:// | stanford.edu | :81 | /class | ?name=cs155 | #homework |
 -----------------------------------------------------------------
 |        |              |     |        |             |           |
 |        |              |     |        |             |           |
  -------- -------------- ----- -------- ------------- -----------
  protocol    hostname     port   path       query       fragment
```

* Special character are encoded as hex:
    * E.g. %0A = newline, %20 or += space, %2B =+

* HTTP Requests
    * A request line (method, file path, HTTP version)
        * GET method: asks the server to send a resource.
        * POST method: sends output data to the server.
    * A series of HTTP headers or header fields.
    * A message body if required.

```
 --------------------------------------------------------------------------
| GET /index.html HTTP/1.1                                                 |
| Acccept: image/gif, image/x-bitmap, image/jpeg, */* Accept-Language: en  |
| Connection: Keep-Alive                                                   |
| User-Agent: Mozilla/1.22 (compible; MSIE 2.0; Window 95)                 |
| Host: www.example.com                                                    |
| Referer: http://www.google.com?q=dingbats                                |
 --------------------------------------------------------------------------
```

* HTTP Response
    * A status line (HTTP version, status code, reason phrase)
        * 2xx: Success
        * 4xx: Client Error (e.g. 404 Not Found)
        * 5xx: Server Error (e.g. 503 Service Unavailable)
    * A series of HTTP headers, or headers field
        * Cookies: Represent state the server would like the browser to store on its behalf
    * A message body

```
HTTP/1.0 200 OK
Date: Sun, 21 Apr 1996 02:20:42 GMT
Server: Microsoft-Internet-Information-Server/5.0
Connection: keep-alive
Content-Type: text/html
Last-Modified: Thu, 18 Apr 1997 17 17:39:05 GMT
Set Cookie: ...
Content-Length: 2543

<HTML>...</HTML>
```

### Web Client and Server

```
            Client                              Server

+----------------------------+      +----------------------------+
| +------------------------+ |      | +------------------------+ |
| |                        | |      | |                        | |
| |         Browser        |<-------->|       Web Server       | |
| |                        | |      | |                        | |
| +------------------------+ |      | +------------------------+ |
|             ^              |      |             ^              |
|             |              |<---->|             |              |
|             v              |      |             v              |
|   +--------------------+   |      |   +--------------------+   |
|   |                    |   |      |   |                    |   |
|   |    Private Data    |   |      |   |      Database      |   |
|   |                    |   |      |   |                    |   |
|   +--------------------+   |      |   +--------------------+   |
|                            |      |                            |
+----------------------------+      +----------------------------+
```

## Significance Of Web Security And Threats In Web

## Security Of Web Cookies

### Session Hijacking
