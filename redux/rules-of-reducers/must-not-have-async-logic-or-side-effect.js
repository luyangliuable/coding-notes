// Reducer violates rule 3:
// They must not do any asynchronous logic or have other “side effects”.

const initialState = [0, 1, 2];

const reducer = (state = initialState, action) => {
    switch (action.type) {
    case 'numbers/addRandom': {
        return [...state, action.payload];
    }
    default: {
        return state;
    }
    }
}

// Example call to reducer
const randomAction = { type: 'numbers/addRandom', payload: Math.random() };
const newState = reducer(undefined, randomAction);
