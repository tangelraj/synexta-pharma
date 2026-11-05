import React, { useEffect, useRef, useState } from "react";
import neurosynImage from "../assets/Container (7).png";
import pantosynImage from "../assets/Container (8).png";
import trypsynImage from "../assets/Container (9).png";
import cefixaImage from "../assets/Container (10).png";
import betasynImage from "../assets/Container (11).png";
import pregasynImage from "../assets/Container (12).png";
import pregasynForteImage from "../assets/Container (13).png";
import "./ProductsSection.css";

const products = [
  {
    name: "NEUROSYN-M™",
    category: "Neurological Health",
    description:
      "Alpha Lipoic Acid 200 mg + Benfotiamine 100 mg + Folic Acid 1.5 mg + Inositol 100 mg + Methylcobalamin 1000 mcg + Vitamin B6 3 mg",
    image: neurosynImage,
    prescriptionLabel: "RX Prescription Formulation",
    formAndPack: "Tablets • 10×10 Alu-Alu",
    indicationSegment: "Neuropathy & Neuroprotection",
    shelfLife: "24 Mos • Below 25°C",
    compliance: "WHO-GMP Certified",
    indications: [
      "Diabetic Peripheral Neuropathy",
      "Axon & Myelin Sheath Regeneration",
      "Neuronal Vascular & Metabolic Care",
      "Paresthesia & Hyperalgesia Relief",
    ],
    actives: [
      { amount: "200 mg", name: "Alpha Lipoic Acid" },
      { amount: "1000 mcg", name: "Methylcobalamin" },
      { amount: "100 mg", name: "Benfotiamine" },
    ],
  },
  {
    name: "PANTOSYN™ 20/40",
    category: "Gastrointestinal Health",
    description: "Pantoprazole 20 mg / 40 mg Tablets",
    image: pantosynImage,
  },
  {
    name: "TRYPSYN-R™",
    category: "Musculoskeletal Support",
    description: "Bromelain 90 mg + Rutoside Trihydrate 100 mg + Trypsin 48 mg",
    image: trypsynImage,
  },
  {
    name: "CEFIXA™ 200",
    category: "Other Formulations",
    description: "Cefixime 200 mg Tablets",
    image: cefixaImage,
  },
  {
    name: "BETASYN™ 8/16",
    category: "Other Formulations",
    description: "Betahistine 8 mg / 16 mg Tablets",
    image: betasynImage,
  },
  {
    name: "PREGASYN™ FORTE",
    category: "Neurological Health",
    description: "Pregabalin 75 mg + Methylcobalamin 1500 mcg",
    image: pregasynForteImage,
  },
  {
    name: "PREGASYN™",
    category: "Neurological Health",
    description: "Methylcobalamin 750 mcg + Pregabalin 50 mg",
    image: pregasynImage,
  },
];

const ProductsSection = () => {
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [showPaymentOptions, setShowPaymentOptions] = useState(false);
  const [selectedPaymentMethod, setSelectedPaymentMethod] = useState("");
  const [showDeliveryPopup, setShowDeliveryPopup] = useState(false);
  const dialogRef = useRef(null);

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;

    if (selectedProduct && !dialog.open) {
      dialog.showModal();
    } else if (!selectedProduct && dialog.open) {
      dialog.close();
    }
  }, [selectedProduct]);

  const closeDialog = () => {
    if (dialogRef.current?.open) {
      dialogRef.current.close();
    }
    setSelectedProduct(null);
    setShowPaymentOptions(false);
    setSelectedPaymentMethod("");
    setShowDeliveryPopup(false);
  };

  const handleDialogCancel = (event) => {
    event.preventDefault();
    closeDialog();
  };

  return (
    <section id="products" className="products-section" aria-labelledby="products-title">
      <header className="products-heading">
        <p className="products-eyebrow">Our Portfolio</p>
        <h2 id="products-title">Our Pharmaceutical Products</h2>
        <p className="products-intro">
          Explore our range of pharmaceutical formulations developed to support
          diverse healthcare needs.
        </p>
      </header>

      <div className="products-grid">
        {products.map((product) => (
          <article className="product-card" key={product.name}>
            <img className="product-image" src={product.image} alt={product.name} />
            <div className="product-details">
              <span className="product-category">{product.category}</span>
              <h3>{product.name}</h3>
              <span className="product-accent" aria-hidden="true" />
              <p>{product.description}</p>
              <button
                className="product-link"
                type="button"
                onClick={() => {
                  setSelectedProduct(product);
                  setShowPaymentOptions(false);
                  setSelectedPaymentMethod("");
                  setShowDeliveryPopup(false);
                }}
                aria-label={`View details for ${product.name}`}
              >
                View Product <span aria-hidden="true">→</span>
              </button>
            </div>
          </article>
        ))}
      </div>

      <dialog
        className="product-dialog"
        ref={dialogRef}
        aria-labelledby="product-dialog-title"
        onClose={closeDialog}
        onCancel={handleDialogCancel}
        onClick={(event) => {
          if (event.target === dialogRef.current) closeDialog();
        }}
      >
        {selectedProduct && (
          <>
            <header className="product-dialog-header">
              <div className="product-dialog-badges">
                <span className="product-dialog-category">
                  {selectedProduct.category}
                </span>
                <span className="product-dialog-prescription">
                  {selectedProduct.prescriptionLabel || "Product Information"}
                </span>
              </div>
              <button
                className="product-dialog-close"
                type="button"
                onClick={closeDialog}
                aria-label="Close product details"
              >
                <svg viewBox="0 0 24 24" aria-hidden="true">
                  <circle cx="12" cy="12" r="9" />
                  <path d="m9 9 6 6m0-6-6 6" />
                </svg>
              </button>
              <h2 id="product-dialog-title">{selectedProduct.name}</h2>
              <p>{selectedProduct.description}</p>
            </header>

            {showPaymentOptions ? (
              <div className="product-dialog-body product-payment-body">
                <button
                  className="product-payment-back"
                  type="button"
                  onClick={() => setShowPaymentOptions(false)}
                >
                  <span aria-hidden="true">←</span> Back to product
                </button>
                <section className="product-payment-options">
                  <h3>Choose a payment option</h3>
                  <p>
                    Select how you would like to pay for {selectedProduct.name}.
                  </p>
                  <div className="product-payment-methods">
                    {[
                      ["upi", "UPI"],
                      ["card", "Credit / Debit Card"],
                      ["netbanking", "Net Banking"],
                      ["cod", "Cash on Delivery"],
                    ].map(([value, label]) => (
                      <label
                        className={`product-payment-method${
                          selectedPaymentMethod === value ? " is-selected" : ""
                        }`}
                        key={value}
                      >
                        <input
                          type="radio"
                          name="paymentMethod"
                          value={value}
                          checked={selectedPaymentMethod === value}
                          onChange={() => {
                            setSelectedPaymentMethod(value);
                            setShowDeliveryPopup(false);
                          }}
                        />
                        <span>{label}</span>
                      </label>
                    ))}
                  </div>
                  <p className="product-payment-note" role="status">
                    Payment checkout is not configured yet. No payment will be
                    collected.
                  </p>
                  <button
                    className="product-payment-ok"
                    type="button"
                    disabled={!selectedPaymentMethod}
                    onClick={() => setShowDeliveryPopup(true)}
                  >
                    OK
                  </button>
                </section>
              </div>
            ) : (
            <div className="product-dialog-body">
              <div className="product-dialog-overview">
                <div className="product-dialog-image-wrap">
                  <img src={selectedProduct.image} alt={selectedProduct.name} />
                </div>
                <dl className="product-dialog-facts">
                  <div>
                    <dt>Form &amp; Pack</dt>
                    <dd>{selectedProduct.formAndPack || "See product packaging"}</dd>
                  </div>
                  <div>
                    <dt>Indication Segment</dt>
                    <dd>{selectedProduct.indicationSegment || selectedProduct.category}</dd>
                  </div>
                  <div>
                    <dt>Shelf Life &amp; Storage</dt>
                    <dd>{selectedProduct.shelfLife || "See product packaging"}</dd>
                  </div>
                  <div>
                    <dt>Compliance</dt>
                    <dd>{selectedProduct.compliance || "See product documentation"}</dd>
                  </div>
                </dl>
              </div>

              <section className="product-dialog-block">
                <h3>Key Therapeutic Indications</h3>
                <ul className="product-dialog-indications">
                  {(selectedProduct.indications || [
                    "Refer to product information for approved indications",
                  ]).map((indication) => (
                    <li
                      className={
                        selectedProduct.indications
                          ? ""
                          : "product-dialog-indication-placeholder"
                      }
                      key={indication}
                    >
                      <span aria-hidden="true">▧</span>
                      {indication}
                    </li>
                  ))}
                </ul>
              </section>

              <section className="product-dialog-block product-dialog-actives-block">
                <div className="product-dialog-block-heading">
                  <h3>Key Active Ingredients</h3>
                  <span>Standardized Pharmacopoeial Grade</span>
                </div>
                <ul className="product-dialog-actives">
                  {(selectedProduct.actives || [
                    { amount: "Composition", name: selectedProduct.description },
                  ]).map((active) => (
                    <li
                      className={
                        selectedProduct.actives
                          ? ""
                          : "product-dialog-active-placeholder"
                      }
                      key={active.name}
                    >
                      {active.amount && <strong>{active.amount}</strong>}
                      <span>{active.name}</span>
                    </li>
                  ))}
                </ul>
              </section>

              <button
                className="product-dialog-buy"
                type="button"
                onClick={() => setShowPaymentOptions(true)}
              >
                Buy Now <span aria-hidden="true">→</span>
              </button>
            </div>
            )}
          </>
        )}
        {showDeliveryPopup && selectedProduct && (
          <div
            className="product-delivery-overlay"
            onClick={(event) => {
            if (event.target === event.currentTarget) {
              setShowDeliveryPopup(false);
            }
            }}
          >
            <section
            className="product-delivery-popup"
            role="alertdialog"
            aria-modal="true"
            aria-labelledby="product-delivery-title"
            aria-describedby="product-delivery-description product-delivery-note"
            >
            <span className="product-delivery-check" aria-hidden="true">
              ✓
            </span>
            <h3 id="product-delivery-title">Thank you!</h3>
            <p id="product-delivery-description">
              Your product will be delivered soon after your order is
              confirmed.
            </p>
            <p className="product-delivery-note" id="product-delivery-note">
              This is a demo. No order has been placed and no payment has
              been processed.
            </p>
            <button
              className="product-delivery-close"
              type="button"
              onClick={() => setShowDeliveryPopup(false)}
            >
              OK
            </button>
            </section>
          </div>
        )}
      </dialog>
    </section>
  );
};

export default ProductsSection;
