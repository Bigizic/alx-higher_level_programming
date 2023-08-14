#!/usr/bin/node

/* secondMaxNum - a function that creates a new array from the default array, it
 * works by iterating through the array and appending any element that's a digit
 * to the newArray as long as the element is not equal to the maximum element in
 * the default array
 *
 * @max: (int) an integer that serves as the maximum integer from the default array
 *
 * @array: default array to perfrom certain operations on
 *
 * Return: void
 */
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

/**
 * secondHelper - this function prints the second max element in the array by going
 * through the already altered array and checking for the maximum integer in the
 * array
 *
 * @array: array to perfrom operation on
 *
 * Return: void
 */
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

/**
 * getMaximum - this function reads from stdin and gets the maximum number from
 * input
 *
 * Return: void
 */
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
