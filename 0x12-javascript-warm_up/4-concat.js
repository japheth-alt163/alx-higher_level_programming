#!/usr/bin/node

// Get the first and second arguments passed
const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

// Use console.log(...) to print the output in the specified format
console.log(arg1 + ' is ' + arg2);
