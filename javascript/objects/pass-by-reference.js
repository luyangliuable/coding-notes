let spaceship = {
    'Fuel Type' : 'Turbo Fuel',
    homePlanet : 'Earth'

};

// Write your code below

function greenEnergy(object) {
    object['Fuel Type'] = 'avocado oil';
}

function remotelyDisable(object) {
    object.disabled = true;
}

greenEnergy(spaceship);
remotelyDisable(spaceship);
console.log(spaceship);
