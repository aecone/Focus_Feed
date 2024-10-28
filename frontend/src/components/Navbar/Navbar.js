import React from 'react';
import './Navbar.css';

function Navbar() {
  return (
    <header className="navbar-container">
      <div className="logo">FocusFeed</div>
      <nav className="navbar">
        <ul>
          <li><a href="#">Feed</a></li>
          <li><a href="#">Follow</a></li>
          <li><a href="#">Profile</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Navbar;