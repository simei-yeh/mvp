import React, { useState } from 'react'

const GraphOptions = () => {
  const timeOptions = ['5min', '15min', '30min', 'daily', 'weekly']

  return (
    <div>
      {timeOptions.map(d => <button key={d}>{d}</button>)}
    </div>
  );
}


export default GraphOptions;