import React, { Component } from "react";
import NavBanner from "../src/components/NavBanner";
import Table from "../src/components/Table";
import GenericButton from "../src/components/GenericButton";

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <NavBanner />
        <main className="container">
          <Table />
          <GenericButton />
        </main>
      </React.Fragment>
    );
  }
}

export default App;
