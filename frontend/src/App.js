import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { SignedIn, SignedOut } from '@clerk/clerk-react';
import Navbar from './components/Navbar/Navbar';
import SearchBar from './components/SearchBar/SearchBar';
import Feed from './components/Feed/Feed';
import LoginPage from './components/LoginPage/LoginPage';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        {/* If the user is signed in, show the main content */}
        <SignedIn>
          <Navbar />
          <SearchBar />
          <Feed />
        </SignedIn>

        {/* If the user is not signed in, show the LoginPage component */}
        <SignedOut>
          <Routes>
            <Route path="/" element={<LoginPage />} />
          </Routes>
        </SignedOut>
      </div>
    </Router>
  );
}

export default App;