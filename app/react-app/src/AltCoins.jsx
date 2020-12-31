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
        labels: this.props.data.map(d => d[2].toFixed(2)),
        datasets: [{
          label: this.props.title,
          data: this.props.data.map(d => d[1]),
          backgroundColor: this.props.color
        }]
      }
    });
  }

  render() {
    return (
      <canvas ref={this.chartRef} />
    );
  }
}

export default AltCoins;