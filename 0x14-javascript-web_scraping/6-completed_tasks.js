#!/usr/bin/node

const numberOfCompletedTasks = () => {
  const url = process.argv[2];
  const request = require('request');
  const userIdList = [];
  const completed = {};

  request.get(url, (error, response, body) => {
    if (error) throw error;
    const data = JSON.parse(body);
    data.forEach((item, index) => {
      if (!userIdList.includes(item.userId) && item.completed === true) {
        userIdList.push(item.userId);
        completed[item.userId] = 0;
      }
      if (item.completed) {
        completed[item.userId]++;
      }
    });
    /* console.log(userIdList); */
    console.log(completed);
  });
};
numberOfCompletedTasks();
