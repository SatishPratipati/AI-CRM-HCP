import Header from "./components/Header";
import InteractionForm from "./components/InteractionForm";
import ChatPanel from "./components/ChatPanel";
import History from "./components/History";
import Footer from "./components/Footer";

import "./App.css";

function App() {
  return (
    <div className="container">

      <Header />

      <div className="stats">

  <div className="stat-card">
    <h3>25</h3>
    <p>Total Interactions</p>
  </div>

  <div className="stat-card">
    <h3>6</h3>
    <p>Today's Visits</p>
  </div>

  <div className="stat-card">
    <h3>4</h3>
    <p>Pending Follow-ups</p>
  </div>

</div>

      <div className="top">

        <div className="left">

          <InteractionForm />

        </div>

        <div className="right">

          <ChatPanel />

        </div>

      </div>

      <History />

      <Footer />

    </div>
  );
}

export default App;