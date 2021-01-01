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
      reddit: [],
      stockGraph: [],
      altCoinPrices: []
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
    .then(response => response.json())
    .then((data) => {
        this.setState({
          reddit: data[0],
          stockGraph: data[1],
          altCoinPrices: data[2]
        })
      })
    }

  render() {
    return (
      <div className="App">
        <div className="headerContainer">
          <h1>tradetheta.io</h1>
        </div>
        <div className="boxesContainer">
          <div className="numbers">
            <Graph data={this.state.stockGraph}
            title="TSLA 1 year"
            color="#B08EA2"
            />
          </div>
          <div className="sources">
            <div>
            <Reddit data={this.state.reddit}
              title="reddit popularity"
              color="#FF4500"
            />
            </div>
            <div>
            <AltCoins data={this.state.altCoinPrices}
            title="Crypto Quotes"
            color="#70CAD1"/>
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
