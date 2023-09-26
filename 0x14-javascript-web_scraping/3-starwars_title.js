#!/usr/bin/node

const movieId = () => {
  const arg = process.argv[2];
  const request = require('request');

  const url = `https://swapi-api.alx-tools.com/api/films/${arg}`;
  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const data = JSON.parse(body);
    console.log(data.title);
  });
};
movieId();
