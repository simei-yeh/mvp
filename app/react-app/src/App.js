import React from 'react'
import './App.css';
import Reddit from './Reddit.jsx'
import AltCoins from './AltCoins.jsx'
import Graph from './Graph.jsx'
import GraphOptions from './GraphOptions.jsx'
import GraphSearchBar from './GraphSearchBar.jsx'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      reddit: [],
      stockGraph: [],
      altCoinPrices: []
    }
    this.retrieveAdditionalData = this.retrieveAdditionalData.bind(this)
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
        data[0].map(d => {
          let x = Math.random() * 256;
          let y = Math.random() * 256;
          let z = Math.random() * 256;
          d.push([x,y,z])
        })
        this.setState({
          reddit: data[0],
          stockGraph: data[1],
          altCoinPrices: data[2]
        })
      })
  }

  retrieveAdditionalData(ticker, interval = 1800) {
    console.log('click!', ticker, interval)
    fetch(`/api/v1/quotes/stocks?ticker=${ticker}&interval=${interval}`, {
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    })
      .then(response => response.json())
      .then((data) => {
        this.setState({
          stockGraph: data
        })
      })
  }

  render() {
    return (
      <div className="App">
        <div className="headerContainer">
          <h1>tradetheta</h1>
        </div>
        <div className="boxesContainer">
          <div className="numbers">
            <div className="graph-search-options-wrapper">
              <GraphOptions />
              <GraphSearchBar />
            </div>
            <Graph data={this.state.stockGraph}
              color="#B08EA2"
            />
          </div>
          <div className="bottom-chart-container">
            <div className="bottom-chart-wrapper">
              <Reddit data={this.state.reddit}
                getTicker={this.retrieveAdditionalData}
                title="reddit popularity"
              />
            </div>
            <div className="bottom-chart-wrapper">
              <AltCoins data={this.state.altCoinPrices}
                title="Crypto Quotes"
                color="#70CAD1" />
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
