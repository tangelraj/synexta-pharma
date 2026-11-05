import React from "react";
import heroImage from "../assets/HeroSection.png";
import "./HeroSection.css";

const HeroSection = () => {
  return (
    <section
      className="hero"
      id="home"
      style={{ "--hero-image": `url("${heroImage}")` }}
      aria-labelledby="hero-title"
    >
      <div className="hero-content">
        <p className="hero-eyebrow">Trusted Pharmaceutical Solutions</p>
        <h1 id="hero-title">
          Quality Medicines.
          <br />
          Trusted Care.
        </h1>
        <p className="hero-description">
          Committed to delivering quality-driven pharmaceutical formulations
          that support healthcare professionals and better patient care.
        </p>
        <div className="hero-actions">
          <a className="hero-button hero-button-primary" href="/products">
            Explore Our Products <span aria-hidden="true">→</span>
          </a>
          <a className="hero-button hero-button-secondary" href="/contact">
            Contact Our Team
          </a>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
