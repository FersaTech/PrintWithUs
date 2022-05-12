import React, { SetStateAction } from "react";
import { Link } from "react-router-dom";
import { AllProducts } from "../Components/Products/AllProducts";
import { ProductsArray } from "../models/Product/ProductModel";

const AllProductsPage = () => {
  const [loading, setLoading] = React.useState<boolean>(false);
  const [loadedProductsArray, setLoadedProductsArray] = React.useState<ProductsArray>();

  // Temporary List for Storing Fetched Products
  let fetchedProducts: any = []

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

      fetchedProducts.push(Product)
    }
    setLoading(false);
    setLoadedProductsArray(fetchedProducts)
  };

  // Fetches All Products on every Component Render, initially the first time on Render
  React.useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <>
      {loading ? 'Loading...' :  <AllProducts products={loadedProductsArray} />}
      <div>AllProducts Page</div>
      <Link to="/">Go to Home</Link>
    </>
  );
};

export default AllProductsPage;
