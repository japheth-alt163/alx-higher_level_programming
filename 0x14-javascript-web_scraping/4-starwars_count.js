#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18'; // Wedge Antilles' character ID

// Make a GET request to the Star Wars API endpoint
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if there was an error making the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the response body as JSON
      const filmsData = JSON.parse(body).results;
      // Filter films where "Wedge Antilles" appears
      const filmsWithWedge = filmsData.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
      // Print the number of films where "Wedge Antilles" appears
      console.log(filmsWithWedge.length);
    } else {
      // Print an error message if the request was not successful
      console.error(`Failed to fetch movie data. Status code: ${response.statusCode}`);
    }
  }
});
