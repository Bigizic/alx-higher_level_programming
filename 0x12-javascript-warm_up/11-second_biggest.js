#!/usr/bin/node

function secondMaxNum (max, array) {
  const newArray = [];
  let i = 0;

  for (i = 0; i < array.length; i++) {
    if (parseInt(array[i]) !== max) {
      newArray.push(parseInt(array[i]));
    }
  }
  secondHelper(newArray);
}

function secondHelper (array) {
  let i = 0;
  let secMax = array[0];

  for (i = 0; i < array.length; i++) {
    if (array[i] > secMax) {
      secMax = array[i];
    }
  }
  console.log(secMax);
}

const getMaximum = () => {
  const args = process.argv.slice(2);
  let i = 0;
  let max = 0;
  let x = 0;

  if (args.length <= 1) {
    console.log(i);
    return;
  }

  for (i = 0; i < args.length; i++) {
    max = parseInt(args[i]);
    if (typeof max === 'number') {
      break;
    }
  }

  for (i = 0; i < args.length; i++) {
    x = parseInt(args[i]);
    if (x > max) {
      max = x;
    }
  }
  secondMaxNum(max, args);
  // console.log(max);
};

getMaximum();
