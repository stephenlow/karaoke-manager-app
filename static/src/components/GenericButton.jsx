import React, { Component } from "react";
import Modal from "react-modal";

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
      modalIsOpen: false
    };

    this.openModal = this.openModal.bind(this);
    this.afterOpenModal = this.afterOpenModal.bind(this);
    this.closeModal = this.closeModal.bind(this);
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

  handleClick = () => {
    console.log("this is:", this);
  };

  render() {
    return (
      <div>
        <button onClick={this.openModal}>+ Add Song</button>
        <Modal
          isOpen={this.state.modalIsOpen}
          onAfterOpen={this.afterOpenModal}
          onRequestClose={this.closeModal}
          style={customStyles}
          contentLabel="Example Modal"
        >
          <h2 ref={subtitle => (this.subtitle = subtitle)}>Add a new song:</h2>
          <form>
            <label>
              Name:
              <input type="text" name="name" />
            </label>
            <br />
            <label>
              Artist Name:
              <input type="text" name="artist_name" />
            </label>
            <br />
            <label>
              Description:
              <input type="text" name="description" />
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
