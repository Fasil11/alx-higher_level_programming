#!/usr/bin/node
const dict = require('./101-data').dict;
const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];

const newDict = valsUniq.reduce((acc, val) => {
  const list = totalist.filter(([key, value]) => value === val).map(([key, value]) => key);
  acc[val] = list.reverse();
  return acc;
}, {});

console.log(newDict);
