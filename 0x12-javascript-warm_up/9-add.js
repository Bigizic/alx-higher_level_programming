#!/usr/bin/node

function add (a, b) {
  const args = process.argv;
  const num = parseInt(args[2]);
  let res = 0;

  if (args.length > 3 && !isNaN(num)) {
    if (typeof parseInt(args[3]) === 'number') {
      res = num + parseInt(args[3]);
      console.log(res);
    }
  } else {
    console.log('NaN');
  }
}

add(0, 0);
