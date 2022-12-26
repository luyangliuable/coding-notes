const assert = require('assert');
const fs = require('fs');
let path, str;

// Running multiple tests can introduce issues if the tests make changes to the testing environment: changes to the environment in one test might affect the next test. Some common changes to an environment include:
// altering files and directory structure
// changing read and write permissions on a file
// editing records in a database

describe('appendFileSync', () => {
    it('creates a new file with a string of text', () => {

        // Setup
        path = './message.txt';
        str = 'Hello Node.js';

        // Exercise: write to file
        fs.appendFileSync(path, str);

        // Verify: compare file contents to string
        const contents = fs.readFileSync(path);
        assert.equal(contents.toString(), str);

        // Teardown: restore file
        fs.unlinkSync(path);
    });

    it('creates a new file with a string of text', () => {

        // Setup
        path = './message.txt';
        str = '';

        // Exercise: write to file
        fs.appendFileSync(path, str);

        // Verify: compare file contents to string
        const contents = fs.readFileSync(path);
        assert.equal(contents.toString(), str);

        // Teardown: restore file
        fs.unlinkSync(path);
    });
});
