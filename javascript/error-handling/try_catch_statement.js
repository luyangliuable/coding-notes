try {
    throw Error("Too normal");
} catch (e) {
    console.log(e.message);
}
