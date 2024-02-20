#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    // Print the error if there was an error making the request
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      // Parse the response body as JSON
      const todos = JSON.parse(body);
      
      // Initialize an object to store the count of completed tasks for each user
      const completedTasksByUser = {};
      
      // Loop through each task
      todos.forEach(todo => {
        // If the task is completed
        if (todo.completed) {
          // Increment the count of completed tasks for the user
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });
      
      // Print the count of completed tasks for each user
      console.log(completedTasksByUser);
    } else {
      // Print an error message if the request was not successful
      console.error(`Failed to fetch tasks data. Status code: ${response.statusCode}`);
    }
  }
});
