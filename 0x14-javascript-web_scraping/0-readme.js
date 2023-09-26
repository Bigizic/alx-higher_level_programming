#!/usr/bin/node

const readFile = () => {
  const args = process.argv;
  const arg = args[2];

  const fs = require('fs');

  fs.readFile(arg, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
};
readFile();
