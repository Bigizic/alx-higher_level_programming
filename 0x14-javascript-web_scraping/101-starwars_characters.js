#!/usr/bin/node

const printCharacters = () => {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  const request = require('request');
  /* const actors = []; */

  request.get(url, (error, response, body) => {
    if (error) throw error;
    const data = JSON.parse(body);

    async function fetchMyActors () {
      for (const link of data.characters) {
        await new Promise((resolve, reject) => {
          request.get(link, (error, response, body) => {
            if (error) reject(error);
            const actorDetails = JSON.parse(body);
            console.log(actorDetails.name);
            resolve();
          });
        });
      }
    }
    fetchMyActors();
  });
};
printCharacters();
