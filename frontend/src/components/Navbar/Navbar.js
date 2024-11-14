import React from 'react';
import './Navbar.css';
import logo from '../../assets/images/logo.svg';
import { UserButton } from '@clerk/clerk-react';

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
      {/* UserButton for profile and log out options */}
      <div className="user-button-container">
        <UserButton />
      </div>
    </header>
  );
}

export default Navbar;