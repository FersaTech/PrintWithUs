import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Home } from "./Pages/Home";
import Layouts from "./Components/Layouts/Layouts";
import { Orders } from "./Pages/Orders";

function App() {
  return (
    <Router>
      <Layouts />
      <Route path="/" component={Home} exact />
      <Route path="/orders" component={Orders} />
    </Router>
  );
}

export default App;
