#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // Print the error object if an error occurred
    console.error(err);
  }
});
