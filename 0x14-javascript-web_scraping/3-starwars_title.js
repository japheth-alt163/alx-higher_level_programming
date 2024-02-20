#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if there was an error making the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the response body as JSON
      const movieData = JSON.parse(body);
      // Print the title of the movie
      console.log(movieData.title);
    } else {
      // Print an error message if the request was not successful
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    }
  }
});
