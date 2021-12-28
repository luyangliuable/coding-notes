// Require modules in:

let Dog = require('./dog.js');
let Cat = require('./cat.js');


let fight = (dog, cat) => {
    if (dog.toothStrength > cat.clawStrength) {
        console.log(`${dog.name} wins!`);
    }
    else if (dog.toothStrength < cat.clawStrength) {
        console.log(`${cat.name} wins!`);
    }
    else {
        console.log(`${dog.name} and ${cat.name} are equally skilled fighters!`);

    }
}

const myDog = new Dog('Rex', Math.random());
const myCat = new Cat('Tabby', Math.random());

fight(myDog, myCat);
