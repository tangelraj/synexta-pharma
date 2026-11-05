import React from "react";
import heroImage from "../assets/HeroSection.png";
import "./QualitySection.css";

const commitments = [
  {
    title: "Commitment to Quality",
    description: "Quality guides every product we bring to market.",
    icon: (
      <>
        <circle cx="12" cy="8" r="4.25" />
        <path d="m9.2 11.2-1 8 3.8-2.4 3.8 2.4-1-8" />
      </>
    ),
  },
  {
    title: "Product Information Transparency",
    description: "Clear, accurate compositions for every formulation.",
    icon: (
      <>
        <path d="M7 3.5h7l5 5V20a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4.5a1 1 0 0 1 1-1Z" />
        <path d="M14 3.5v5h5M9 13h6M9 16.5h6" />
      </>
    ),
  },
  {
    title: "Consistent Brand Standards",
    description: "A uniform standard of presentation across our range.",
    icon: (
      <>
        <path d="m12 3 8 3v5.5c0 5-3.4 8.2-8 9.5-4.6-1.3-8-4.5-8-9.5V6l8-3Z" />
        <path d="m9 12 2 2 4-4" />
      </>
    ),
  },
  {
    title: "Healthcare Professional Support",
    description: "Responsive help for professionals and partners.",
    icon: (
      <>
        <path d="M16 20v-1.5a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4V20" />
        <circle cx="9.5" cy="7" r="4" />
        <path d="M17 11a4 4 0 0 0 0-8M21 20v-1.5a4 4 0 0 0-3-3.87" />
      </>
    ),
  },
];

const QualitySection = () => {
  return (
    <section
      className="quality-section"
      id="quality"
      style={{ "--quality-background": `url("${heroImage}")` }}
      aria-labelledby="quality-title"
    >
      <div className="quality-content">
        <header className="quality-heading">
          <p>Quality Assurance</p>
          <h2 id="quality-title">
            Quality at the Heart of Every
            <br />
            Formulation
          </h2>
        </header>

        <div className="quality-grid">
          {commitments.map((commitment) => (
            <article className="quality-card" key={commitment.title}>
              <span className="quality-icon" aria-hidden="true">
                <svg
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="1.8"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  {commitment.icon}
                </svg>
              </span>
              <h3>{commitment.title}</h3>
              <p>{commitment.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default QualitySection;
