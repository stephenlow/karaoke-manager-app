import React, { Component } from "react";
import Banner from "react-banner";

import "react-banner/dist/style.css";

class NavBanner extends Component {
  render() {
    return <Banner logo="Karaoke Manager" url={window.location.pathname} />;
  }
}

export default NavBanner;
