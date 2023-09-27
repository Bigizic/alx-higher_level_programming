#!/usr/bin/node

const characterCount = () => {
  const url = process.argv[2];
  const request = require('request');
  let count = 0;
  const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
  const temp = 'http://swapi.co/api/people/18/';

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const data = JSON.parse(body);
    for (const item of data.results) {
      if (Array.isArray(item.characters)) {
        if (item.characters.includes(temp) || item.characters.includes(charId)) {
          count += 1;
        }
      }
    }
    console.log(count);
  });
};
characterCount();
