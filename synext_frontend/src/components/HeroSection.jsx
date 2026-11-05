import React, { useEffect, useState } from "react";
import heroImage from "../assets/HeroSection.png";
import { getHome } from "../services/api";
import "./HeroSection.css";

const HeroSection = () => {
  const [home, setHome] = useState(null);

  useEffect(() => {
    getHome()
      .then((data) => {
        if (data.title) {
          setHome(data);
        }
      })
      .catch((error) => {
        console.error("Error loading home data:", error);
      });
  }, []);

  const backgroundImage = home?.banner_image || heroImage;

  return (
    <section
      className="hero"
      id="home"
      style={{ "--hero-image": `url("${backgroundImage}")` }}
      aria-labelledby="hero-title"
    >
      <div className="hero-content">
        <p className="hero-eyebrow">
          Trusted Pharmaceutical Solutions
        </p>

        <h1 id="hero-title">
          {home?.title || (
            <>
              Quality Medicines.
              <br />
              Trusted Care.
            </>
          )}
        </h1>

        <p className="hero-description">
          {home?.subtitle ||
            "Committed to delivering quality-driven pharmaceutical formulations that support healthcare professionals and better patient care."}
        </p>

        <div className="hero-actions">
          <a
            className="hero-button hero-button-primary"
            href={home?.button_link || "/#products"}
          >
            {home?.button_text || "Explore Our Products"}
            <span aria-hidden="true"> →</span>
          </a>

          <a
            className="hero-button hero-button-secondary"
            href="/#contact"
          >
            Contact Our Team
          </a>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;