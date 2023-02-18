const fs = require('fs');
const file = './data.txt';

// This is a pure function because it always returns the same output given the same input.
const capitalizeMessage = (message) => {
    return message.toUpperCase();
}

// This line is not part of the function, it is just reading a file and storing the contents in the message variable.
const message = fs.readFileSync(file, 'utf8');

// This line is also not part of the function, it is just calling the capitalizeMessage function and printing the output to the console.
console.log(capitalizeMessage(message));
