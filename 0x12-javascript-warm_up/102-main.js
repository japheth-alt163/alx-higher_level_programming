#!/usr/bin/node

// Import the addMeMaybe function from 102-add_me_maybe.js
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;

// Call addMeMaybe with number = 4 and theFunction printing the incremented value
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
