#!/usr/bin/node

/**
 * add - exporting a named function, use {module.exports = function()} for unnamed
 * function
 */
exports.add = function add (a, b) {
  return (a + b);
};
