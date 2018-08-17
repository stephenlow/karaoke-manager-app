import React from "react";
import ReactDOM from "react-dom";
import App from "./App";
import NavBanner from "../src/components/NavBanner";
import Table from "../src/components/Table";
import registerServiceWorker from "./registerServiceWorker";

ReactDOM.render(<App />, document.getElementById("root"));
registerServiceWorker();
