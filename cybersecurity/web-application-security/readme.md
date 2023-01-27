# Web Application Safety

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Web Application Safety](#web-application-safety)
    - [Basics Of Web](#basics-of-web)
        - [Web and HTTP (HTTPS)](#web-and-http-https)
        - [URL](#url)
        - [Web Client and Server](#web-client-and-server)
        - [General goals of web security](#general-goals-of-web-security)
    - [Significance Of Web Security](#significance-of-web-security)
    - [Web Security Threads](#web-security-threads)
    - [How browser renders a page](#how-browser-renders-a-page)
    - [Security Of Web Cookies](#security-of-web-cookies)
        - [Session Hijacking](#session-hijacking)

<!-- markdown-toc end -->

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
* [More info on HTTP Reponse](../web-requests/HTTP_Requests_and_Responses.md)

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

### General goals of web security
* Safely browse the web
    * No stolen information (without user's permission)
    * Site A cannot compromise session at Site B
* Secure web applications
    * Applications delivered over the web should have the **same security properties we require for stand-alone applications**
    * HTTPS - http over SSL (Secure Socket Layer)
        * **Encrypts** for the browser-server traffic
        * **Prevents** eavesdropping, and main-in-the-middle attack (if certification verification is done correctly)
        * Helps user **ensure authenticity** of the server.


## Significance Of Web Security
* Web apps are:
    * **easy to target** for attackers
        * **finding** vulnerable sites, **automating** and **scaling** attacks.
    * **Not easy to develop well** and securely.
    * Often vulnerable **making server, database, internal network, and data insecure**.


## Web Security Threads
* **Information disclosure** (lost data confidentiality)
    * business secrets
    * financial information
    * medical data
    * government documents
* **tampering** (lost data integerity)
* **spoofing**/elevation of privilege/unauthorized access
    * Functionality of the system abused.
* Denial of Service (DDOS)
    * Loss of avalaiblity or functionality (and revenue)
* **Attacker breach firewall** (foot in the door)
* Web defacement (clients and stakeholders)
    * loss of reputation
    * fear, uncertainty, doubt

### Chrome Security Architecture
```
browser process   GPU singleton  Renderer Sandbox   Renderer Sandbox
  +--------+         -----              -------        -------
  |        |  <---> |     |  <-------> |       |      |       |
  |        |         -----             |       |      |       |
  |        | <-----------------------> |       |      |       |
  |        |                            -------        -------
  |        |                               ^              ^
  |        |                               |              |
  |        |                               v              v
  |        |                           -------------------------
  |        |                          | ----   -----   -------  |
  |        |<------------------------>||java| |flash| |acrobat| |
  |        |                          | ----   -----   -------  |
  |        |                           -------------------------
  +--------+
```

## How browser renders a page
todo

## Security Of Web Cookies

### Session Hijacking
