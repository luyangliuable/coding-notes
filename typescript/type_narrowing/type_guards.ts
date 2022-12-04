function formatStatistic(stat: string | number) {
    if (typeof stat === 'number'){
        return stat.toFixed(2);
    } else if (typeof stat === 'string') {
        return stat.toUpperCase();
    }
}

console.log(formatStatistic('Win'));
console.log(formatStatistic(0.364));
