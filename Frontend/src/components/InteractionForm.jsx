import { useState } from "react";
import axios from "axios";

function InteractionForm() {
  const [form, setForm] = useState({
    hcp_name: "",
    hospital: "",
    specialization: "",
    discussion: "",
    summary: "",
    follow_up: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const generateSummary = async () => {
  try {

    const response = await axios.post(
      "http://127.0.0.1:8000/ai/chat",
      {
        message: form.discussion
      }
    );

    setForm({
      ...form,
      summary: response.data.response
    });

  } catch (error) {

    console.log(error);

    alert("Unable to generate AI summary.");

  }
};

  const saveInteraction = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/interactions/", form);

      alert("Interaction Saved");

      setForm({
        hcp_name: "",
        hospital: "",
        specialization: "",
        discussion: "",
        summary: "",
        follow_up: "",
      });
    } catch (err) {
      alert("Error Saving");
      console.log(err);
    }
  };

  return (
    <div className="card">

      <h2>Log Interaction</h2>

      <label>Doctor Name</label>
      <input
        name="hcp_name"
        placeholder="Enter Doctor Name"
        value={form.hcp_name}
        onChange={handleChange}
      />
      <label>Hospital</label>
      <input
        name="hospital"
        placeholder="Hospital"
        value={form.hospital}
        onChange={handleChange}
      />
      <label>Specialization</label>
      <input
        name="specialization"
        placeholder="Specialization"
        value={form.specialization}
        onChange={handleChange}
      />
      <label>Discussion</label>
      <textarea
        name="discussion"
        placeholder="Discussion"
        value={form.discussion}
        onChange={handleChange}
      />
      <button
  type="button"
  onClick={generateSummary}
  style={{ marginBottom: "15px" }}
>
  ✨ Generate AI Summary
</button>
      <textarea
  name="summary"
  value={form.summary}
  readOnly
/>
      <label>Follow Up</label>
      <input
        name="follow_up"
        placeholder="Follow Up"
        value={form.follow_up}
        onChange={handleChange}
      />

      <button onClick={saveInteraction}>
        Save Interaction
      </button>

    </div>
  );
}

export default InteractionForm;