import React from "react";
import { SignedIn, SignedOut, UserButton } from "@clerk/clerk-react";
import { Outlet, Link, Navigate } from "react-router-dom";

const Layout = () => {
  return (
    <div className="app-layout">
      <header className="app-header">
        <div className="header-content">
          <h1>Code Quest AI</h1>
          <SignedIn>
            <nav>
              <Link to="/">Generate</Link>
              <Link to="/history">History</Link>
              <UserButton afterSignOutUrl="/sign-in" />
            </nav>
          </SignedIn>
        </div>
      </header>
      <main className="app-main">
        <SignedOut>
          <Navigate to="/sign-in" replace />
        </SignedOut>
        <SignedIn>
          <Outlet />
        </SignedIn>
      </main>
    </div>
  );
};

export default Layout;
