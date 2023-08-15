#!/usr/bin/node

/*
 * concatFiles - function that reads from multiple files and copy the contents
 * read to fileC
 */
function concatFiles (fileA, fileB, fileC) {
  const fs = require('fs');
  const fileNames = [fileA, fileB];

  fileNames.forEach(fileName => {
    fs.readFile(fileName, 'utf8', (err, data) => {
      if (err) {
        console.error('Error reading files', err);
        return (0);
      }

      fs.appendFile(fileC, data, 'utf8', err => {
        if (err) {
          console.error('Error writing to destination file', err);
          return (0);
        }
      });
    });
  });
}
const args = process.argv.slice(2);
const fileA = args[0];
const fileB = args[1];
const fileC = args[2];
concatFiles(fileA, fileB, fileC);
