#!/usr/bin/node

// Define the factorial function
function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

// Get the first argument passed
const arg = parseInt(process.argv[2]);

// Call the factorial function and print the result
console.log(factorial(arg));
