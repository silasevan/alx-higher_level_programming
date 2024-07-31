#!/usr/bin/node
// Write a script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const long = data.length;

    const countDict = {};

    for (let i = 0; i < long; i++) {
      if (data[i].completed) {
        if (!(data[i].userId in countDict)) {
          countDict[data[i].userId] = 0;
        }
        countDict[data[i].userId] += 1;
      }
    }
    console.log(countDict);
  }
});
