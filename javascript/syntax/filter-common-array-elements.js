// Write your code here:

const justCoolStuff = (arr1, arr2) => {
    const res = arr1.filter(item => {
        let a = false;

        for (var item2 of arr2) {
            if (item2 == item) {
                return true;
            };
        };
    });

    return res;
};


// Feel free to uncomment the code below to test your function
const coolStuff = ['gameboys', 'skateboards', 'backwards hats', 'fruit-by-the-foot', 'pogs', 'my room', 'temporary tattoos'];

const myStuff = [ 'rules', 'fruit-by-the-foot', 'wedgies', 'sweaters', 'skateboards', 'family-night', 'my room', 'braces', 'the information superhighway'];

console.log(justCoolStuff(myStuff, coolStuff));
// Should print [ 'fruit-by-the-foot', 'skateboards', 'my room' ]
