import React from "react";
import { Link } from "react-router-dom";
import styles from "../styles/_404NotFoundStyle.module.css";

const _404NotFound = () => {
  return (
    <React.Fragment>
      <div className="flex items-center justify-center w-screen h-screen ">
        <div className="px-4 lg:py-12">
          <div className="lg:flex relative">
            <div className="flex flex-col items-center justify-center md:py-24 lg:py-28 mx-auto ">
              <h1 className={`font-bold  text-purple-600 z-10 -my-32 ${styles['text-9xl']}`}>
                404
              </h1>
            </div>
            <div className="absolute z-30 my-20  ">
              <img
                src="src\assets\_404.png"
                alt="image"
                className="object-cover w-full h-full opacity-90 "
              />

              <p className={`mb-2 font-bold text-center text-gray-800 md:text-3xl ${styles['text-2xl']} `}>
                <span className="text-red-500 ">Oops!</span> Page not found
              </p>
              <p className="mb-8 text-center text-gray-500 md:text-lg">
                The page you’re looking for has no result.
              </p>
              <Link
                to="/"
                className="px-10 text-center py-2 text-md ml-32 font-semibold text-purple-800 rounded-full bg-purple-200 "
              >
                Back
              </Link>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default _404NotFound;


