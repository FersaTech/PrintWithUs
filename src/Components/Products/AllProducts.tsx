import React from "react";
import { ProductsArray } from "../../models/Product/ProductModel";
import { Product } from "./Product";

export const AllProducts: React.FC<{ products: ProductsArray[] }> = (props) => {
  return (
      <>
      
      {props.products?.map((product) => {
        return (
          <Product
            name={product.name}
            image1={product.image1}
            finish={product.finish}
            thickness={product.thickness}
            price={product.price}
          />
        );
      })}
    </>
  );
};
