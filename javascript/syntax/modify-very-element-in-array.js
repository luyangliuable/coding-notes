// Write your code here:


const convertToBaby = (arr) => {
    for (var i = 0; i < arr.length; i++) {
        arr[i] = `baby ${arr[i]}`;
    };

    return arr;
};





// When you're ready to test your code, uncomment the below and run:

const animals = ['panda', 'turtle', 'giraffe', 'hippo', 'sloth', 'human'];

console.log(convertToBaby(animals));
