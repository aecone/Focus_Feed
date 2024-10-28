import React from 'react';
import Navbar from './components/Navbar/Navbar';
import SearchBar from './components/SearchBar/SearchBar';
import Feed from './components/Feed/Feed';
import './App.css';

function App() {
  return (
    <div className="App">
      <Navbar />
      <SearchBar />
      <Feed />
    </div>
  );
}

export default App;