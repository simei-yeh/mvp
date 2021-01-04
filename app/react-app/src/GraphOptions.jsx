import React, { useState } from 'react'
import './GraphOptions.css'

const GraphOptions = () => {
  const timeOptions = ['5min', '15min', '30min', 'daily', 'weekly']

  const[timeValue, setValue] = useState({option: '30min'})

  const handleTimeClick = (event) => {
    event.persist();
    event.preventDefault();
    setValue((timeValue) => ({
      ...timeValue,
      option: event.target.value,
    }));
    console.log('clicked ', timeValue)
  }

  return (
    <div className="options-bar-wrapper">
      {timeOptions.map(d => <button className={timeValue.option === d ? "selectedButton" : "timeButton"} key={d} value={d} onClick={handleTimeClick}>{d}</button>)}
    </div>
  );
}


export default GraphOptions;