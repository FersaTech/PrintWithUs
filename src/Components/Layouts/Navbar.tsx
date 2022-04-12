import { ReactComponent as SVGIcon } from "../../@types/assets/pwu.svg";
import { FaUsersCog } from "react-icons/fa";
import { RiShoppingCart2Fill} from "react-icons/ri";
import { SearchBar } from "./SearchBar";

export const Navbar = () => {
  return (
    <nav className="flex-1">
     
        <div className=" bg-cyan-200 px-2 py-0.5 h-[3.8rem] flex ">
          <section className="">
            <SVGIcon className=" h-40 w-40 -mt-10" />
          </section>
          <RiShoppingCart2Fill className="fixed right-[8rem] mt-2 w-10 text-white drop-shadow-lg shadow-black h-10" />
          <FaUsersCog className="fixed right-[4rem] mt-2 w-10 h-10 text-white drop-shadow-md shadow-black" />
          <SearchBar />
        </div>
        <div className="bg-violet-900 text-white flex space-x-20 rounded-b-lg">
          <div>ALL</div>
          <div>New Arrival</div>
          <div>Recommended</div>
          <div className="fixed right-3">About Us</div>
        </div>
    </nav>
  )
}
