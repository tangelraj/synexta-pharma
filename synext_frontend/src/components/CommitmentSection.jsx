import React from "react";
import backgroundImage from "../assets/QualityCommitmentSection.png";
import "./CommitmentSection.css";

const commitments = [
  {
    title: "Commitment to Quality",
    icon: (
      <>
        <circle cx="12" cy="12" r="8" />
        <path d="M7.5 12h8M13 9.5l2.5 2.5-2.5 2.5" />
      </>
    ),
  },
  {
    title: "Product Information Transparency",
    icon: (
      <>
        <path d="M7 3.5h7l5 5V20a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4.5a1 1 0 0 1 1-1Z" />
        <path d="M14 3.5v5h5M9 12h6M9 15h4M15 17l2 2" />
      </>
    ),
  },
  {
    title: "Consistent Brand Standards",
    icon: (
      <>
        <path d="m12 3 2.2 2 3-.1.8 2.9 2.1 2-1.2 2.8.6 2.9-2.7 1.4-1.4 2.6-3-.6-2.8 1.2-2-2.1-2.9-.8.1-3L3 12l2-2.2-.1-3 2.9-.8 2-2.1 2.2 1.1Z" />
        <path d="m9 12 2 2 4-4" />
      </>
    ),
  },
  {
    title: "Healthcare Professional Support",
    icon: (
      <>
        <circle cx="9" cy="8" r="3" />
        <path d="M3.5 20v-1.5a5.5 5.5 0 0 1 11 0V20h-11Z" />
        <path d="M16 5.5a3 3 0 0 1 0 5.8M18 14a4.5 4.5 0 0 1 2.5 4.1V20" />
      </>
    ),
  },
];

const CommitmentSection = () => (
  <section
    className="commitment-section"
    style={{ "--commitment-background": `url("${backgroundImage}")` }}
    aria-labelledby="commitment-title"
  >
    <div className="commitment-content">
      <header className="commitment-heading">
        <p>Our Commitment</p>
        <h2 id="commitment-title">Quality at the Heart of Every Formulation</h2>
      </header>

      <div className="commitment-grid">
        {commitments.map((commitment) => (
          <article className="commitment-card" key={commitment.title}>
            <span className="commitment-icon" aria-hidden="true">
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
          </article>
        ))}
      </div>
    </div>
  </section>
);

export default CommitmentSection;
