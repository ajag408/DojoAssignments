import React from 'react';

import Square from './Square'; // we can drop the .js file extension
import './App.css';
const App = (props) => {
  return (
      <div>
          <Square back_color="blue" color="white" text="white on blue" />
          <Square back_color="red" color="blue" text="blue on red" />
          <Square back_color="pink" color="green" text="green on pink" />
      </div>
  )
};
export default App;
