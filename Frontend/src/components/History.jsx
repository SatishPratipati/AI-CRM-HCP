import { useEffect, useState } from "react";
import axios from "axios";

function History() {

  const [items, setItems] = useState([]);

  useEffect(() => {

    load();

  }, []);

  const load = async () => {

    const res = await axios.get(
      "http://127.0.0.1:8000/interactions/"
    );

    setItems(res.data);

  };

  return (

    <div className="card">

      <h2>Recent Interaction</h2>

      {

        items.map((item) => (
  <div
    key={item.id}
    style={{
      background: "#f8fafc",
      padding: "15px",
      borderRadius: "10px",
      marginBottom: "15px",
      border: "1px solid #e5e7eb",
    }}
  >
    <h3>👨‍⚕️ {item.hcp_name}</h3>

    <p><strong>🏥 Hospital:</strong> {item.hospital}</p>

    <p><strong>💊 Summary:</strong> {item.summary}</p>

    <p><strong>📅 Follow Up:</strong> {item.follow_up}</p>
  </div>
))
      }

    </div>

  );

}

export default History;