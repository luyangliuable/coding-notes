#

const whatsMyAge = () : number => {
    return Math.floor(Math.random() * 120 + 1);
};

console.log(`I am ${whatsMyAge()} years old today!`);
