import React from 'react'
import Chart from 'chart.js';

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidUpdate() {
    this.myChart.data.labels = this.props.data[0][3].map(d => new Date(d['t']).toLocaleString('en-US'));
    this.myChart.data.datasets[0].label = this.props.data[0][0].split('-').join(' ');
    this.myChart.data.datasets[0].data = this.props.data[0][3].map(d => d['c']);
    this.myChart.update();
  }

  componentDidMount() {
    this.myChart = new Chart(this.chartRef.current, {
      type: 'line',
      data: {
        labels: '',
        datasets: [{
          label: '',
          data: '',
          backgroundColor: 'rgb(176,142,162,0.2)'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
      }
    });
  }

  render() {
    return (
      <canvas ref={this.chartRef} />
    );
  }
}

export default Graph;