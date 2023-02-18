# redux

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [redux](#redux)
    - [Rules of Reducers](#rules-of-reducers)
    - [Immutable Updates and Pure Function](#immutable-updates-and-pure-function)
    - [Examples](#examples)

<!-- markdown-toc end -->


## Rules of Reducers
1. They should only calculate the new state value based on the state and action arguments.
> See [must-be-based-on-action-arguments.js](./rules-of-reducers/must-be-based-on-action-arguments.js )  <br />
2. They are not allowed to modify the existing state. Instead, they must copy the existing state and make changes to the copied values.
> See [not-allowed-to-modify-existing-state.js](./rules-of-reducers/not-allowed-to-modify-existing-state.js)  <br />
3. They must not do any asynchronous logic or have other “side effects”.
> See [must-not-have-async-logic-or-side-effect.js](./rules-of-reducers/must-not-have-async-logic-or-side-effect.js)  <br />

## Immutable Updates and Pure Function
* Redux requires immutable updates and pure functions to be used in its reducers.
* **Immutable** updates make a copy of the argument and change the copy, rather than changing the original.
* **Pure functions** will always have the same output given the same input and have no side effects.
* Reducers should only calculate the new state based on the state and action arguments.
* Asynchronous logic or other side effects should not be performed by reducers to maintain their purity.

## Store
* Redux uses a store object to contain the state, dispatch actions, and call the reducer.
* There is typically only one store per Redux application.
* The store initializes the state and the view displays it.
* When a user interacts with the view, an action is dispatched to the store and the reducer determines the next state.
* The view is updated to display the new state.

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
