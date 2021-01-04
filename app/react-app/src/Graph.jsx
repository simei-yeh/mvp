import React from 'react'
import Chart from 'chart.js';

class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidUpdate() {
    let data = this.props.data[0];
    this.myChart.data.labels = data[3].map(d => new Date(d['t']).toLocaleString('en-US'));
    this.myChart.data.datasets[0].label = data[0].split('-').join(' ');
    this.myChart.data.datasets[0].data = data[3].map(d => d['c']);
    this.myChart.options.title.text = `${data[2]} every ${data[8]} for ${data[6]}`
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
        title: {
          fontSize: 20,
          display: true,
          text: '',
        },
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false
        },
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