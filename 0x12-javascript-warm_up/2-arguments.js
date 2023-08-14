#!/usr/bin/node

const printsArguments = () => {
  const args = process.argv.slice(1);
  const noArg = 'No argument';
  const oneArg = 'Argument found';
  const mulArg = 'Arguments found';
  if (args.length < 2) {
    console.log(noArg);
  } else if (args.length === 2) {
    console.log(oneArg);
  } else {
    console.log(mulArg);
  }
};
printsArguments();
