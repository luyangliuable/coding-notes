function formatValue(value: string | number) {
    // Write your code here
    if (typeof value === 'string') {
        console.log(value.toLowerCase());
    } else if (typeof value === 'number') {
        console.log(value.toFixed(2));
    }
}

formatValue('Hiya');
formatValue(42);
