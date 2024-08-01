import { BrowserRouter, Route, Routes } from "react-router-dom";
import Navbar from "./Navbar";
import Library from "./pages/Library";
import Events from "./pages/Events";
import Members from "./pages/Members";
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/Library" element={<Library />} />
          <Route path="/Events" element={<Events />} />
          <Route path="/Members" element={<Members />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
