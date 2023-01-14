const promise = new Promise((resolve, reject) => {
    var res;
    if (Math.random() < .5) {
        res = true;
    } else {
        res = false;
    }

    if (res) {
        setTimeout( ()  => resolve('Resolved!'), 5000 );
    }
    else {
        setTimeout(() => reject(Error('Error')), 5000);
    }
});

promise.then((res) => console.log(res), (err) => console.log(err));
