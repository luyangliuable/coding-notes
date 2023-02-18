// Reducer violates rule 2: 
// They are not allowed to modify the existing state. 
// Instead, they must copy the existing state and make changes to the copied values.

// The todoReducer function takes in the current state and an action, and returns a new state
// based on the action. When updating the state, the reducer follows the guideline that
// reducers are not allowed to modify the existing state directly. 

// To create a new state, the reducer uses the spread operator to create a copy of the
// existing state array, and then adds the new todo item to the end of the new array
// using the payload from the action. This ensures that the original state is not mutated
// and that the reducer returns a new state with the updated todo list.

const todoReducer = (state = [], action) => {
    switch (action.type) {
    case 'todos/addTodo': {
        // state.push(action.payload); // This line violates the guideline
        return [...state, action.payload]; // Instead, create a new state by copying the existing state and adding the new item
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
