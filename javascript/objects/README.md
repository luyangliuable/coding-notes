# Objects

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Objects](#objects)
    - [Accessing objects bracket notation](#accessing-objects-bracket-notation)

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


