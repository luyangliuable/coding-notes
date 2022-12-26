function checkPalindrome(testStr) {
    let reversedStr = '';

    for(let i=testStr.length-1; i >= 0; i--) {
        reversedStr += testStr[i];
    }

    if (testStr === reversedStr) {
        return `The word "${testStr}" is a palindrome!`;
    } else {
        return `The word "${testStr}" is not a palindrome.`;
    }
};

console.log(checkPalindrome('racecar'));

// Generate a random hexadecimal string
const generateBackgroundColor = () => {
    const hexadecimals = '0123456789ABCDEF';
    let randomHexString = '#';
    for (let i = 0; i < 6; i++) {
        const randomHexChar = hexadecimals[Math.floor(Math.random() * hexadecimals.length)];
        randomHexString += randomHexChar;
    };
    return randomHexString;
};

// Grab the element with ID #colorBtn from the DOM
const colorBtn = document.getElementById('colorBtn');

// Change the background color and display the color on the page
const changeColor = () => {
    const randomBackgroundColor = generateBackgroundColor();
    document.body.style.backgroundColor = randomBackgroundColor;
    document.querySelector('#randomColorText').innerHTML = randomBackgroundColor;
}

// Write your event handler here
colorBtn.onclick(() => {
    alert();
    changeColor();
});
