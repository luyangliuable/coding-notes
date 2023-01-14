const {shopForBeans, soakTheBeans, cookTheBeans} = require('./library.js');

// Write your code below:

async function makeBeans() {
    // We mark our function as async.

    // Inside our function, we create a variable firstValue assigned await returnsFirstPromise(). This means firstValue is assigned the resolved value of the awaited promise.
    const type = await shopForBeans();

    // Then, we create a variable secondValue assigned to await returnsSecondPromise(firstValue). Therefore, secondValue is assigned this promise’s resolved value.
    const isSoft = await soakTheBeans(type);

    // Then, we create a variable dinner assigned to await cookTheBeans(isSoft). Therefore, this value is assigned previous promise’s resolved value.
    const dinner = await cookTheBeans(isSoft);
};

makeBeans();
