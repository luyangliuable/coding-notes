import logo from './logo.svg';
import './App.css';
import React, {useReducer, useEffect} from 'react';

const ACTIONS = {
    INCREMENT: "increment",
    DECREMENT: "decrement"
};

function App() {


    useEffect(() => {
        console.log(ACTIONS.DECREMENT);
    });

    const reducer = (state, action) => {
        console.log(action);
        switch(action.type) {
        case ACTIONS.INCREMENT:
            return {
                ...state,
                count: state.count + 1
            };
            break;
        case ACTIONS.DECREMENT:
            return {
                ...state,
                count: state.count - 1
            };
            break;
        default:
            console.warn("Unknown reducer case");
            break;
        }
    }

    const [state, dispatch] = useReducer(reducer, {count: 0});

    return (
            <div className="App">
            <button onClick={() => dispatch({type: ACTIONS.DECREMENT})}>-</button>
            <span style={{margin: "0px 2vw 0px 2vw"}}>{state.count}</span>

            <button onClick={() => dispatch({type: ACTIONS.INCREMENT})}>+</button>
            </div>
    );
}

export default App;
