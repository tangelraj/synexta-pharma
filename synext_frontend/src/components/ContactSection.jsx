
import React, { useEffect, useState } from "react";
import { getContact, submitEnquiry } from "../services/api";
import "./ContactSection.css";

const contactTopics = [
  {
    label: "Product information requests",
    icon: (
      <>
        <path d="m9.5 14.5 5-5a3.54 3.54 0 0 1 5 5l-3 3a3.54 3.54 0 0 1-5 0" />
        <path d="m14.5 9.5-5 5a3.54 3.54 0 0 1-5-5l3-3a3.54 3.54 0 0 1 5 0" />
      </>
    ),
  },
  {
    label: "Distribution & business partnerships",
    icon: (
      <>
        <path d="M16 20v-1.5a4 4 0 0 0-4-4H7a4 4 0 0 0-4 4V20" />
        <circle cx="9.5" cy="7" r="4" />
        <path d="M17 11a4 4 0 0 0 0-8M21 20v-1.5a4 4 0 0 0-3-3.87" />
      </>
    ),
  },
  {
    label: "Healthcare professional support",
    icon: (
      <>
        <path d="M6 4v5a6 6 0 0 0 12 0V7" />
        <path d="M6 4H4v3h4V4H6Zm12 3h-2v3h4V7h-2Z" />
        <path d="M12 15v2a3 3 0 0 0 6 0v-1" />
        <circle cx="18" cy="15" r="1.5" />
      </>
    ),
  },
];

const ContactSection = () => {
  const [contact, setContact] = useState(null);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");
  const [isSuccess, setIsSuccess] = useState(false);

  useEffect(() => {
    let cancelled = false;

    getContact()
      .then((data) => {
        if (!cancelled && data.heading) {
          setContact(data);
        }
      })
      .catch((error) => {
        console.error("Error loading Contact data:", error);
      });

    return () => {
      cancelled = true;
    };
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const form = event.currentTarget;
    const data = Object.fromEntries(new FormData(form).entries());

    const name = (data.name || "").trim();
    const email = (data.email || "").trim();
    const phone = (data.phone || "").trim();
    const message = (data.message || "").trim();

    setStatus("");
    setIsSuccess(false);

    if (name.length < 3 || !/^[A-Za-z ]+$/.test(name)) {
      setStatus("Please enter a valid name with at least 3 letters.");
      return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setStatus("Please enter a valid email address.");
      return;
    }

    if (phone && !/^[0-9]{10}$/.test(phone)) {
      setStatus("Phone number must contain exactly 10 digits.");
      return;
    }

    if (!data.enquiryType) {
      setStatus("Please select an enquiry type.");
      return;
    }

    if (message.length < 10) {
      setStatus("Message must contain at least 10 characters.");
      return;
    }

    setLoading(true);

    try {
      await submitEnquiry({
        ...data,
        name,
        email,
        phone,
        message,
      });

      setIsSuccess(true);
      setStatus("Your enquiry has been submitted successfully!");
      form.reset();
    } catch (error) {
      setIsSuccess(false);
      setStatus(
        error.message || "Unable to send enquiry. Please try again."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <section
      id="contact"
      className="contact-section"
      aria-labelledby="contact-title"
    >
      <div className="contact-layout">
        <div className="contact-information">
          <p className="contact-eyebrow">Contact</p>

          <h2 id="contact-title">
            {contact?.heading || "Get in Touch"}
          </h2>

          <p className="contact-intro">
            {contact?.description ||
              "Have a question about our products or a business enquiry? Send us a message and our team will get back to you."}
          </p>

          <ul className="contact-topics">
            {contactTopics.map((topic) => (
              <li className="contact-topic" key={topic.label}>
                <span
                  className="contact-topic-icon"
                  aria-hidden="true"
                >
                  <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="1.8"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    {topic.icon}
                  </svg>
                </span>

                <span>{topic.label}</span>
              </li>
            ))}
          </ul>
        </div>

        <form className="contact-form" onSubmit={handleSubmit}>
          <div className="contact-field-grid">
            <label className="contact-field">
              <span>Name *</span>
              <input
                name="name"
                type="text"
                autoComplete="name"
                minLength={3}
                maxLength={100}
                pattern="[A-Za-z ]{3,}"
                title="Enter at least 3 letters"
                required
              />
            </label>

            <label className="contact-field">
              <span>Business email *</span>
              <input
                name="email"
                type="email"
                autoComplete="email"
                maxLength={254}
                required
              />
            </label>

            <label className="contact-field">
              <span>Phone number</span>
              <input
                name="phone"
                type="tel"
                autoComplete="tel"
                inputMode="numeric"
                pattern="[0-9]{10}"
                maxLength={10}
                title="Enter exactly 10 digits"
              />
            </label>

            <label className="contact-field">
              <span>Company / Organization</span>
              <input
                name="company"
                type="text"
                autoComplete="organization"
              />
            </label>

            <label className="contact-field contact-field-full">
              <span>Enquiry type *</span>
              <select
                name="enquiryType"
                defaultValue=""
                required
              >
                <option value="" disabled>
                  Select an option
                </option>

                <option value="product-information">
                  Product information requests
                </option>

                <option value="business-partnership">
                  Distribution &amp; business partnerships
                </option>

                <option value="healthcare-support">
                  Healthcare professional support
                </option>

                <option value="other">Other</option>
              </select>
            </label>

            <label className="contact-field contact-field-full">
              <span>Message *</span>
              <textarea
                name="message"
                rows={4}
                minLength={10}
                maxLength={2000}
                required
              />
            </label>
          </div>

          <button
            className="contact-submit"
            type="submit"
            disabled={loading}
          >
            {loading ? "Sending..." : "Submit Enquiry"}
          </button>

          {status && (
            <p
              role="status"
              aria-live="polite"
              style={{
                marginTop: "15px",
                color: isSuccess ? "green" : "red",
                fontWeight: "600",
              }}
            >
              {status}
            </p>
          )}
        </form>
      </div>
    </section>
  );
};

export default ContactSection;
