#!/usr/bin/node

// Get the list of arguments
const args = process.argv.slice(2);

// Convert each argument to an integer
const numbers = args.map(arg => parseInt(arg));

// Sort the array of numbers in descending order
numbers.sort((a, b) => b - a);

// Get the second element in the sorted array (second biggest integer)
const secondBiggest = numbers[1] || 0;

// Print the result
console.log(secondBiggest);
