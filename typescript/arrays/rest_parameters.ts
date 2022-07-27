function addPower(p: number, ...numsToAdd: number[]): number {
    let answer = 0;
    for (let i = 0; i < numsToAdd.length; i++) {
        answer += numsToAdd[i] ** p;
    }
    return answer;
}

// This will result in an error
addPower('a string', 4, 5, 6)
