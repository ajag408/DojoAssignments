import React from 'react';
const Square = (props) => {

  return <div style={{font: "bold", display: "inline-block", "background-color":props.back_color, color: props.color, height: "100px", width: "100px"}}>{props.text}</div>;
  // note the double curly braces here:
  // the style property needs to be a complete javascript object,
  // and since we are embedding this value, it is also being wrapped in a set of
  // curly braces for JSX
};
export default Square;
