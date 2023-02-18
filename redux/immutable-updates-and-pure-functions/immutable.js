// This function is immutable because it creates a new array without modifying the original list.
const removeItemAtIndex = (list, index) => {
    // Use the spread operator to create a new array with the elements before the removed element and the elements after the removed element.
    return [
        ...list.slice(0, index),
        ...list.slice(index+1, list.length)
    ];
};

// This line is not part of the function, it just calls the function with sample arguments and prints the result to the console.
console.log(removeItemAtIndex(['a', 'b', 'c', 'd'], 1));
