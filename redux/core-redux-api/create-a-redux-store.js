// Import the createStore function from the 'redux' library
import {createStore} from 'redux';

// Set the initial state for the counter
const initialState = 0;

// Define a reducer function for the counter
const countReducer = (state = initialState, action) => {
    switch (action.type) {
    case 'increment':
        return state + 1;
    default:
        return state;
    }
}

// Create a Redux store using the countReducer function
const store = createStore(countReducer);
