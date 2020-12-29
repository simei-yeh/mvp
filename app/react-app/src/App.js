import React from 'react'
import './App.css';
import Reddit from './Reddit.jsx'
import AltCoins from './AltCoins.jsx'
import Graph from './Graph.jsx'
import Quotes from './Quotes.jsx'

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
        <div className="headerContainer">
          <h1>tradetheta.io</h1>
        </div>
        <div className="boxesContainer">
          <div className="numbers">
            <Graph />
            <Quotes />
          </div>
          <div className="sources">
            <Reddit />
            <AltCoins />
          </div>
        </div>
      </div>
    )
  }
}

export default App;
