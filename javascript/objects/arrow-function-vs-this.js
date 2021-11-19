const robot = {
    energyLevel: 100,
    checkEnergy: function () {
        console.log(`Energy is currently at ${this.energyLevel}%.`);
    },

    somethingElse: () => {
        console.log(robot.energyLevel);
    }
}

robot.checkEnergy();

robot.somethingElse();
