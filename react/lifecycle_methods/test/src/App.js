import React from 'react';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {display: true};
    }

    render() {
        return (
                <>
                <button onClick={() => this.setState({display: !this.state.display})}>Toggle Hide</button>
                {this.state.display ? <Clock /> : ''}
            </>);
    }
}

class Clock extends React.Component {


    constructor(props) {
        super(props);
        this.state = { date: new Date(), display: true };
    }



    render() {
        console.log('This component will shown');
        return (
                <>
                {this.state.display ? <div style={
                    {
                        position: 'absolute',
                        left: '25vw',
                        top: '10vw',
                        borderRadius: '20px',
                        background: '#1e90ff',
                        width: '50vw',
                        height: '40vw',
                        color: 'white',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        fontSize: '40px'
                    }}>

                 {this.props.isPrecise
                  ? this.state.date.toISOString()
                  : this.state.date.toLocaleTimeString()}
                 </div>
                 : ''}
            </>
        );
    }


    componentDidMount() {
        const oneSecond = 1000;
        this.startInterval(oneSecond);
        console.log('This component will is showing');
    }


    componentWillUnmount() {
        clearInterval(this.intervalID);
        console.log('This component will now be hidden');
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

export default App;
