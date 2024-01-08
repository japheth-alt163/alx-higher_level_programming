#!/usr/bin/node

// Get the first argument passed
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the conversion was successful and print the output accordingly
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Use nested loops to print the square
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
