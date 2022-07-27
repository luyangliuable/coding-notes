///////////////////////////////////////////////////////////////////////////////
//  WARNING: docstring appears before functions in typescript and javascript //
///////////////////////////////////////////////////////////////////////////////


/**
 * This function makes a fruit salad by adding all the fruits.
 * @param fruit1 - the first fruit.
 * @param fruit2 - the second fruit
 * @returns nothing
 */
function makeFruitSalad(fruit1: string, fruit2: string): void {
    let salad = fruit1 + fruit2 + fruit2 + fruit1 + fruit2 + fruit1 + fruit1;
    console.log(salad);
}


/**
 * This function makes proclamation.
 * @param status - the status of you
 * @param repeat - the number of times to repeat the proclamation.
 * @returns nothing
 */
function proclaim(status = 'not ready...', repeat = 1) {
    for (let i = 0; i < repeat; i += 1) {
        console.log(`I'm ${status}`);
    }
}
