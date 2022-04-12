import * as React from "react";
import { Navbar } from "./Navbar";

interface Layout {
  className: string
}

const Layouts: React.FC<Layout> = (props) => {
  return (
    <div className={`${props.className}`}>
      <Navbar />
        {props.children}
    </div>
  );
};

export default Layouts;
