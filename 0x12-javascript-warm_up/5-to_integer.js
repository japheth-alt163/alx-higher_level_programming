#!/usr/bin/node

// Get the first argument passed
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Check if the conversion was successful and print the output accordingly
if (!isNaN(num)) {
  console.log('My number:', num);
} else {
  console.log('Not a number');
}
