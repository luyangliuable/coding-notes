
// Write your code below:

enum Pet {
    Hamster,
    Rat,
    Chinchilla,
    Tarantula
}

let petOnSaleTS: Pet = Pet.Chinchilla;

let ordersArrayTS: [Pet, number][] = [
    [Pet.Rat, 2],
    [Pet.Chinchilla, 1],
    [Pet.Hamster, 2],
    [Pet.Chinchilla, 50]
];

const a = Pet.Hamster;
console.log(a);

// Wrong code because Jerboa is not a type of pet!
// Error goes bellow
ordersArrayTS.push([Pet.Jerboa, 3]);
