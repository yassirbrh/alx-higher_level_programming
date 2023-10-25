#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const completed = {};
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed === true) {
        if (completed[tasks[i].userId] === undefined) {
          completed[tasks[i].userId] = 1;
        } else {
          completed[tasks[i].userId]++;
        }
      }
    }
    console.log(completed);
  }
});
