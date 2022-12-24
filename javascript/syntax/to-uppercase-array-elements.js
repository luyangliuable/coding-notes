// Write your code here:

const shoutGreetings = (arr) => {
    for (let i = 0; i < arr.length; i++)
        arr[i] = `${ arr[i].toUpperCase() }!`;

    return arr;
};


// Feel free to uncomment out the code below to test your function!

const greetings = ['hello', 'hi', 'heya', 'oi', 'hey', 'yo'];

console.log(shoutGreetings(greetings));
// Should print [ 'HELLO!', 'HI!', 'HEYA!', 'OI!', 'HEY!', 'YO!' ]
