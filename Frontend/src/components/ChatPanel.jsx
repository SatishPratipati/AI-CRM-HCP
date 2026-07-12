import { useState } from "react";
import axios from "axios";

function ChatPanel() {

  const [message, setMessage] = useState("");

  const [reply, setReply] = useState("");

  const askAI = async () => {

    const res = await axios.post(
      "http://127.0.0.1:8000/ai/chat",
      {
        message,
      }
    );

    setReply(res.data.response);
  };

  return (
    <div className="card">

      <h2>🤖 AI Assistant</h2>

      <textarea
        rows={7}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Chat with AI..."
      />

      <button onClick={askAI}>
        Ask AI Assisstant
      </button>

      <h3>AI Generated Recommendation</h3>

      <div className="response">

  <h3>🤖 AI Recommendation</h3>

  <hr />

  <p>{reply}</p>

</div>
    </div>
  );
}

export default ChatPanel;