import "phoenix_html"
import React from 'react';
import ReactDOM from 'react-dom';

import socket from './socket';

import Header from './components/header';
import Board from './board';

function renderHeader() {
  let div = document.getElementById('header');
  ReactDOM.render(<Header />, div);
}

function renderBoard() {
  let main = document.getElementById('main');
  ReactDOM.render(<Board />, main);
}

function start() {
  renderHeader();
  renderBoard();
}

$(start);
