// Reducer violates rule 2: 
// They are not allowed to modify the existing state. 
// Instead, they must copy the existing state and make changes to the copied values.

const todoReducer = (state = [], action) => {
    switch (action.type) {
    case 'todos/addTodo': {
        // state.push(action.payload);
        return [...state, action.payload];
    }
    case 'todos/removeAll': {
        return [];
    }
    default: {
        return state;
    }
    }
}

// Example call to reducer
const state = [ 'Print trail map', 'Pack snacks', 'Summit the mountain' ];
const addTodoAction = { type: 'todos/addTodo', payload: 'Descend' };
const newState = todoReducer(state, addTodoAction);
