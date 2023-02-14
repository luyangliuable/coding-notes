# Capabilities

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Capabilities](#capabilities)
    - [Using capabilities](#using-capabilities)
    - [Cookies](#cookies)
        - [Purpose of Cookies](#purpose-of-cookies)
        - [Statefulness with cookies](#statefulness-with-cookies)
    - [Security of web cookies](#security-of-web-cookies)
    - [How browser renders a page](#how-browser-renders-a-page)
    - [Security Of Web Cookies](#security-of-web-cookies)
        - [Session Hijacking](#session-hijacking)
        - [Mitigating Session Hijacking](#mitigating-session-hijacking)
        - [Non-defense](#non-defense)
        - [Session mananagent](#session-mananagent)

<!-- markdown-toc end -->



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

