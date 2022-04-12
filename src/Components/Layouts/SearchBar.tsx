import React from "react";
import { Link } from "react-router-dom";

export const SearchBar = () => {
  return (
    <>
      <div className="container w-1/2 ml-52 my-[0.2rem] flex">
        <input
          type="text"
          name="Search Bar"
          id="search"
          className="rounded-l-full p-2 italic flex-1 relative z-0 "
          placeholder="Search ?"
        />
       <Link
        to="/"
        className="inset-0 z-10  left bg-black text-white w-24 rounded-r-full text-center container flex items-center justify-center  "
      >
        <h1 className="mt-[0.2rem] text-bold italic font-serif ">Go</h1>
      </Link>
      

      </div>
    </>
  );
};
