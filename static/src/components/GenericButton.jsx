import React, { Component } from "react";
import Modal from "react-modal";
import Request from "superagent";

const customStyles = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)"
  }
};

class GenericButton extends Component {
  state = {};

  constructor() {
    super();
    this.state = {
      modalIsOpen: false,
      name: "",
      artist_name: "",
      description: ""
    };

    this.openModal = this.openModal.bind(this);
    this.afterOpenModal = this.afterOpenModal.bind(this);
    this.closeModal = this.closeModal.bind(this);
    this.handleAddClick = this.handleAddClick.bind(this);
  }

  openModal() {
    this.setState({ modalIsOpen: true });
  }

  afterOpenModal() {
    // references are now sync'd and can be accessed.
    this.subtitle.style.color = "#f00";
  }

  closeModal() {
    this.setState({ modalIsOpen: false });
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleAddClick(event) {
    event.preventDefault();
    const { name, artist_name, description } = this.state;
    const API_POST_SONGS = "http://localhost:5000/song/add";
    let request =
      '{ "data":{ "type": "song", "attributes": { "name":' +
      JSON.stringify(name) +
      ', "artist_name": ' +
      JSON.stringify(artist_name) +
      ', "description": ' +
      JSON.stringify(description) +
      "}}}";

    console.log(request);
    Request.post(API_POST_SONGS)
      .set("Content-Type", "application/json")
      .send(request)
      .then(response => console.log(response))
      .catch(err => console.log(err));

    this.closeModal();
    window.location.reload();
  }

  render() {
    const { modalIsOpen, name, artist_name, description } = this.state;
    return (
      <div>
        <button onClick={this.openModal}>+ Add Song</button>
        <Modal
          isOpen={modalIsOpen}
          onAfterOpen={this.afterOpenModal}
          onRequestClose={this.closeModal}
          style={customStyles}
          contentLabel="Add Song Modal"
        >
          <h2 ref={subtitle => (this.subtitle = subtitle)}>Add a new song:</h2>
          <form onSubmit={this.handleAddClick}>
            <label>
              Name:
              <input
                type="text"
                name="name"
                value={name}
                onChange={this.onChange}
              />
            </label>
            <br />
            <label>
              Artist Name:
              <input
                type="text"
                name="artist_name"
                value={artist_name}
                onChange={this.onChange}
              />
            </label>
            <br />
            <label>
              Description:
              <input
                type="text"
                name="description"
                value={description}
                onChange={this.onChange}
              />
            </label>
            <br />
            <button onClick={this.closeModal}>Close</button>
            <button>Add</button>
          </form>
        </Modal>
      </div>
    );
  }
}

export default GenericButton;
