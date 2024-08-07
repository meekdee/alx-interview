#!/usr/bin/node

const request = require('request');

// Ensure the movie ID is provided
if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

// Fetch movie details
request('https://swapi-api.hbtn.io/api/films/' + movieId, function (err, res, body) {
  if (err) throw err;

  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});

const exactOrder = (actors, x) => {
  if (x === actors.length) return;

  request(actors[x], function (err, res, body) {
    if (err) throw err;

    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};