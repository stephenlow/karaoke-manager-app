import React, { Component } from "react";
import NavBanner from "../src/components/NavBanner";
import Table from "../src/components/Table";

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <NavBanner />
        <main className="container">
          <Table />
        </main>
      </React.Fragment>
    );
  }
}

export default App;
