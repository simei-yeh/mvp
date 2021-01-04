import React, { useState } from 'react'
import './GraphSearchBar.css';

const GraphSearchBar = () => {
  const timeOptions = ['5min', '15min', '30min', 'daily', 'weekly']


  return (
    <div className="search-bar-wrapper">
      {timeOptions.map(d => <button key={d}>{d}</button>)}
    </div>
  );
}


export default GraphSearchBar;