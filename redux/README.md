# redux

## Rules of Reducers
1. They should only calculate the new state value based on the state and action arguments.
2. They are not allowed to modify the existing state. Instead, they must copy the existing state and make changes to the copied values.
3. They must not do any asynchronous logic or have other “side effects”.

## Examples
* ./test.js

```js
(params) => {
    2
}
```

* ./reducer.js

```js
// Define the initial state with an array of songs
const initialState = [ 'Take Five', 'Claire de Lune', 'Respect' ];

// Action for adding a new song to the state
const addNewSong = {
    type: 'songs/addSong',
    payload: 'Halo'
};

// Action for removing a specific song from the state
const removeSong = {
    type: 'songs/removeSong',
    payload: 'Take Five'
};

// Action for removing all songs from the state
const removeAll = {
    type: 'songs/removeAll',
};

// Reducer for managing the state updates based on actions
const reducer = (state = initialState, action) => {
    switch(action.type) {
        case 'songs/addSong': {
            // Add the new song to the state
            return [...state, action.payload];
        }
        case 'songs/removeSong': {
            // Remove the specific song from the state
            return state.filter(item => item !== action.payload);
        }
        default: {
            // Return the current state if no action is matched
            return state;
        }
    }
};
```
