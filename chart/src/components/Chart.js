import React, {Component} from 'react';
import {Bar, Line, Pie, Scatter} from 'react-chartjs-2';

class Chart extends Component {
  constructor(props) {
    super(props);
    this.state = {
      barData:{
        labels: ['EDM', 'Hip Hop', 'Pop', 'Country', 'Rock', 'Jazz'],
        datasets: [
          {
            label:'Likeability',
            data:[
              .5,
              .34,
              .89,
              .76
            ],
            backgroundColor:[
              'rgba(255, 99, 132, 0.6)',
              'rgba(54, 162, 235, 0.6)',
              'rgba(255, 206, 86, 0.6)',
              'rgba(75, 192, 192, 0.6)',
              'rgba(255, 159, 64, 0.6)',
              'rgba(153, 102, 255, 0.6)',
            ]
          }
        ]
      }
    }
  }

  render() {
    return (
      <div className="chart">
        <Bar
          data = {this.state.barData}
          options = {{
            maintainAspectRatio: false,
          }}

        />
        <Line
          data={this.state.barData}
          options={{
            title:{
              display:this.props.displayTitle,
              text:'Largest Cities In '+this.props.location,
              fontSize:25
            },
            legend:{
              display:this.props.displayLegend,
              position:this.props.legendPosition
            }
          }}
        />
      </div>
    )
  }
}

export default Chart;
