let petOnSale = 'chinchilla';
let ordersArray = [
    ['rat', 2],
    ['chinchilla', 1],
    ['hamster', 2],
    ['chinchilla', 50]
];

// Write your code below:

///////////////////////////////////////////////////////////////////////////////
//                                String Enum                                //
///////////////////////////////////////////////////////////////////////////////

enum Pet {
    Hamster = "HAMSTER",
    Rat = "RAT",
    Chinchilla = "CHINCHILLA",
    Tarantula = "TARANTULA"
}


let petOnSaleTS: Pet = Pet.Chinchilla;


let ordersArrayTS: [Pet, number][] = [
    [Pet.Rat, 2],
    [Pet.Chinchilla, 1],
    [Pet.Hamster, 2],
    [Pet.Chinchilla, 50]
];


// This will give an error as 0th element must be an enum
ordersArrayTS.push(['HAMSTER', 1]);
