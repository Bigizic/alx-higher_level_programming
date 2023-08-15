#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  const newArray = [];

  for (i = list.length - 1; i >= 0; i--) {
    newArray.push(list[i]);
  }
  return (newArray);
};
