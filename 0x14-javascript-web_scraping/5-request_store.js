#!/usr/bin/node

const urlWriteFile = () => {
  const url = process.argv[2];
  const fileName = process.argv[3];
  const request = require('request');
  const fs = require('fs');

  request.get(url, (error, response, body) => {
    if (error) throw error;
    fs.writeFile(fileName, body, (err) => {
      if (err) throw err;
    });
  });
};
urlWriteFile();
