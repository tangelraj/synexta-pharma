import React from "react";

import Navbar from "./components/navbar";
import HeroSection from "./components/HeroSection";
import AboutSection from "./components/AboutSection";
import ProductsSection from "./components/ProductsSection";
import WhyChooseUsSection from "./components/WhyChooseUsSection";
import QualitySection from "./components/QualitySection";
import CommitmentSection from "./components/CommitmentSection";
import ConnectSection from "./components/ConnectSection";
import ContactSection from "./components/ContactSection";
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Navbar />
      <HeroSection />
      <AboutSection />
      <ProductsSection />
      <WhyChooseUsSection />
      <QualitySection />
      <CommitmentSection />
      <ConnectSection />
      <ContactSection />
      <Footer />
    </>
  );
}

export default App;