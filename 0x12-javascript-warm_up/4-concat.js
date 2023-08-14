#!/usr/bin/node

const twoArguments = () => {
  const args = process.argv.slice(2);
  if (args) {
    console.log(args[0] + ' is ' + args[1]);
  }
};

twoArguments();
