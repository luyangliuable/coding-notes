const speciesArray = [ {speciesName:'shark', numTeeth:50}, {speciesName:'dog', numTeeth:42}, {speciesName:'alligator', numTeeth:80}, {speciesName:'human', numTeeth:32}];

// Write your code here:

const sortSpeciesByTeeth = (arr) => {
    const res = arr.sort(( item, prev ) => {
        return item.numTeeth - prev.numTeeth;
    });

    return res;
};






// Feel free to comment out the code below when you're ready to test your function!

console.log(sortSpeciesByTeeth(speciesArray));

  // Should print:
  // [ { speciesName: 'human', numTeeth: 32 },
  //   { speciesName: 'dog', numTeeth: 42 },
  //   { speciesName: 'shark', numTeeth: 50 },
  //   { speciesName: 'alligator', numTeeth: 80 } ]

