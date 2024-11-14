import React from 'react';
import { SignedIn, SignedOut, SignInButton, SignUpButton, UserButton } from '@clerk/clerk-react';
import './LoginPage.css';

const Login = () => {
  return (
    <div className="login-container">
      <h2>Welcome to Focus Feed</h2>

      {/* Show SignInButton and SignUpButton if the user is signed out */}
      <SignedOut>
        <p>Please sign in or register to continue:</p>
        <div className="auth-buttons">
          <SignInButton />
          <SignUpButton />
        </div>
      </SignedOut>

      {/* Show UserButton if the user is signed in */}
      <SignedIn>
        <p>You are already signed in!</p>
        <UserButton />
      </SignedIn>
    </div>
  );
};

export default Login;