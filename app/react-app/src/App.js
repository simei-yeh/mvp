import React, { useState, useEffect } from 'react'
import './App.css';

function App() {
// eslint-disable-next-line
  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch('/api', {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
       }
    })
    .then(response => response.text())
    .then(data => console.log(data))
  })
  return (
    <div className="App">
      <h1>checking</h1>
    </div>
  );
}

export default App;
