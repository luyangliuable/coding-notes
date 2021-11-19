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

