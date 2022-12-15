# Client Url cURL
* cURL (client URL) is a command-line tool and library that primarily supports HTTP along with many other protocols.

* Good choice for scripts as well as automation.

* Essential for sending various types of web requests from the command line, which is necessary for many types of web penetration tests.

## cURL and HTTPS
cURL should automatically handle all HTTPS communication standards and perform a secure handshake and then encrypt and decrypt data automatically.

* If we ever contact a website with an invalid SSL certificate or an outdated one, then cURL by default would not proceed with the communication to protect against the earlier mentioned MITM attacks

* Ignore SSL certicate
```bash
curl -k
```


## cURL and view HTTP Response body

```bash
curl inlanefreight.com -v
```

* Even more verbose input
```bash
curl inlanefreight.com -vvv
```

## Curl Cheat Sheet

| Command                                                                                                        | Description                                          |
|:---------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------|
| curl -h                                                                                                        | cURL help menu                                       |
| curl google.com                                                                                                | Basic GET request                                    |
| curl -s -O google.com/index.com                                                                                | Download file                                        |
| curl -k https://inlanefreight.com                                                                              | Skip HTTPS (SSL) certificate validation              |
| curl inlanefreight.com -v                                                                                      | Print full HTTP request/response details             |
| curl -I https://www.inlanefreight.com                                                                          | curl -I https://www.inlanefreight.com                |
| curl -i https://www.inlanefreight.com                                                                          | Print response headers and response body             |
| curl https://www.inlanefreight.com -A 'Mozilla/5.0'                                                            | Set User-Agent header                                |
| curl -u admin:admin http://<SERVER_IP>:<PORT>/                                                                 | Set HTTP basic authorization credentials             |
|                                                                                                                |                                                      |
| curl http://admin:admin@<SERVER_IP>:<PORT>/                                                                    | Pass HTTP basic authorization credentials in the URL |
| curl -H 'Authorization: Basic YWRtaW46YWRtaW4=' http://<SERVER_IP>:<PORT>/                                     | Set request header                                   |
| curl 'http://<SERVER_IP>:<PORT>/search.php?search=le'                                                          | Pass GET parameters                                  |
| curl -X POST -d 'username=admin&password=admin' http://<SERVER_IP>:<PORT>/                                     | Send POST request with POST data                     |
| curl -b 'PHPSESSID=c1nsa6op7vtk7kdis7bcnbadf1' http://<SERVER_IP>:<PORT>/                                      | Set request cookies                                  |
| curl -X POST -d '{"search":"london"}' -H 'Content-Type: application/json' http://<SERVER_IP>:<PORT>/search.php | Send POST request with JSON data                     |
| curl https://www.inlanefreight.com -A 'Mozilla/5.0'                                                            | Set custom User-Agent                                |



### APIs
| Command                                                                                                                                      | Description      |
|:---------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| curl http://<SERVER_IP>:<PORT>/api.php/city/london                                                                                           | Read entry       |
| curl -s http://<SERVER_IP>:<PORT>/api.php/city/ `pipe symbol` jq                                                                             | Read all entries |
| curl -X POST http://<SERVER_IP>:<PORT>/api.php/city/ -d '{"city_name":"HTB_City", "country_name":"HTB"}' -H 'Content-Type: application/json' | Download file    |
