import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Home } from "./Pages/Home";
import Layouts from "./Components/Layouts/Layouts";
import { Orders } from "./Pages/Orders";
import { Footer } from "./Components/Layouts/Footer";

function App() {
  return (
    <Router>
      <Layouts className="bg-gradient-to-r from-gray-300  to-blue-300">
        <Route path="/" component={Home} exact />
        <Route path="/orders" component={Orders} />
      </Layouts>
      <Footer />
    </Router>
  );
}

export default App;
