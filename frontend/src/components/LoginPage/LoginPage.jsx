import React from 'react';
import { SignedIn, SignedOut, SignInButton, UserButton } from '@clerk/clerk-react';

const Login = () => {
  return (
    <div className="login-container">
      <h2>Welcome to Focus Feed</h2>

      {/* Show SignInButton if the user is signed out */}
      <SignedOut>
        <p>Please sign in to continue:</p>
        <SignInButton />
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