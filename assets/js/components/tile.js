import React from 'react';

class Tile extends React.Component {

   constructor(props) {
    super(props);
    this.state = {
      value: null,
    };
  }

  render() {
    return (
      <td onClick={() =>{
         window.alert("Invalid Ship");
       }}>
        {this.state.value}
      </td>
    );
  };
}

export default Tile
