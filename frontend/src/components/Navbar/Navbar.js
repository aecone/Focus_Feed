import React from 'react';
import './Navbar.css';
import logo from '../../assets/images/logo.svg'; // Adjust path based on your setup

function Navbar() {
  return (
    <header className="navbar-container">
      <div className="logo-container">
        <img src={logo} alt="FocusFeed Logo" className="logo" />
      </div>
      <nav>
        <ul className="navbar-links">
          <li><a href="#">Feed</a></li>
          <li><a href="#">Follow</a></li>
          <li><a href="#">Profile</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Navbar;