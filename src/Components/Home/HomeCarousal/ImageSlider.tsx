import React from "react";
import { SliderData } from "./SliderData";
import { FaArrowAltCircleRight, FaArrowAltCircleLeft } from "react-icons/fa";
import classes from "./ImageSlider.module.css";

interface CarousalData {
  CarousalImage: string;
}

export const ImageSilder: React.FC<{ slides: {}[] }> = (props) => {
  const [current, setCurrent] = React.useState<number>(0);
  const length = props.slides.length;

  const nextSlide = () => {
    setCurrent(current === length - 1 ? 0 : current + 1);
  };

  const prevSlide = () => {
    setCurrent(current === 0 ? length - 1 : current - 1);
  };

  if (!Array.isArray(props.slides) || props.slides.length <= 0) {
    return null;
  }

  return (
    <section className={`${classes.slider} mb-10`}>
      <FaArrowAltCircleLeft className={classes.leftArrow} onClick={prevSlide} />
      <FaArrowAltCircleRight
        className={classes.rightArrow}
        onClick={nextSlide}
      />
      {SliderData.map((slide: CarousalData, index) => {
        return (
          <div
            className={
              index === current
                ? `${classes.slide} ${classes.active}`
                : classes.slide
            }
            key={index}
          >
            {index === current && (
              <img
                src={slide.CarousalImage}
                alt="Carousal"
                className={classes.image}
              />
            )}
          </div>
        );
      })}
    </section>
  );
};
