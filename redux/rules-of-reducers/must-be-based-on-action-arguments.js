// Reducer violates rule 1: 
// They should only calculate the new state value based on the state and action arguments.

const globalSong = 'We are the World';

const playlistReducer = (state = [], action) => {
    switch (action.type) {
    case 'songs/addGlobalSong': {
        // return [...state, globalSong];
        return [...state, action.payload];
    }

    default:
        return state;
    }
}

// Example call to reducer
const state = [ 'Take Five', 'Claire de Lune', 'Respect' ];
const addAction = { type: 'songs/addGlobalSong', payload: 'We are the World' };
const newState = playlistReducer(state, addAction);
