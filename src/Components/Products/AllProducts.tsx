import React from "react";
import { ProductsArray } from "../../models/Product/ProductModel";
import { Product } from "./Product";

export const AllProducts = (props: any) => {
  return (
      <>
      
      {props.products?.map((product: any) => {
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
