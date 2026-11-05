import React from "react";
import connectBackground from "../assets/ConnectCTASection.png";
import "./ConnectSection.css";

const ConnectSection = () => (
  <section
    className="connect-section"
    style={{ "--connect-background": `url("${connectBackground}")` }}
    aria-labelledby="connect-title"
  >
    <div className="connect-content">
      <p className="connect-eyebrow">Let's Connect</p>
      <h2 id="connect-title">Let's Connect for Better Healthcare Solutions</h2>
      <p className="connect-description">
        Connect with our team to learn more about our pharmaceutical product
        portfolio and business enquiries.
      </p>
      <div className="connect-actions">
        <a className="connect-button connect-button-primary" href="/contact">
          Contact Us <span aria-hidden="true">→</span>
        </a>
        <a className="connect-button connect-button-secondary" href="/products">
          Explore Products
        </a>
      </div>
    </div>
  </section>
);

export default ConnectSection;
