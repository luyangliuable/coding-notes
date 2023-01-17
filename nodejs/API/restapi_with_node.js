const http = require('http');
const url = require('url');
const fs = require('fs');

/**
 * @module  createServer
 * @desc  creates a simple REST API server
 */
const server = http.createServer((req, res) => {
    /**
     * @desc Parse the incoming request's URL
     * @type {url.UrlWithParsedQuery}
     */
    const parsedUrl = url.parse(req.url, true);

    /**
     * @desc Get the pathname from the parsed URL
     * @type {string}
     */
    const path = parsedUrl.pathname;

    /**
     * @desc Trim any leading or trailing slashes from the path
     * @type {string}
     */
    const trimmedPath = path.replace(/^\/+|\/+$/g, '');

    /**
     * @desc Get the method of the request and convert it to lowercase
     * @type {string}
     */
    const method = req.method.toLowerCase();

    if (method === 'get' && trimmedPath === 'users') {
        /**
         * @desc If a GET request is made to the /users endpoint,
         *  set the content type to JSON and return a response of all users
         */
        res.setHeader('Content-Type', 'application/json');
        res.writeHead(200);
        res.end(JSON.stringify({ message: 'Retrieving all users' }));
    } else if (method === 'get' && trimmedPath === 'users/1') {
        res.setHeader('Content-Type', 'application/json');
        res.writeHead(200);
        res.end(JSON.stringify({ message: 'Retrieving user with ID 1' }));
    } else if (method === 'post' && trimmedPath === 'users') {

        /**
         * @desc Initializing an empty variable to hold the incoming request body
         */
        let body = '';

        req.on('data', data => {
            /**
             * @desc Appending each chunk of data to the body variable
             */
            body += data;
        });

        req.on('end', () => {
            /**
             * @desc Setting the header of the response to 'application/json'
             * and returning a 200 status code indicating success
             * and returning a json message that contains the request body
             */
            res.setHeader('Content-Type', 'application/json');
            res.writeHead(200);
            res.end(JSON.stringify({ message: 'Creating new user', body: JSON.parse(body) }));
        });
    } else {
        /**
         * @desc If the request method and endpoint don't match the specified routes
         *  it will return a 404 status code indicating that the requested resource could not be found
         */
        res.writeHead(404);
        res.end();
    }
});


/**
 * @constant {number} PORT - The port number to listen on
 */
const PORT = 3000;


/**
 * @desc Start listening on the specified port, and log a message when the server has started
 */
server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
