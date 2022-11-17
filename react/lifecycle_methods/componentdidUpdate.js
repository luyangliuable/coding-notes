import React from 'react';


export class Clock extends React.Component {

    constructor(props) {
        super(props);
        this.state = { date: new Date() };
    }


    render() {
        return (
                <div>
                {this.props.isPrecise
                 ? this.state.date.toISOString()
                 : this.state.date.toLocaleTimeString()}
            </div>
        );
    }


    componentDidMount() {
        const oneSecond = 1000;
        // this.intervalID = setInterval(() => {
        //     this.setState({ date: new Date() });
        // }, oneSecond);
        this.startInterval(oneSecond);
    }


    componentWillUnmount() {
        clearInterval(this.intervalID);
    }

    startInterval(delay) {
        // const delay = 100;
        this.intervalID = setInterval(() => {
            this.setState({ date: new Date() });
        }, delay);
    }

    componentDidUpdate(prevProps) {
        if ( this.props.isPrecise === prevProps.isPrecise) {
            return;
        };

        clearInterval(this.intervalID);
        const delay = 100;
        this.startInterval(delay);
    }
}
