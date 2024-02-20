#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint for the specified movie
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if there was an error making the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the response body as JSON
      const movieData = JSON.parse(body);
      
      // Print the characters of the movie in the same order as the list in the response
      movieData.characters.forEach(characterUrl => {
        // Make a GET request to the character URL
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            // Print the error if there was an error making the request
            console.error(error);
          } else {
            if (response.statusCode === 200) {
              // Parse the response body as JSON
              const characterData = JSON.parse(body);
              // Print the name of the character
              console.log(characterData.name);
            } else {
              // Print an error message if the request was not successful
              console.error(`Failed to fetch character data. Status code: ${response.statusCode}`);
            }
          }
        });
      });
    } else {
      // Print an error message if the request was not successful
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    }
  }
});

