function proclaim(status?: string) {
    // The parameter status is optional due to the question mark
    console.log(`I'm ${status || 'not ready...'}`);
}

proclaim();
proclaim('ready?');
proclaim('ready!');
