import React from "react";
import { ImageSilder } from "../Components/Home/HomeCarousal/ImageSlider";
import { SliderData } from "../Components/Home/HomeCarousal/SliderData";
import { Profile } from "../Components/Home/Portfolio/Profile";

export const Home: React.FC = () => {
  

  return (
    <>
      <ImageSilder slides={SliderData} />
      <hr className="  border-r-2  ml-2 mr-2 border-white " />
      <Profile />

      {}
    </>
  );
};
