// Don't change this part:
let dogTup: [string, string, string, string] = ['dog', 'brown fur', 'curly tail', 'sad eyes'];

// Your code goes here:
const myArr = dogTup.concat(["droopy ears"])

// myArr is not a tuple but an array.
myArr[50] = "not a dog";

console.log(myArr);
