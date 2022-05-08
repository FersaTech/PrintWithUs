import React from "react";
import Carousal from "../Components/Home/Carousal";
import Nav from "../Components/Home/Nav";
import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <>
      <Nav />
      <Carousal />
      <Link to="/products">All Products</Link>
      <br />
      <Link to="/random">404 Page</Link>
    </>
  );
};

export default HomePage;
