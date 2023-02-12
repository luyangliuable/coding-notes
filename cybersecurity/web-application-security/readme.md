# Web Application Safety

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Web Application Safety](#web-application-safety)
    - [Basics Of Web](#basics-of-web)
        - [Web and HTTP (HTTPS)](#web-and-http-https)
        - [HTTP is Stateless](#http-is-stateless)
        - [URL](#url)
        - [Web Client and Server](#web-client-and-server)
        - [General goals of web security](#general-goals-of-web-security)
    - [Significance Of Web Security](#significance-of-web-security)
    - [Web Security Threads](#web-security-threads)
        - [Chrome Security Architecture](#chrome-security-architecture)
    - [OS vs Browser](#os-vs-browser)
    - [Maintaining State](#maintaining-state)
    - [Security of web cookies](#security-of-web-cookies)
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


### HTTP is Stateless
* Lifetime of HTTP:
  1. Client **connects to the server**
  2. Client **issues a request**
  3. Server **responds**
  4. Client **issues a request for something in the response**
  5. Repeat...
  5. Client **disconnects**
* **HTTP won't remember** the same user again

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


## Web Security Threats
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
* Principles:
    * **Isolation**
        * **Separate** web application, browser components from each other.
    * Principle of **Least Previlage**
        * Runs each component with the bare minimal privileges
        * Only if they need it
        * Minimize damage
```
browser process   GPU singleton  Renderer Sandbox   Renderer Sandbox
  +--------+         -----              -------        -------
  |        |  <---> |     |  <-------> |       |      |       |
  |        |         -----             |       |      |       |
  |        | <-----------------------> |       |      |       |
  |        |                            -------        -------
  |        |                             ^                  ^
  |        |                             | plugin processes |
  |        |                             v                  v
  |        |                           -------------------------
  |        |                          | ----   -----   -------  |
  |        |<------------------------>||java| |flash| |acrobat| |    <----->
  |        |                          | ----   -----   -------  | (IPC Channel)
  |        |                           -------------------------
  +--------+
```

* Browser sandbox
    * **Run remote web applications** safely
    * **Limited to access** to OS, network, and browser data
* Approach
    * **Isolate sites** in different security context
    * Browser **manages resources** like OS

## OS vs Browser
|                 | Operating System                    | Web Browser                                                             |
|:---------------:|:-----------------------------------:|:-----------------------------------------------------------------------:|
| Primitives      | Processes, system calls, filesystem | Frames, Content (javascript), DOM, cookies and localstorage             |
| Principles      | Users: Discretionary control        | "Origins": Mandatory access control                                     |
| Vulnerabilities | Buffer overflow, root exploit       | cross-site scripting, cross-site request forgery, cache history attacks |

## Maintaining State
```
      Client                             Server
 ------------------                 -----------------
|                  | HTTP Request  |                 |
|                  |-------------->|                 |
|     Browser      |               |    Web Server   |
|    ---------     | HTTP Response |    --------     |
|   |  State  |    |<--------------|   | State  |    |
|    ---------     |               |    --------     |
 ------------------                 -----------------
```

* A web application often uses **ephemeral** state to store information that is used during a specific user session.
  * This state is typically used for intermediate results during server processing, rather than long-term data storage (which is not ACID compliant).
* This ephemeral state is then sent to the client and returned in subsequent requests.
* There are two main types of ephemeral state: **hidden fields** and **cookies**.
    * Hidden fields: store **data within an HTML form**
    * Cookies: store data **in the browser**.

## Capabilities
* Large random identifier to index trusted state.
* Web applications maintain both **ephemeral** and **trusted states**.
    * These intermediate results are **sent to the client** in the form of capabilities.
    * The **client references these capabilities** in subsequent responses to the server, **allowing for the continued processing and maintenance** of the trusted state on the server side.

* Capabilities should be **large, random to prevent unauthorized access**.
    * Difficult to guess

## Using capabilities
* Option 1: With hidden fields
    * Old and tedious way
* Option 2: Cookies



## Cookies
  * Are Key-value pairs
  * e.g. Set-Cookie:edition=us;expires=Wed,27-Jan-2022 16:29:21 GMT;path=/;domain=.zdnet.com
    * Store value **us** under the key **edition**
    * Expires 27-Jan-2022
    * Only readable by any domain ending in zdnet.com
    * Send the cookie with any future requests to <domain>/<path>

### Purpose of Cookies
* Session Identifier
  * After a user has authenticated, a unique session identifier is stored in a cookie
  * Subsequent actions by the user on the website can **reference this session identifier instead of requiring re-authentication**
* Personalization
  * Anonymous users can customize the site by **storing preferences**, such as font choice, in a cookie for easy retrieval during future visits.
* **Tracking users**
  * Advertisers want to know your behaviour
  * Ideally build a **profile across different websites**
  * Visit the Apple Store, then see iPad ads on Amazon?
  * How can site B know what you did on site A?

### Statefulness with cookies
* Cookie:
  * Server generates a large random number ( compability ) to denote state.
  * Is sent to the client and stored by the client.
  * Client returns the cookie with subsequent requests **to the same server** allowing server to access the associated state.


## Security of web cookies
* Web based state using hidden fields and cookies
* Session hijacking
* Session management


## How browser renders a page
todo

## Security Of Web Cookies
* Session cookies are, once again, capabilities/tokens
  * User gives this to a site denoting privileges of the user that established that session

* Stealing a cookie may allow an attacker to impersonate a user
  * Actions that will seem to be due to that user
  * Permitting theft or corruption of sensitive data

### Session Hijacking
* Compromise the server or user's machine
  * Then predict it based on information you know
* Via Networks attacks
  * Sniff the network
  * DNS cache poisoning
    * Tricks the user into thinking you are on a certain site
    * The user will send you the cookie
* Countermeasures
  * Avoid theft by guessing; cookies should be
    * Randomly chosen
    * Sufficiently long
  * Require separate, correlating information
    * Only accept requests due to legitimate interactions with web site (e.g., from clicking links)

### Mitigating Session Hijacking
* Normally only one cookie (known as auth_token) to validate user.
    * Does not change from one login to the next
    * Does not become invalid when the user logs out
    * So stealing this cookie once, you can log in as many times as you want until passwd change

* Defense:
    * Timeout session IDs and delete them once session ends.


### Non-defense
* False positives: Store client IP address for session; if session changes to a different address, must be a session hijack
  * Problem, false positives: IP addresses change!
  * Moving between WiFi network and 3G network
  * DHCP renegotiation

* False negatives: could be hijacked to different machine with same IP address
  * Both requests via same NAT box

### Session mananagent
• Generate new session ID on login (do not reuse old ones)
• Use cookies for storing session id
• Set session timeout and provide logout possibility
• Consider enabling “same IP” policy (not always possible)
• User agent (browser version)
• Require https (at least for the login / password transfer)


## Common Threats at Server Side
* Attacker interacts as web app client with server web application
* Goal: Inject attacker code to modify web app behavior on server
* e.g. SQL Code Injection

```
 ------------            ------------            ------------
|            |--------->|            |--------->|            |
| Client     |          |  Server    |          |  Database  |
|            |<---------|            |<---------|            |
 ------------    HTTP   ------------      SQL    ------------
  Client                  Server script      Database interpretor (MYSQL)
  Web                     (PHP)
  Browser
  (HTML)
```
