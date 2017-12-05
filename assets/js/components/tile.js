import React from 'react';

class Tile extends React.Component {
  render() {
    return (
      <td onClick={this.props.onClick}></td>
    );
  };

  handleClick() {
    window.alert("Invalid ship!");
  }
}

export default Tile
