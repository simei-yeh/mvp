import React, { useState, useEffect } from 'react'
import './GraphOptions.css'

const GraphOptions = ({callback}) => {
  const timeOptions = ['5min', '15min', '30min', 'daily', 'weekly']

  const[timeSelected, setTimeSelected] = useState(false)
  const[timeValue, setValue] = useState({option: '30min'})

  const handleTimeClick = (event) => {
    event.preventDefault();
    setValue((timeValue) => ({
      ...timeValue,
      option: event.target.value,
    }));
    setTimeSelected(true);
  }

  // useEffect(() => {
  //   if (timeSelected) {
  //     console.log('clicked ', timeValue)
  //     callback(undefined, timeValue.option)
  //     setTimeSelected(false)
  //   }
  // })

  useEffect(() => {
    if (timeSelected) {
      console.log('clicked ', timeValue)
      callback(undefined, timeValue.option)
      setTimeSelected(false)
    }
  }, [timeSelected])

  return (
    <div className="options-bar-wrapper">
      {timeOptions.map(d => <button className={timeValue.option === d ? "selectedButton" : "timeButton"} key={d} value={d} onClick={handleTimeClick}>{d}</button>)}
    </div>
  );
}


export default GraphOptions;