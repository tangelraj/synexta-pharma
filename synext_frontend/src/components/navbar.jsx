
import React, { useState } from "react";
import logo from "../assets/logo.png";
import "./navbar.css";

const Navbar = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const closeMenu = () => setMenuOpen(false);

  return (
    <header className="site-header">
      <nav className="navbar" aria-label="Main navigation">
        <a className="brand" href="/" aria-label="Synexta Pharma home">
          <img src={logo} alt="Synexta Pharma" />
        </a>

        <button
          className="menu-toggle"
          type="button"
          aria-label={menuOpen ? "Close navigation menu" : "Open navigation menu"}
          aria-expanded={menuOpen}
          aria-controls="primary-navigation"
          onClick={() => setMenuOpen((isOpen) => !isOpen)}
        >
          <span />
          <span />
          <span />
        </button>

        <div
          id="primary-navigation"
          className={`nav-menu${menuOpen ? " is-open" : ""}`}
        >
          <div className="nav-links">
            <a href="/#home" onClick={closeMenu}>Home</a>
            <a href="/#about" onClick={closeMenu}>About Us</a>
            <a href="/#products" onClick={closeMenu}>Products</a>
            <a href="/#why-us" onClick={closeMenu}>Why choose Us</a>
            <a href="/#quality" onClick={closeMenu}>Quality Assurance</a>
            <a href="/#contact" onClick={closeMenu}>Contact</a>
          </div>

          <a href="/#products" className="explore-btn" onClick={closeMenu}>
            Explore Products
          </a>
        </div>
      </nav>
    </header>
  );
};

export default Navbar;
