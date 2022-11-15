#!/usr/bin/node

const request = require('request');
const url = require('process').argv[2];

request.get(url, (err, resp, body) => {
  if (err) {
    throw err;
  }
  const movies = JSON.parse(body).results;
  let movieNum = 0;
  for (const movie of movies) {
    for (const character of movie.characters) {
      if (character.endsWith('18/')) {
        movieNum += 1;
        break;
      }
    }
  }
  console.log(movieNum);
});
