#!/usr/bin/node

function recursiveFactorial (a) {
  if (a === 0 || a === 1) {
    return (1);
  } else {
    return (a * recursiveFactorial(a - 1));
  }
}

const readArgs = () => {
  const args = process.argv.slice(2);
  const num = parseInt(args[0]);
  let x;

  if (!num) {
    x = recursiveFactorial(0);
  }

  if (num >= 0) {
    x = recursiveFactorial(num);
  }

  console.log(x);
};

readArgs();
