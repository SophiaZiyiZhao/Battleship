import React from 'react';

import Grid from './components/grid';

class Board extends React.Component {
   render() {
    return (
      <div className="row">
        <div className="col-md-1" />
         <div className="col-md-4">
         <h3> <p> My Board</p> </h3>
          <Grid />
        </div>
        <div className="col-md-2" />
        <div className="col-md-4">
          <h3> <p> Opponent Board</p> </h3>
          <Grid />
        </div>
        <div className="col-md-1" />

      </div>
    );
  }
}

export default Board
