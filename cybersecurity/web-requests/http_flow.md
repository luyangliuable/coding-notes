# HTTP Flow

![Alt Text](https://academy.hackthebox.com/storage/modules/35/HTTP_Flow.png )

1. When user enters url into browser, it sends a request to a **DNS** (Domain Name Resolution).
2. The DNS looks up the IP address for the url and returns it. Otherwise servers cannot communicate without an IP address.
  * Our browsers usually first look up records in the local '/etc/hosts' file, and if the requested domain does not exist within it, then they would contact other DNS servers. We can use the '/etc/hosts' to manually add records to for DNS resolution, by adding the IP followed by the domain name.
3. The browsers sends GET request to IP address at default (:80) HTTP port asking for root path ( / ).
4. The contents of index.html are read and returned by the web server as an HTTP response with an status code (e.g. 200 OK).
5. Web browser (client) renders contents and presents to the user.
