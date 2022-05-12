import React from "react";
import { Card } from "./UI/Card";

export const Product = (props: any) => {
  return (
    <Card>
      <img
        src={props.image1}
        alt="Card 2"
        className="w-full"
      />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">
          <h1>{props.name}</h1>
          <h3>{props.finish}</h3>
          <h2>{props.thickness}</h2>
          <p className="text-purple-600">
            {props.price}
          </p>
        </div>
        <div className="grid grid-flow-col gap-5 px-6">
          <span className="bg-violet-600 text-white text-sm rounded-full px-3 py1 font-base mb-2 text-center">
            Visit
          </span>
          <span className="bg-violet-600 text-white text-sm rounded-full px-3 py1 font-base mb-2 text-center">
            Customize
          </span>
          <span className="bg-violet-600 text-white text-sm rounded-full px-3 py1 font-base mb-2 text-center">
            Buy
          </span>
        </div>
      </div>
    </Card>
  );
};
