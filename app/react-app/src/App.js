import React from 'react'
import './App.css';
import Reddit from './Reddit.jsx'
import AltCoins from './AltCoins.jsx'
import Graph from './Graph.jsx'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    }
  }


  componentDidMount() {
    this.retrieveInitialData()
  }

  retrieveInitialData() {
    fetch('/api', {
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    })
      .then(response => response.text())
      .then(data => console.log(data))
  }

  render() {
    return (
      <div className="App">
        <h1>checking</h1>
        <Graph />
        <Reddit />
        <AltCoins />
      </div>
    )
  }
}

export default App;
