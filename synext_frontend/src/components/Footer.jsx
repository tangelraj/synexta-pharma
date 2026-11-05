import React from "react";
import logo from "../assets/logo.png";
import "./Footer.css";

const quickLinks = [
  { label: "Home", href: "#home" },
  { label: "About Us", href: "#about" },
  { label: "Products", href: "#products" },
  { label: "Our Expertise", href: "#why-choose-us" },
  { label: "Quality Assurance", href: "#quality" },
  { label: "Contact", href: "#contact" },
];

const productLinks = [
  [
    { label: "NEUROSYN-M™", href: "/products" },
    { label: "TRYPSYN-R™", href: "/products" },
    { label: "BETASYN™ 8/16", href: "/products" },
    { label: "PREGASYN™", href: "/products" },
  ],
  [
    { label: "PANTOSYN™ 20/40", href: "/products" },
    { label: "CEFIXA™ 200", href: "/products" },
    { label: "PREGASYN™ FORTE", href: "/products" },
  ],
];

const Footer = () => (
  <footer className="site-footer">
    <div className="footer-main">
      <div className="footer-brand">
        <a href="#home" aria-label="Synexta Pharma home">
          <img src={logo} alt="Synexta Pharma" />
        </a>
        <p>Quality Medicines. Trusted Care.</p>
      </div>

      <nav className="footer-quick-links" aria-label="Footer quick links">
        <h2>Quick Links</h2>
        <ul>
          {quickLinks.map((link) => (
            <li key={link.label}>
              <a href={link.href}>{link.label}</a>
            </li>
          ))}
        </ul>
      </nav>

      <nav className="footer-products" aria-label="Footer products">
        <h2>Products</h2>
        <div className="footer-product-columns">
          {productLinks.map((column, index) => (
            <ul key={index}>
              {column.map((product) => (
                <li key={product.label}>
                  <a href={product.href}>{product.label}</a>
                </li>
              ))}
            </ul>
          ))}
        </div>
      </nav>
    </div>

    <div className="footer-bottom">
      <p>© 2026 Synexta Pharma. All rights reserved.</p>
      <nav aria-label="Legal links">
        <a href="/privacy-policy">Privacy Policy</a>
        <a href="/terms-and-conditions">Terms and Conditions</a>
      </nav>
    </div>
  </footer>
);

export default Footer;
