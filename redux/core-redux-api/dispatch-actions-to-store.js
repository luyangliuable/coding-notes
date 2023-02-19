// Import the createStore function from the 'redux' library
import { createStore } from 'redux';

// Set the initial state for the counter
const initialState = 0;

// Define a reducer function for the counter that updates the state based on 'increment' and 'decrement' actions
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

// Create a Redux store using the countReducer function
const store = createStore(countReducer);

// Dispatch actions to increment and decrement the counter and log the updated state of the store to the console
store.dispatch({type: 'increment'});
store.dispatch({type: 'increment'});
console.log(store.getState());

let numberOfTimes = 3;

store.dispatch({type: 'decrement'});
store.dispatch({type: 'decrement'});
store.dispatch({type: 'decrement'});
console.log(store.getState());

// Use a for loop to dispatch multiple decrement actions to the store and update the state accordingly
for (const i = 0; i < numberOfTimes; i++) {
store.dispatch({type: 'decrement'});
}
