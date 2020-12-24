import logo from './logo.svg';
import React, { useState, useEffect } from 'react'
import './App.css';

function App() {
  const [initialData, setInitialData] = useState([{}])

  useEffect(() => {
    fetch('/')
    .then(response => response.json())
    .then(data => console.log(data))
  })
  return (
    <div className="App">
      <h1>checking</h1>
    </div>
  );
}

export default App;
