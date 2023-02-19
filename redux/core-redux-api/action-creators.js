import { createStore } from 'redux';

// Create your action creators here.

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

// Modify the dispatches below.
store.dispatch({ type: 'increment' });
store.dispatch({ type: 'increment' });
console.log(store.getState());

store.dispatch({ type: 'decrement' });
store.dispatch({ type: 'decrement' });
store.dispatch({ type: 'decrement' });
console.log(store.getState());
