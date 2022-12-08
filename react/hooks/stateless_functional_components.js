import React from 'react';
import ReactDOM from 'react-dom';

function Friend() {
    return (
        <img src="https://content.codecademy.com/courses/React/react_photo-octopus.jpg" />
    );
};

export default Friend;

ReactDOM.render(
	      <Friend />,
	  document.getElementById('app')
);
