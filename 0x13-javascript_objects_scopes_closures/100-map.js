#!/usr/bin/node

const myList = require('./100-data').list;

function factorIndex () {
  const map1 = myList.map((value, index) => value * index);
  console.log(myList);
  console.log(map1);
}
factorIndex();
