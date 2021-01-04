import React, { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearchDollar } from '@fortawesome/free-solid-svg-icons'
import './GraphSearchBar.css';

const GraphSearchBar = () => {



  return (
    <form className="search-bar-wrapper">
      <label htmlFor="searchbar"></label>
      <input type="text" name="searchbar"></input>
      <button className="icon"><FontAwesomeIcon icon={faSearchDollar} /></button>
    </form>
  );
}


export default GraphSearchBar;