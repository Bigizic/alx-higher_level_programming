#!/usr/bin/node

const writeFile = () => {
  const fileName = process.argv[2];
  const word = process.argv[3];

  const fs = require('fs');

  fs.writeFile(fileName, word, (err) => {
    if (err) throw err;
  });
};
writeFile();
