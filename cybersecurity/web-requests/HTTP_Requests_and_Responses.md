# HTTP Request


## Structure

```bash
GET /users/login/html HTTP/1.1
```

| Field   | Example           | Description                                                                                                   |
|:--------|:------------------|:--------------------------------------------------------------------------------------------------------------|
| Method  | GET               | The HTTP method or verb which specifies the type of action to perform                                         |
| Path    | /users/login/html | The path to the resource being accessed. This field can also be suffixed with a query string (?username=user) |
| Version | HTTP/1.1          | The third and final field  is used to denote the HTTP version                                                 |

## HTTP Response

```csv
HTTP/1.1 200 OK
Date: Mon, 13 Jul 2020 10:46:21 GMT
Server: Apache/2.4.41 (ubuntu)
Set-Cookie: PHPSESSID=mwewjnewjqenkqw; path=/
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache., must-revalidate
Pragma: no-cache
Vary: Accept-Encoding
Content-length: 964
Connection: close
Content-Type: text/html; charset=UTF-8
```

* The first line of an HTTP response contains two fields separated by spaces. The first being the HTTP version (e.g. HTTP/1.1), and the second denotes the HTTP response code (e.g. 200 OK).

## Browser Devtools
These tools can be a vital asset in any web assessment we perform, as a browser (and its DevTools) are among the assets we are most likely to have in every web assessment exercise.


Www can use Filter URLs to search for a specific request, in case the website loads too many to go through.
