import { Routes, Route } from "react-router-dom";
import AllProductsPage from "./Pages/AllProductsPage";
import HomePage from "./Pages/HomePage";
import _404NotFound from "./Pages/_404NotFound";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/products" element={<AllProductsPage />} />
        <Route path="*" element={<_404NotFound />} />
      </Routes>
    </div>
  );
}

export default App;
