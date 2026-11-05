import React from "react";
import pipettingImage from "../assets/Image (Researcher pipetting samples in a laboratory).png";
import "./WhyChooseUsSection.css";

const reasons = [
  {
    title: "Quality first",
    description: "Formulations selected and presented with a focus on quality.",
  },
  {
    title: "Product clarity",
    description: "Exact names, strengths and compositions — nothing hidden.",
  },
  {
    title: "Responsible communication",
    description: "Accurate information without exaggerated claims.",
  },
  {
    title: "Professional engagement",
    description: "A team that listens to healthcare professionals and partners.",
  },
];

const WhyChooseUsSection = () => (
  <section id="why-choose-us" className="why-choose-section" aria-labelledby="why-choose-title">
    <div className="why-choose-layout">
      <div className="why-choose-content">
        <p className="why-choose-eyebrow">Why Choose Us</p>
        <h2 id="why-choose-title">Why Choose Synexta Pharma?</h2>
        <p className="why-choose-intro">
          We keep things simple: dependable products, clear information and a
          people-first approach.
        </p>

        <ul className="why-choose-list">
          {reasons.map((reason) => (
            <li className="why-choose-item" key={reason.title}>
              <span className="why-choose-check" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none">
                  <circle cx="12" cy="12" r="9" />
                  <path d="m8.5 12 2.3 2.3 4.8-4.8" />
                </svg>
              </span>
              <span className="why-choose-copy">
                <strong>{reason.title}</strong>
                <span>{reason.description}</span>
              </span>
            </li>
          ))}
        </ul>
      </div>

      <img
        className="why-choose-image"
        src={pipettingImage}
        alt="A researcher pipetting samples in a laboratory"
      />
    </div>
  </section>
);

export default WhyChooseUsSection;
