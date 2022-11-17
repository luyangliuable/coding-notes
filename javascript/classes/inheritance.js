class HospitalEmployee {
    constructor(name, department) {
        this._name = name;
        this._department = department;
        this._remainingVacationDays = 20;
    };

    get name() {
        return this._name;
    }

    get department() {
        return this._department;
    }

    get remainingVacationDays() {
        return this._remainingVacationDays;
    }

    takeVacationDays(daysOff) {
        this._remainingVacationDays -= daysOff;
    }

}

class Doctor extends HospitalEmployee {
    constructor(name, department) {
        super(name, department);
        // this._insurance;
    }
}


class Nurse extends HospitalEmployee {
    constructor(name, certifications) {
        super(name, 'Nurse');
        this._certifications = certifications;
    }

    addCertification(newCertification) {
        this._certifications.push(newCertification);
        console.log(this._certifications);
    }

    get certifications() {
        return this._certifications;
    }
}

const nurseOlynyk = new Nurse('Olynyk', ['Trauma','Pediatrics']);

nurseOlynyk.takeVacationDays(5);
nurseOlynyk.addCertification('Genetics');

console.log(nurseOlynyk.remainingVacationDays);

console.log(nurseOlynyk.certifications);
