import React from "react";
import { Link } from "react-router-dom";
import { AllProducts } from "../Components/Products/AllProducts";
import { ProductsArray } from "../models/Product/ProductModel";

const AllProductsPage = () => {
  const [loading, setLoading] = React.useState<boolean>(false);
  const [productsArray, setProductsArray] = React.useState<ProductsArray>();


  //Fucntion to fetch all Products --> Asynchronus Function
  const fetchProducts = async () => {
    setLoading(true);
    const response = await fetch(
      "https://django-pwu-api.herokuapp.com/products/",
      {
        method: "GET",
        headers: { Accept: "application/json" },
      }
    );
    const data = await response.json();
    for (const res in data) {
      const Product = {
        name: data[res].name,
        image1: data[res].image1,
        finish: data[res].finish,
        thickness: data[res].thicknes,
        price: data[res].price,
      };

      setProductsArray(Product);
    }
    setLoading(false);
  };

  // Fetches All Products on every Component Render, initially the first time on Render
  React.useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <>
      {loading ? 'Loading...' :  <AllProducts products={productsArray} />}
      <div>AllProducts Page</div>
      <Link to="/">Go to Home</Link>
    </>
  );
};

export default AllProductsPage;
