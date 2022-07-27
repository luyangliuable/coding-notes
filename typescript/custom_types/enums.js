var petOnSale = 'chinchilla';
var ordersArray = [
    ['rat', 2],
    ['chinchilla', 1],
    ['hamster', 2],
    ['chinchilla', 50]
];
// Write your code below:
var Pet;
(function (Pet) {
    Pet["Hamster"] = "dsadasd";
    Pet[Pet["Rat"] = void 0] = "Rat";
    Pet[Pet["Chinchilla"] = void 0] = "Chinchilla";
    Pet[Pet["Tarantula"] = void 0] = "Tarantula";
})(Pet || (Pet = {}));
var a = Pet.Hamster;
console.log(a);
