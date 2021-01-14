import React, { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearchDollar } from '@fortawesome/free-solid-svg-icons'
import './GraphSearchBar.css';
import useDebounce from './use-debounce.jsx';


const GraphSearchBar = ({ callback, autosuggest, suggestionsArray }) => {
  const [value, setValue] = useState('');
  const [inputChange, setInputChange] = useState(false);
  const [selectDropDown, setselectDropDown] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [suggestions, setSuggestions] = useState([]);
  const [suggestionsBool, setsuggestionsBool] = useState(false);


  const handleInputChange = (e) => {
    e.persist();
    setValue(e.target.value.toUpperCase());
    setInputChange(true);
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  }

   const handleSelection = (e) => {
    setValue(e.target.innerHTML.toUpperCase())
    setSuggestions([]);
    setselectDropDown(true)
   }

  useEffect(() => {
    console.log('use effect')
    if (inputChange) {
      console.log('input changed')
      autosuggest(value)
      setInputChange(false);
      setsuggestionsBool(true)
    } else if (selectDropDown) {
      console.log('selectDropDown')
      setselectDropDown(false)
      setsuggestionsBool(false)
    } else if (suggestionsBool) {
      setSuggestions(suggestionsArray)
    }
  }, [inputChange, suggestionsArray, autosuggest, value, selectDropDown, suggestionsBool])

  useEffect(() => {
    if (submitted) {
      console.log('submitted')
      callback(value)
      setSubmitted(false);
      setValue('')
    }
  }, [submitted, callback, value])

  return (
    <form className="search-bar-wrapper" onSubmit={handleSubmit} autoComplete="off">
      <label htmlFor="searchbar"></label>
      <input type="text" name="searchbar" className="searchbar" onChange={handleInputChange} value={value} placeholder="Type to search ticker"></input>
      <div className="autosuggestion-wrapper">
        {suggestions.map(a => <li key={a} className="autosuggestion-bullet" value={a} onClick={handleSelection}>{a}</li>)}
      </div>
      <button className="icon"><FontAwesomeIcon icon={faSearchDollar} /></button>
    </form>
  );
}


export default GraphSearchBar;