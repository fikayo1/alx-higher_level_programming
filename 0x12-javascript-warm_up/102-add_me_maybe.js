#!/usr/bin/node

function addMeMaybe (number, thetFunction) {
  thetFunction(number + 1);
}

module.exports = { addMeMaybe };
