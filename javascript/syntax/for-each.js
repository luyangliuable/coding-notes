const veggies = ['broccoli', 'spinach', 'cauliflower', 'broccoflower'];

const politelyDecline = (veg) => {
    console.log('No ' + veg + ' please. I will have pizza with extra cheese.');
}

// Write your code here:
const declineEverything = (arr) => {
    arr.forEach((item) => politelyDecline(item));
};

declineEverything(veggies);
