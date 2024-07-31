#!/usr/bin/node
// return list of names of characters from movie in order

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const charDict = {};

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const charList = JSON.parse(body).characters;
    let count = 0;
    for (let i = 0; i < charList.length; i++) {
      request.get(charList[i], function (err, response, body) {
        if (err) {
          console.log(err);
        }
        const person = JSON.parse(body);
        charDict[person.url] = person.name;
        count++;
        if (count === charList.length) {
          for (const charURL of charList) {
            console.log(charDict[charURL]);
          }
        }
      });
    }
  }
});
