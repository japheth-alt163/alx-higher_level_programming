#!/usr/bin/node

// Get the first argument passed
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Check if the conversion was successful and print the output accordingly
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  // Use a loop to print "C is fun" x times
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
