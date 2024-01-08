#!/usr/bin/node

// Get the first argument passed
const firstArg = process.argv[2];

// Use console.log(...) to print the output based on the presence of the first argument
if (!firstArg) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
