const assert = require('assert');
const fs = require('fs');
let path, str;

// beforeEach(callback) - callback is run before each test
// afterEach(callback) - callback is run after each test
// before(callback) - callback is run before the first test
// after(callback) - callback is run after the last test

describe('appendFileSync', () => {

    before(() => {
        path = './message.txt';
    });

    afterEach(() => {
        fs.unlinkSync(path);
    });

    it('writes a string to text file at given path name', () => {

        // Setup
        str = 'Hello Node.js';

        // Exercise: write to file
        fs.appendFileSync(path, str);

        // Verify: compare file contents to string
        const contents = fs.readFileSync(path);
        assert.equal(contents.toString(), str);

    });

    it('writes an empty string to text file at given path name', () => {

        // Setup
        str = '';

        // Exercise: write to file
        fs.appendFileSync(path, str);

        // Verify: compare file contents to string
        const contents = fs.readFileSync(path);
        assert.equal(contents.toString(), str);
    });
});
