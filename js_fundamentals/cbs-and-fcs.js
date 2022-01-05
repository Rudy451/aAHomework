/*const readline = require('readline');
const reader = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

//console.log("Processing Function....");
//setTimeout(function(){console.log("HAMMERTIME");}, 5000);

function teaAndBiscuits(){
  let firstAns = "";
  let secondAns = "";

  reader.question("Would you like some tea???\n> ", function(res){
    firstAns = res.indexOf("y") > -1 ? "do" : "dont";
    reader.question("Would you like biscuits???\n> ", function(res){
      secondAns = res.indexOf("y") > -1 ? "do" : "dont";
      console.log(`So you ${firstAns} want tea and you ${secondAns} want coffee`);
      reader.close();
    });
  });
}

//teaAndBiscuits();
*/
function Cat () {
this.name = 'Markov';
this.age = 3;
}

function Dog () {
  this.name = 'Noodles';
  this.age = 4;
}

Dog.prototype.chase = function (cat) {
  console.log(`My name is ${this.name} and I'm chasing ${cat.name}! Woof!`)
};

const Markov = new Cat ();
const Noodles = new Dog ();

Noodles.chase(Markov);
Noodles.chase.call(Markov, Noodles);
Noodles.chase.apply(Markov, [Noodles]);
