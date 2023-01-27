# Hypertext Transfer Protocol Secure (HTTPS)

* Everything being transfered with HTTP is clear text so it is not secure and can be subjected to attacks.

* In HTTPs all communications are transferred in an encrypted format,

* a third party does intercept the request, they would not be able to extract the data out of it.

*  HTTPS has become the mainstream scheme for websites on the internet, and HTTP is being phased out, and soon most web browsers will not allow visiting HTTP websites.

* The request may still reveal the visited URL if it contacted a clear-text DNS server.

* It is recommended to utilize encrypted DNS servers (e.g. 8.8.8.8 or 1.2.3.4), or utilize a VPN service to ensure all traffic is properly encrypted.

# HTTPS Flow
1. If we type http:// instead of https:// to visit a website that enforces HTTPS, the browser attempts to resolve the domain and redirects the user to the webserver hosting the target website.

2. A request is sent to port 80 first, which is the unencrypted HTTP protocol. The server detects thisand redirects the client to secure HTTPS port 443 instead. This is done via the 301 Moved Permanently response code, which we will discuss in an upcoming section.

3. The client (web browser) sends a "client hello" packet, giving information about itself.

4. After this, the server replies with "server hello", followed by a key exchange to exchange SSL certificates.

5. The client verifies the key/certificate and sends one of its own. After this, an encrypted handshake is initiated to confirm whether the encryption and transfer are working correctly.
