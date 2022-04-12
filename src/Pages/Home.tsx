import React from "react";
import { ImageSilder } from "../Components/Home/HomeCarousal/ImageSlider";
import { SliderData } from "../Components/Home/HomeCarousal/SliderData";
import { Profile } from "../Components/Home/Portfolio/Profile";

export const Home: React.FC = () => {
  return (
    <>
      <ImageSilder slides={SliderData} />
      <Profile />

      {}
    </>
  );
};
