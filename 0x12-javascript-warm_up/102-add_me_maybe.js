#!/usr/bin/node

// Define the addMeMaybe function
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
