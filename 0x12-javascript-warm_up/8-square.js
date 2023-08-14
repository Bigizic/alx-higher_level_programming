#!/usr/bin/node

const nTimes = () => {
  const args = process.argv.slice(2);
  const num = parseInt(args[0]);
  let i = 0;
  let word = 'X';

  if (num < 0) {
    return;
  }

  if (!isNaN(num)) {
    for (i = 0; i < num; i++) {
      word = 'X'.repeat(num);
      console.log(word);
    }
  }
  if (isNaN(num)) {
    console.log('Missing size');
  }
};

nTimes();
