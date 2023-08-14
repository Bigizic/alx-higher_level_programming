#!/usr/bin/node

const anInteger = () => {
  const args = process.argv.slice(2);
  const num = parseInt(args[0]);

  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + num);
  }
};
anInteger();
