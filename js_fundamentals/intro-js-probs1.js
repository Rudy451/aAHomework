function mysteryScoping1() {
  var x = 'out of block';
  if (true) {
    var x = 'in block';
    console.log(x);
  }
  console.log(x);
}

function mysteryScoping2() {
  const x = 'out of block';
  if (true) {
    const x = 'in block';
    console.log(x);
  }
  console.log(x);
}

function mysteryScoping3() {
  const x = 'out of block';
  if (true) {
    const x = 'in block';
    console.log(x);
  }
  console.log(x);
}

function mysteryScoping4() {
  let x = 'out of block';
  if (true) {
    x = 'in block';
    console.log(x);
  }
  console.log(x);
}

function mysteryScoping5() {
  let x = 'out of block';
  if (true) {
    x = 'in block';
    console.log(x);
  }
  x = 'out of block again';
  console.log(x);
}

console.log("Section #1");
console.log("Mystery Scoping #1");
mysteryScoping1();
console.log("Mystery Scoping #2");
mysteryScoping2();
console.log("Mystery Scoping #3");
mysteryScoping3();
console.log("Mystery Scoping #4");
mysteryScoping4();
console.log("Mystery Scoping #5");
mysteryScoping5();

function madLib(verb, adj, noun){
  return `We shall ${verb.toUpperCase()} the ${adj.toUpperCase()} ${noun.toUpperCase()}.`;
}

console.log("Section #2");
console.log("Madlib Function")
console.log(madLib('make', 'best', 'guac'));

function isSubString(searchString, subString){
  if(searchString.length == 1 || subString.length == 1){
    return searchString.length >= subString.length && searchString[0] == subString[0]
  }
  return searchString[0] == subString[0] ? isSubString(searchString.slice(1), subString.slice(1)) : false;
}

console.log("Section #3");
console.log("Problem #1");
console.log(isSubString("time to program", "time"))
console.log("Problem #2");
console.log(isSubString("Jump for joy", "joys"));

function fizzBuzz(array){
  var new_array = [];
  for(let i = 0; i < array.length; ++i){
    if(array[i] % 3 == 0 || array[i] % 5 == 0){
      new_array.push(array[i])
    }
  }
  return new_array;
}

console.log("Section #4");
console.log("Problem #1");
console.log(fizzBuzz([3, 4, 1, 2, 3, 18, 3, 2, 85, 15, 25]));

function isPrime(n){
  let result = !(n > 2 && n % 2 == 0);
  if(result){
    for(let i = n - 2; i > 2; i = i - 2){
      if(n % i == 0){
        result = false;
        break;
      }
    }
  }
  return result;
}

console.log("Problem #2");
console.log(isPrime(2));
console.log("Problem #3");
console.log(isPrime(10));
console.log("Problem #4");
console.log(isPrime(15485863));
console.log("Problem #5");
console.log(isPrime(3548563));

function sumOfNPrimes(n){
  let total = 0;
  if(n > 0){
    for(let i = 2; n > 0; ++i){
      if(isPrime(i)){
        total += i;
        --n;
      }
    }
  }
  return total;
}

console.log("Problem #6");
console.log(sumOfNPrimes(0));
console.log("Problem #8");
console.log(sumOfNPrimes(1));
console.log("Problem #8");
console.log(sumOfNPrimes(4));
