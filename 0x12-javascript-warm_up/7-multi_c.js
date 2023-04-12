#!/usr/bin/node

const arg = process.argv[2];
if (isNaN(parseInt(arg)))
{
	console.log("Missing number of occurrences");
}
else {
	const x = parseInt(arg);
	let i = 0;
	while (i < x)
	{ console.log("C is fun");
	i++; }
}
