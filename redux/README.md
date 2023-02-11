

# redux

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
