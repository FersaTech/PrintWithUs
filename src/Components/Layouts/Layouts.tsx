import * as React from "react";
import { ReactComponent as SVGIcon } from "../../@types/assets/pwu.svg";
import { FaUsersCog, FaLuggageCart } from "react-icons/fa";
import { Link } from "react-router-dom"

const Layouts: React.FC = () => {
  return (
    <nav className="flex-1">
     
        <div className=" bg-cyan-200 px-2 py-0.5 h-[3.5rem] flex ">
          <SVGIcon className="h-32 w-32 -mt-7 " />
          <FaLuggageCart className="fixed right-[8rem] mt-2 w-10 text-white drop-shadow-lg shadow-black h-10" />
          <FaUsersCog className="fixed right-[4rem] mt-2 w-10 h-10 text-white drop-shadow-md shadow-black" />
          <section className="">
            <div className="w-[350px] h-[35px] rounded-1-full drop-shadow-md shadow-black bg-gray-50 rounded-full text-left p-3 mt-2  ">
              Search Bar
              <Link to="/" className="bg-black rounded-full flex  h [15px] w-16 text-white text-center offset- ">
                Go
              </Link>
            </div>
          </section>
        </div>
        <div className="bg-violet-900 text-white flex space-x-20 rounded-b-lg">
          <div>ALL</div>
          <div>New Arrival</div>
          <div>Recommended</div>
          <div className="fixed right-3">About Us</div>
        </div>
    </nav>
  );
};

export default Layouts;
