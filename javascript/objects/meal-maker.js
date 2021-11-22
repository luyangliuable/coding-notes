const menu = {
    _courses: {
        appetizers: [],
        mains: [],
        desserts: [],
    },
    set appetizer(newAppetizer) {
        this._courses.appetizers.push(newAppetizer);
    },

    get appetizer() {
        return this._courses.appetizers;
    },

    get course() {
        for(let course in this._courses) {
            console.log(`${course}: ${this._courses[course]}`);
        }
    },

    set mains(newMain) {
        this._course.main.push(newMain);
    },

    get Mains() {
        return this._course.mains;
    },

    set desserts(newDesert) {
        this._course.desserts.push(newDesert);
    },

    get desserts() {
        return this._course.desserts;
    },

    addDishToCourse(dish) {
        this.appetizer = dish.name;
    },

    getRandomDishFromCourse: (courseName) => {
        let randnum = Math.random()*(courseName._courses.dishes.length);

        randnum = Math.floor(randnum);
        return courseName._course.dishes[randnum];
    }

};

menu.appetizer = "pie";
console.log(menu.appetizer);

console.log(menu.course);
