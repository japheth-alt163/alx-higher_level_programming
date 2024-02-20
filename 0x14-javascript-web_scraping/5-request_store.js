#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    // Print the error if there was an error making the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Write the body response to the specified file
      fs.writeFile(filePath, body, 'utf-8', (err) => {
        if (err) {
          // Print the error if there was an error writing the file
          console.error(err);
        }
      });
    } else {
      // Print an error message if the request was not successful
      console.error(`Failed to fetch webpage. Status code: ${response.statusCode}`);
    }
  }
});
