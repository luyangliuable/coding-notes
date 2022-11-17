import React from 'react';
import ReactDOM from 'react-dom';

class Clock extends React.Component {
    // Add your methods in here.
    constructor(props) {
        super(props);
        this.state = {date: new Date()};
    }

    render() {
        ///////////////////////////////////////////////////////////////////////
        //                             Mount time                            //
        ///////////////////////////////////////////////////////////////////////
        return(
                <div>
                {this.state.date.toLocaleTimeString()}
            </div>
        );
    }

    componentDidMount() {
        ///////////////////////////////////////////////////////////////////////
        //                            Update timer                           //
        ///////////////////////////////////////////////////////////////////////
        const oneSecond = 1000;
        this.intervalID = setInterval(() => {
            this.setState({ date: new Date() });
        }, oneSecond);    }

    componentWillUnmount() {
        ///////////////////////////////////////////////////////////////////////
        //                             HIde time                             //
        ///////////////////////////////////////////////////////////////////////
        clearInterval(this.intervalID);

    }

    ReactDOM.render(<Clock />, document.getElementById('app'));
