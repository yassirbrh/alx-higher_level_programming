#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    let i = 0;
    const character = 'https://swapi-api.alx-tools.com/api/people/18/';
    for (i = 0; i < results.length; i++) {
      const index = results[i].characters.indexOf(character);
      if (index !== -1) {
        count++;
      }
    }
    console.log(count);
  }
});
