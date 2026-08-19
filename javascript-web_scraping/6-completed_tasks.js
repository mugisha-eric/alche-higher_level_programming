#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (!completed[todo.userId]) {
          completed[todo.userId] = 0;
        }
        completed[todo.userId]++;
      }
    });

    console.log(completed);
  }
});
