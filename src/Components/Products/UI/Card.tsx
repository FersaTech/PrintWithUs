import React from "react";

export const Card = (props: any) => {
  return (
    <div className="card gap-8 md:flex md:flex-wrap 2xl:grid 2xl:grid-cols-3 md:justify-items-center mt-28">
      <div className="py-10 mx-auto ">
        <div className="rounded-lg overflow-hidden shadow-lg max-w-sm">
          {props.children}
        </div>
      </div>
    </div>
  );
};
