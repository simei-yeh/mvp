import React from 'react'
import Chart from 'chart.js';

class Reddit extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidUpdate() {
    this.myChart.data.labels = this.props.data.map(d => d[3]);
    this.myChart.data.datasets[0].data = this.props.data.map((d,i) => ({'x': d[1], 'y': d[0], 'r': d[0] < 10 ? d[0] : Math.log(d[0])*3}));
    this.myChart.update();
  }

  componentDidMount() {
    this.myChart = new Chart(this.chartRef.current, {
      type: 'bubble',
      data: {
        labels: this.props.data.map(d => d[3]),
        datasets: [{
          label: this.props.title,
          data: this.props.data.map((d,i) => ({'x': d[1], 'y': d[0], 'r': d[0] < 10 ? d[0] : Math.log(d[0])*3})),
          backgroundColor: 'rgba(255,69,0,0.5)'
        }]
      },
      options: {
        events: ['click','mousemove', 'mouseout'],
        onClick: (e) => {

        },
        onHover: (e) => {

        },
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
              callback: function (value, index, values) {
                return Number(value.toString());//pass tick values as a string into Number function
              },
            },
            afterBuildTicks: function (chartObj) { //Build ticks labelling as per your need
              chartObj.ticks = [];
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
              min: 0, //minimum tick
              max: 8000, //maximum tick
              callback: function (value, index, values) {
                return Number(value.toString());//pass tick values as a string into Number function
              },
            },
            afterBuildTicks: function (chartObj) { //Build ticks labelling as per your need
              chartObj.ticks = [];
            }
          }],
        }
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