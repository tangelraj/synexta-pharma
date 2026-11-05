import React from "react";
import researcherImage from "../assets/Medical researcher using laboratory microscope.png";
import "./AboutSection.css";

const features = [
  {
    title: "Quality-Focused Approach",
    description: "Every formulation is presented with care, clarity and consistency.",
    icon: (
      <>
        <circle cx="12" cy="8" r="4.25" />
        <path d="m9.2 11.2-1 8 3.8-2.4 3.8 2.4-1-8" />
      </>
    ),
  },
  {
    title: "Reliable Pharmaceutical Solutions",
    description: "A focused portfolio built around everyday healthcare needs.",
    icon: (
      <>
        <path d="M9 3h6" />
        <path d="M10 3v6.2l-5.3 8.5A1.5 1.5 0 0 0 6 20h12a1.5 1.5 0 0 0 1.3-2.3L14 9.2V3" />
        <path d="M7.5 15h9" />
      </>
    ),
  },
  {
    title: "Healthcare-Centered Commitment",
    description: "We work alongside healthcare professionals for better patient care.",
    icon: (
      <>
        <path d="M20.8 8.8c0 4.1-8.8 10-8.8 10s-8.8-5.9-8.8-10a4.6 4.6 0 0 1 8.8-1.7 4.6 4.6 0 0 1 8.8 1.7Z" />
        <path d="M4.5 11h4l1.5-2.5 2.2 5 1.7-2.5h5.6" />
      </>
    ),
  },
];

const AboutSection = () => {
  return (
    <section id="about" className="about-section" aria-labelledby="about-title">
      <div className="about-layout">
        <img
          className="about-image"
          src={researcherImage}
          alt="A pharmaceutical researcher working with a microscope in a laboratory"
        />

        <div className="about-content">
          <p className="about-eyebrow">About Synexta Pharma</p>
          <h2 id="about-title">Committed to Quality. Focused on Care.</h2>
          <p className="about-description">
            Synexta Pharma offers a range of pharmaceutical formulations
            designed to support diverse healthcare needs. Our approach is built
            on quality, transparency and a genuine commitment to trusted
            healthcare solutions.
          </p>

          <ul className="about-features">
            {features.map((feature) => (
              <li className="about-feature" key={feature.title}>
                <span className="about-feature-icon" aria-hidden="true">
                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.8"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    {feature.icon}
                  </svg>
                </span>
                <span className="about-feature-copy">
                  <strong>{feature.title}</strong>
                  <span>{feature.description}</span>
                </span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </section>
  );
};

export default AboutSection;
