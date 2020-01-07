import React from 'react'; // import the React library
import ReactDOM from 'react-dom'; // import the ReactDOM library
// we can create a simple element to display on our HTML page
// const App = React.createElement("h1", null, "Hello World");

// with JSX we can perform the same React.createElement() call with the following:
import App from './App';
// and load our App into the DOM, targeting the div located in /public/index.html
ReactDOM.render(<App />, document.getElementById('root'));
