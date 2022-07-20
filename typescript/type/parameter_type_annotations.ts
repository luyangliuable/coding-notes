// Value should be a number
function triple(value: number) {
    return value * 3;
}

// greeting should be a string and value should be a number
function greetTripled(greeting: string, value: number) {
    console.log(`${greeting}, ${triple(value)}!`);
}

greetTripled('Hiya', 5);
