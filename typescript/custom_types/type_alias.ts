// This is a generic type alias
type Collection<G> = {
    name: string,
    quantity: number,
    content: G[]
};

let bookCollection: Collection<string> = {
    name: 'Nursery Books',
    quantity: 3,
    content: ['Goodnight Moon', 'Humpty Dumpty', 'Green Eggs & Ham']
};

let primeNumberCollection: Collection<number> = {
    name: 'First 5 Prime Numbers',
    quantity: 5,
    content: [2, 3, 5, 7, 11]
};

// This is a generic function type alias
function findMiddleMember<M>(members: M[]): M {
    return members[Math.floor(members.length/2)];
}

// Call function for an array of strings
console.log(findMiddleMember<string>(['I', 'am', 'very', 'happy'])); // Prints "very"

// Call function for an array of numbers
console.log(findMiddleMember<number>([210, 369, 102]));     // Prints 369
