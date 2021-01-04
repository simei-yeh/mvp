import React, { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearchDollar } from '@fortawesome/free-solid-svg-icons'
import './GraphSearchBar.css';

const GraphSearchBar = ({ callback, autosuggest, suggestionsArray }) => {
  const [value, setValue] = useState('');
  const [inputChange, setInputChange] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [suggestions, setSuggestions] = useState(suggestionsArray);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  }

  const handleInputChange = (e) => {
    e.persist();
    setValue(e.target.value.toUpperCase());
    setInputChange(true);
  }

  useEffect(() => {
    if (inputChange) {
      console.log('input changed')
      autosuggest(value)
      setInputChange(false);
    } else {
      setSuggestions(suggestionsArray)
    }
  }, [inputChange, suggestionsArray, autosuggest, value])

  useEffect(() => {
    if (submitted) {
      console.log('submitted')
      callback(value)
      setSubmitted(false);
      setValue('')
    }
  }, [submitted, callback, value])

  return (
    <form className="search-bar-wrapper" onSubmit={handleSubmit}>
      <label htmlFor="searchbar"></label>
      <input type="text" name="searchbar" className="searchbar" onChange={handleInputChange} value={value} placeholder="Type to search ticker"></input>

      <button className="icon"><FontAwesomeIcon icon={faSearchDollar} /></button>
    </form>
  );
}


export default GraphSearchBar;