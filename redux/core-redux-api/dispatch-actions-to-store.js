import { createStore } from 'redux';

const initialState = 0;
const countReducer = (state = initialState, action) => {
    switch (action.type) {
    case 'increment':
        return state + 1;
    case 'decrement':
        return state - 1;
    default:
        return state;
    }
}

const store = createStore(countReducer);

// Dispatch your actions here.
store.dispatch({type: 'increment'});
store.dispatch({type: 'increment'});
console.log(store.getState());

let numberOfTimes = 3;

store.dispatch({type: 'decrement'});
store.dispatch({type: 'decrement'});
store.dispatch({type: 'decrement'});
console.log(store.getState());

for (const i = 0; i < numberOfTimes; i++) {
    store.dispatch({type: 'decrement'});
}
