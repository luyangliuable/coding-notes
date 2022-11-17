class HospitalEmployee {
    constructor(name) {
        this._name = name;
        this._remainingVacationDays = 20;
    }

    static generatePassword() {
        ///////////////////////////////////////////////////////////////////////
        //                                  comment                                                                      //
        ///////////////////////////////////////////////////////////////////////////////

        return Math.floor( Math.random()*10000 );
    }

    get name() {
        return this._name;
    }

    get remainingVacationDays() {
        return this._remainingVacationDays;
    }

    takeVacationDays(daysOff) {
        this._remainingVacationDays -= daysOff;
    }
}

class Nurse extends HospitalEmployee {
    constructor(name, certifications) {
        super(name);
        this._certifications = certifications;
    }

    get certifications() {
        return this._certifications;
    }

    addCertification(newCertification) {
        this.certifications.push(newCertification);
    }
}

console.log(HospitalEmployee.generatePassword());
