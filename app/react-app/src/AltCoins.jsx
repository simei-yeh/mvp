import React from 'react'
import Chart from 'chart.js';

class AltCoins extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidUpdate() {
    this.myChart.data.labels = this.props.data.map(d => d[1]);
    this.myChart.data.datasets[0].data = this.props.data.map(d => d[2].toFixed(2));
    this.myChart.update();
  }

  componentDidMount() {
    this.myChart = new Chart(this.chartRef.current, {
      type: 'bar',
      data: {
        labels: this.props.data.map(d => d[1]),
        datasets: [{
          label: this.props.title,
          data: this.props.data.map(d => d[2].toFixed(2)),
          backgroundColor: 'rgba(112,202,209, 0.7)'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'price vs USD'
            },
            type: 'logarithmic',
            position: 'left',
            ticks: {
              min: 0, //minimum tick
              max: 35000, //maximum tick
              callback: function (value, index, values) {
                return Number(value.toString());//pass tick values as a string into Number function
              },
            },
            afterBuildTicks: function (chartObj) { //Build ticks labelling as per your need
              chartObj.ticks = [];
              chartObj.ticks.push(10);
              chartObj.ticks.push(100);
              chartObj.ticks.push(500);
              chartObj.ticks.push(1000);
              chartObj.ticks.push(10000);
              chartObj.ticks.push(20000);
              chartObj.ticks.push(35000);
            },

          }],
          xAxes: [{
            gridLines: {
              display: false,
              tickMarkLength: 0
            },
            scaleLabel: {
              display: true,
              labelString: 'cryptocurrency'
            },

          }],
        }
      },
    });
  }

  render() {
    return (
      <div>
        <h3>AltCoins Quotes</h3>
        <canvas ref={this.chartRef} />
      </div>
    );
  }
}

export default AltCoins;