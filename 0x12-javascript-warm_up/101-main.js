#!/usr/bin/node

// Import the callMeMoby function from 101-call_me_moby.js
const callMeMoby = require('./101-call_me_moby').callMeMoby;

// Call callMeMoby with x = 3 and theFunction printing 'C is fun'
callMeMoby(3, function () {
  console.log('C is fun');
});
