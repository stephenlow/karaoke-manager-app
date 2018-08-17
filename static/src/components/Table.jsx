import React, { Component } from "react";
import { BootstrapTable, TableHeaderColumn } from "react-bootstrap-table";
import "../../node_modules/react-bootstrap-table/css/react-bootstrap-table.css";
import Request from "superagent";

class Table extends Component {
  constructor() {
    super();
    this.state = {};
  }

  componentDidMount() {
    const API_GET_SONGS = "http://localhost:5000/song/";
    Request.get(API_GET_SONGS).then(response => {
      this.setState({
        songs: response.body.data,
        total: response.body.data.length
      });
    });
  }

  showSongName(cell) {
    return cell.name;
  }

  showArtistName(cell) {
    return cell.artist_name;
  }

  showDescription(cell) {
    return (
      "<a href=" +
      cell.description +
      "' target='_blank'>" +
      cell.description +
      "</a>"
    );
  }

  render() {
    return (
      <React.Fragment>
        <div>
          <BootstrapTable data={this.state.songs}>
            <TableHeaderColumn isKey dataField="id">
              ID
            </TableHeaderColumn>
            <TableHeaderColumn
              dataField="attributes"
              dataFormat={this.showSongName}
            >
              Name
            </TableHeaderColumn>
            <TableHeaderColumn
              dataField="attributes"
              dataFormat={this.showArtistName}
            >
              Value
            </TableHeaderColumn>
            <TableHeaderColumn
              dataField="attributes"
              dataFormat={this.showDescription}
            >
              Description
            </TableHeaderColumn>
          </BootstrapTable>
        </div>
      </React.Fragment>
    );
  }
}

export default Table;
