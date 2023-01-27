# Uniform Resource Locator (URL)


* Used to access resouces over HTTP

## Structure

http://admin:password@inlanefreight.com:80/dashboard.php?login=true#status

| Component    | Example           | Description                                                                                                                              |
|:-------------|:------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| Scheme       | http://https://   | Identifies protocols being access by the Client,                                                                                         |
| User info    | admin:password@   | Used to authenticate the host                                                                                                            |
| Host         | inlanefreight.com | Signifies the resource location                                                                                                          |
| Port         | :80               | Default port is 80, https default to 443                                                                                                 |
| Path         | /dashboard.php    | Points to resource being access, default is index                                                                                        |
| Query String | ?login=true       | The query string starts with a question mark. It consists of a parameter and value. Multiple Query can be separated by an ampersand (&) |
| Fragments    | #status           | Process by browser to access sections of web page.                                                                                       |



