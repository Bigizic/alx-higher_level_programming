#!/usr/bin/node

const myDict = require('./101-data').dict;

function sortedDict () {
  const newDict = {};

  for (const userId in myDict) {
    const occurrences = myDict[userId];

    if (!newDict[occurrences]) {
      newDict[occurrences] = [];
    }
    newDict[occurrences].push(userId);
  }
  console.log(newDict);
}

sortedDict();
