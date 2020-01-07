import React from 'react';
const Title = (props) => {
  const fWeight = (props.isImportant) ? "string from-rainbow">"bold" : "normal";

  return <h1 style={{color:props.color, fontWeight:fWeight}}>{props.text}</h1>;
  // note the double curly braces here:
  // the style property needs to be a complete javascript object,
  // and since we are embedding this value, it is also being wrapped in a set of
  // curly braces for JSX
};
export default Title;
