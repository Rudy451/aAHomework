function printCallback(word){
  console.log(`Mx. ${word} Jingleheimer Schmidt`);
}

function titleize(names_array, my_callback){
  names_array = names_array.map(name => `${name.slice(0, 1).toUpperCase()}${name.slice(1)}`);
  names_array.forEach(my_callback);
}

console.log("Section #1");
console.log("Problem #1");
titleize(["Mary", "Brian", "Leo"], printCallback);

function Elephant(name, height, tricks) {
  this.name = name;
  this.height = height;
  this.tricks = tricks;
}

Elephant.prototype.trumpet = function(){console.log(`${name} the elephant goes 'phrRRRRRRRRRRR!!!!!!!'`);}
Elephant.prototype.grow = function(){this.height += 12;}
Elephant.prototype.addTrick = function(trick){this.tricks.push(trick);}
Elephant.prototype.play = function(){console.log(this.tricks[Math.floor(Math.random() * this.tricks.length)]);}

console.log("Section #2 - Problem #1");
Dumbo = new Elephant("Dumbo", 60, ["Flies", "Dances", "Cowers"]);
console.log(Dumbo.name, Dumbo.height, Dumbo.tricks);

let ellie = new Elephant("Ellie", 185, ["giving human friends a ride", "playing hide and seek"]);
let charlie = new Elephant("Charlie", 200, ["painting pictures", "spraying water for a slip and slide"]);
let kate = new Elephant("Kate", 234, ["writing letters", "stealing peanuts"]);
let micah = new Elephant("Micah", 143, ["trotting", "playing tic tac toe", "doing elephant ballet"]);

let herd = [ellie, charlie, kate, micah];

Elephant.paradeHelper = function(elephant){
  console.log(`${elephant.name} is trotting by!`);
}

console.log("Section #3 - Problme #1");
herd.forEach(elephant => Elephant.paradeHelper(elephant));


function dinerBreakfast(item){
  let myOrder = "I'd like cheesy scrambled eggs";
  return function order(item){
    let args = Array.from(arguments);
    myOrder = myOrder.concat(`${args.length == 0 ? '' : ` and ${item}`}`);
    console.log(`${myOrder} please${item === undefined ? '' : '.'}`);
    return 0;
  };
}

console.log("Section #4 - Problem #1");
let bfastOrder = dinerBreakfast();
bfastOrder("chocolate chip pancakes");
bfastOrder("grits");
