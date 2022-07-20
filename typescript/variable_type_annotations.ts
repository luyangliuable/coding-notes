///////////////////////////////////////////////////////////////////////////////
//                 Decalre that phoneNumbermust be a string.                 //
///////////////////////////////////////////////////////////////////////////////
let phoneNumber : string;

if (Math.random() > 0.5) {
    phoneNumber = '+61770102062';
} else {
    // This will give an error as phone number must be in string.
    //phoneNumber = 7167762323;

    // FIX:
    phoneNumber = "7167762323";
}
