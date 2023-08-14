#!/usr/bin/node

const nTimes = () => {
  const args = process.argv.slice(2);
  const num = parseInt(args[0]);
  let neg = false;
  let i = 0;
  if (num === 0) { return; }

  if (!isNaN(num)) {
    for (i = 0; i < num; i++) {
      console.log('C is fun');
    }
  } else {
    neg = true;
  }

  if (isNaN(num) || neg === true) {
    console.log('Missing number of occurrences');
  }
};

nTimes();
