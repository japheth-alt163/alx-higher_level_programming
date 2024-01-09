#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const userId in dict) {
  const occurrences = dict[userId].toString();

  if (newDict[occurrences] === undefined) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
}

console.log(newDict);
