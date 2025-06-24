import React from "react";
import { SignIn, SignUp, SignedIn, SignedOut } from "@clerk/clerk-react";

const AuthenticationPage = () => {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: '100vh',
      width: '100%',
      backgroundColor: 'var(--primary-bg)'
    }}>
      <div style={{
        width: '100%',
        maxWidth: '420px',
        padding: '2rem',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '2rem'
      }}>
        <SignedOut>
          <div style={{ width: '100%' }}>
            <SignIn routing="path" path="/sign-in" />
          </div>
          <div style={{ width: '100%' }}>
            <SignUp routing="path" path="/sign-up" />
          </div>
        </SignedOut>

        <SignedIn>
          <div className="redirect-message">
            <p>You are signed in</p>
          </div>
        </SignedIn>
      </div>
    </div>
  );
};

export default AuthenticationPage;
