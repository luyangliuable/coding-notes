// Write your code here:

function findMyKeys(arr) {
    for (let i = 0; i < arr.length; i++) {
        if ( arr[i] === 'keys') {
            return i;
        }
    }
    return -1;
}

// Feel free to comment out the code below to test your function

const randomStuff = ['credit card', 'screwdriver', 'receipt', 'gum', 'keys', 'used gum', 'plastic spoon'];

console.log(findMyKeys(randomStuff));
// Should print 4
