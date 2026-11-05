const API_URL = (
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"
).replace(/\/$/, "");

export async function getHome() {
  const API_URL =
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

  const response = await fetch(`${API_URL}/api/home/`);

  if (!response.ok) {
    throw new Error("Failed to load home data");
  }

  return response.json();
}
export async function getAbout() {
  const API_URL = (
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"
  ).replace(/\/$/, "");

  const response = await fetch(`${API_URL}/api/about/`);

  if (!response.ok) {
    throw new Error(`About API failed: ${response.status}`);
  }

  return response.json();
}
export async function getProducts() {
  const API_URL = (
    import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"
  ).replace(/\/$/, "");

  const response = await fetch(`${API_URL}/api/products/`);

  if (!response.ok) {
    throw new Error(`Products API failed: ${response.status}`);
  }

  return response.json();
}
const CONTACT_API_URL = (
  import.meta.env.VITE_API_URL || "http://127.0.0.1:8000"
).replace(/\/$/, "");

export async function getContact() {
  const response = await fetch(`${CONTACT_API_URL}/api/contact/`);

  if (!response.ok) {
    throw new Error(`Contact API failed: ${response.status}`);
  }

  return response.json();
}

export async function submitEnquiry(data) {
  const response = await fetch(
    `${CONTACT_API_URL}/api/submit-enquiry/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    }
  );

  const result = await response.json();

  if (!response.ok) {
    throw new Error(result.error || "Unable to send enquiry right now.");
  }

  return result;
}