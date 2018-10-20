import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Chart from './components/Chart.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          Yo yo yo
        </div>
        <div class="container">
          <Chart />
        </div>
      </div>
    );
  }
}

export default App;
