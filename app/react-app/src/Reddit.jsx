import React from 'react'
import Chart from 'chart.js';

class Reddit extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  parseChartData() {
    let chartData = []
    this.props.data.map(d => {
      let x = Math.random() * 256;
      let y = Math.random() * 256;
      let z = Math.random() * 256;
      let datapoint = {
        label: d[3],
        data: [{ 'x': d[1], 'y': d[0], 'r': d[0] < 10 ? d[0] : Math.log(d[0]) * 3 }],
        backgroundColor: `rgba(${x},${y},${z},0.5)`,
        hoverBorderWidth : 8,
        hoverBackgroundColor: `rgba(${x},${y},${z},1)`,
      }
      chartData.push(datapoint);
    });
    return chartData;
  }

  componentDidUpdate() {
    this.myChart.data.datasets = this.parseChartData();
    this.myChart.update();
  }

  componentDidMount() {
    this.myChart = new Chart(this.chartRef.current, {
      type: 'bubble',
      data: {
        datasets: this.parseChartData()
      },
      options: {
        events: ['mousemove', 'mouseout', 'click', 'touchstart', 'touchmove'],
        onClick: (e) => {

        },
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'weighted popularity'
            },
            type: 'logarithmic',
            position: 'left',
            ticks: {
              min: 0, //minimum tick
              max: 30000, //maximum tick
              display: false,
              callback: function (value, index, values) {
                return Number(value.toString());//pass tick values as a string into Number function
              },
            },
            afterBuildTicks: function (chartObj) { //Build ticks labelling as per your need
              chartObj.ticks = [];
            },
            gridLines: {
              tickMarkLength: 0// Adjusts the height for the tick marks area
            }
          }],
          xAxes: [{
            scaleLabel: {
              display: true,
              labelString: 'number of mentions'
            },
            type: 'logarithmic',
            position: 'left',
            ticks: {
              display: false,
              min: 0, //minimum tick
              max: 8000, //maximum tick
              callback: function (value, index, values) {
                return value;
              },
            },
            afterBuildTicks: function (chartObj) { //Build ticks labelling as per your need
              chartObj.ticks = [];
            }
          }],
        },
      },
    });
  }

  render() {
    return (
      <canvas ref={this.chartRef} />
    );
  }
}

export default Reddit;