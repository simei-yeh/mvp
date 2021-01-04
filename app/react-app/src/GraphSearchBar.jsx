import React, { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearchDollar } from '@fortawesome/free-solid-svg-icons'
import './GraphSearchBar.css';

const GraphSearchBar = ({callback, autosuggest}) => {
  const [value, setValue] = useState('');
  const [submitted, setSubmitted] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  }

  const handleInputChange = (e) => {
    e.persist();
    setValue(e.target.value.toUpperCase());
  }

  useEffect(() => {
    if (submitted) {
      console.log('submitted')
      callback(value)
      setSubmitted(false);
      setValue('')
    }
  }, [submitted])

  return (
    <form className="search-bar-wrapper" onSubmit={handleSubmit}>
      <label htmlFor="searchbar"></label>
      <input type="text" name="searchbar" className="searchbar" onChange={handleInputChange} value={value}></input>
      <button className="icon"><FontAwesomeIcon icon={faSearchDollar} /></button>
    </form>
  );
}


export default GraphSearchBar;