# Objects

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Objects](#objects)
    - [Accessing objects bracket notation](#accessing-objects-bracket-notation)
    - [Objects Property Assignment](#objects-property-assignment)
        - [**Delete** operator](#delete-operator)
    - [Methods in objects](#methods-in-objects)
    - [Nested objects](#nested-objects)
    - [Pass By Reference](#pass-by-reference)
    - [Looping Through Objects](#looping-through-objects)
    - [This keyword](#this-keyword)
    - [Arrow Functions and this](#arrow-functions-and-this)
    - [Privacy](#privacy)
    - [Getters](#getters)
    - [Setters](#setters)

<!-- markdown-toc end -->


## Accessing objects bracket notation


With bracket notation you can **also use a variable inside the brackets to select the keys of an object**. This can be especially helpful when working with functions:

```javascript
let returnAnyProp = (objectName, propName) => objectName[propName];
returnAnyProp(spaceship, 'homePlanet'); // Returns 'Earth'
```

If we tried to write our returnAnyProp() function with dot notation (objectName.propName) the computer would look for a key of 'propName' on our object and not the value of the propName parameter. Let’s get some practice using bracket notation to access properties!

## Objects Property Assignment
One of two things can happen with property assignment:

* If the property already exists on the object, whatever value it held before will be replaced with the newly assigned value.
* If there was no property with that name, a new property will be added to the object.

```javascript
const spaceship = {type: 'shuttle'};

spaceship = {type: 'alien'}; // TypeError: Assignment to constant variable.
spaceship.type = 'alien'; // Changes the value of the type property
spaceship.speed = 'Mach 5'; // Creates a new key of 'speed' with a value of 'Mach 5'
```
### **Delete** operator

```javascript
const spaceship = {
  'Fuel Type': 'Turbo Fuel',
  homePlanet: 'Earth',
  mission: 'Explore the universe'
};

delete spaceship.mission;  // Removes the mission property
```

## Methods in objects


```javascript
const alienShip = {
  invade: function () {
    console.log('Hello! We have come to dominate your planet. Instead of Earth, it shall be called New Xaculon.')
  }
};
```
*With the new method syntax introduced in ES6 we can omit the colon and the function keyword.*

```javascript
const alienShip = {
  invade () {
    console.log('Hello! We have come to dominate your planet. Instead of Earth, it shall be called New Xaculon.')
  }
};
```

**Calling a method()**
```javascript
alienShip.invade(); // Prints 'Hello! We have come to dominate your planet. Instead of Earth, it shall be called New Xaculon.'
```


## Nested objects

```javascript
const spaceship = {
     telescope: {
        yearBuilt: 2018,
        model: '91031-XLT',
        focalLength: 2032
     },
    crew: {
        captain: {
            name: 'Sandra',
            degree: 'Computer Engineering',
            encourageTeam() { console.log('We got this!') }
         }
    },
    engine: {
        model: 'Nimbus2000'
     },
     nanoelectronics: {
         computer: {
            terabytes: 100,
            monitors: 'HD'
         },
        'back-up': {
           battery: 'Lithium',
           terabytes: 50
         }
    }
};
```

**Chain operators to access nested properties:**

```javascript
spaceship.nanoelectronics['back-up'].battery; // Returns 'Lithium'
```
## Pass By Reference
Objects are passed by reference. This means when we pass a variable assigned to an object into a function as an argument, the computer interprets the parameter name as pointing to the space in memory holding that object. As a result, functions which change object properties actually **mutate the object permanently** (even when the object is assigned to a const variable).

```javascript
const spaceship = {
  homePlanet : 'Earth',
  color : 'silver'
};

let paintIt = obj => {
  obj.color = 'glorious gold'
};

paintIt(spaceship);

spaceship.color // Returns 'glorious gold'
```
## Looping Through Objects

```javascript
let spaceship = {
  crew: {
    captain: {
      name: 'Lily',
      degree: 'Computer Engineering',
      cheerTeam() { console.log('You got this!') }
    },
    'chief officer': {
      name: 'Dan',
      degree: 'Aerospace Engineering',
      agree() { console.log('I agree, captain!') }
    },
    medic: {
      name: 'Clementine',
      degree: 'Physics',
      announce() { console.log(`Jets on!`) } },
    translator: {
      name: 'Shauna',
      degree: 'Conservation Science',
      powerFuel() { console.log('The tank is full!') }
    }
  }
};

// for...in
for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`);
}
```

Loops are programming tools that repeat a block of code until a condition is met. We learned how to iterate through arrays using their numerical indexing, but the key-value pairs in objects aren’t ordered! JavaScript has given us alternative solution for iterating through objects with the for...in syntax .

for...in will execute a given block of code for each property in an object.

## This keyword



```javascript
const goat = {
  dietType: 'herbivore',
  makeSound() {
    console.log('baaa');
  },
  diet() {
    console.log(this.dietType);
  }
};

goat.diet();
// Output: herbivore
```

That’s strange, why is dietType not defined even though it’s a property of goat? That’s because **inside the scope of the .diet() method, we don’t automatically have access to other properties of the goat object**.

## Arrow Functions and this

We saw in the previous exercise that for a method, the calling object is the object the method belongs to. If we use the this keyword in a method then the value of this is the calling object. However, it becomes a bit more complicated when we start using arrow functions for methods. Take a look at the example below:

```javascript
const goat = {
  dietType: 'herbivore',

  makeSound() {
    console.log('baaa');
  },

  diet: () => {
    console.log(this.dietType);
  }
};
 
goat.diet(); // Prints undefined
```

In the comment, you can see that goat.diet() would log undefined. So what happened? Notice that the .diet() method is defined using an arrow function.

**Arrow functions inherently bind, or tie, an already defined this value to the function itself that is NOT the calling object.** In the code snippet above, the value of this is the global object, or an object that exists in the global scope, which doesn’t have a dietType property and therefore returns undefined.

## Privacy

```javascript
const bankAccount = {
  _amount: 1000
}
```

In the example above, **the _amount is not intended to be directly manipulated**.

Even so, it is still possible to reassign _amount:

```javascript
bankAccount._amount = 1000000;
```

## Getters


```javascript
const person = {
  _firstName: 'John',
  _lastName: 'Doe',
  get fullName() {
    if (this._firstName && this._lastName){
      return `${this._firstName} ${this._lastName}`;
    } else {
      return 'Missing a first name or a last name.';
    }
  }
}
 
// To call the getter method: 
person.fullName; // 'John Doe'
```

* We use the get keyword followed by a function.
* We use an if...else conditional to check if both _firstName and _lastName exist (by making sure they both return truthy values) and then return a different value depending on the result.
* We can access the calling object’s internal properties using this. In fullName, we’re accessing both this._firstName and this._lastName.
* In the last line we call fullName on person. In general, getter methods do not need to be called with a set of parentheses. Syntactically, it looks like we’re accessing a property.


## Setters

```javascript
const person = {
  _age: 37,
  set age(newAge){
    if (typeof newAge === 'number'){
      this._age = newAge;
    } else {
      console.log('You must assign a number to age');
    }
  }
};
```
Notice that in the example above:

* We can perform a check for what value is being assigned to this._age.
* When we use the setter method, only values that are numbers will reassign this._age
* There are different outputs depending on what values are used to reassign this._age.

**Setters do not need to be called with a set of parenthesis:**

```javascript
person.age = 40;
console.log(person._age); // Logs: 40
person.age = '40'; // Logs: You must assign a number to age
```

## Factory functions

**Factory function is a function that returns an object and can be reused to make multiple object instances.** Factory functions can also have parameters allowing us to customize the object that gets returned.

```javascript
const monsterFactory = (name, age, energySource, catchPhrase) => {
  return { 
    name: name,
    age: age, 
    energySource: energySource,
    scare() {
      console.log(catchPhrase);
    } 
  }
};
```
```javascript
const ghost = monsterFactory('Ghouly', 251, 'ectoplasm', 'BOO!');
ghost.scare(); // 'BOO!'
```

## Destructuring

### Property value shorthand

```javascript
const monsterFactory = (name, age) => {
  return { 
    name,
    age 
  }
};
```
### Destructured Assignment

```javascript
const vampire = {
  name: 'Dracula',
  residence: 'Transylvania',
  preferences: {
    day: 'stay inside',
    night: 'satisfy appetite'
  }
};

const { residence } = vampire; 
console.log(residence); // Prints 'Transylvania'

const { day } = vampire.preferences; 
console.log(day); // Prints 'stay inside'
```


### Built-in Object methods
We can also take advantage of built-in methods for Objects!

For example, we have access to object instance methods like: .hasOwnProperty(), .valueOf(), and many more! Practice your documentation reading skills and check out: MDN’s object instance documentation.


There are also useful Object class methods such as Object.assign(), Object.entries(), and Object.keys() just to name a few. For a comprehensive list, browse: [MDN’s object instance documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object#Methods) 
