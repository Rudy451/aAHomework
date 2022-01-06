import React from "react";

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    // your code here
    this.state = {
      num1: "",
      num2: "",
      result: 0,
    };
    this.setNum1 = this.setNum1.bind(this);
    this.setNum2 = this.setNum2.bind(this);
    this.addition = this.addition.bind(this);
    this.subtraction = this.subtraction.bind(this);
    this.multiplication = this.multiplication.bind(this);
    this.division = this.division.bind(this);
  }

  // your code here
  setNum1(e){
    e.preventDefault();
    const num = e.target.value;
    if((/^\d.*?/).test(num)){
      this.setState({num1 : num});
    }
    if(num == "" && this.state.num1.length == 1){
      this.setState({num1: ""});
    }
  }

  setNum2(e){
    e.preventDefault();
    const num = e.target.value;
    if((/^\d.*?/).test(num)){
      this.setState({num2 : num});
    }
    if(num == "" && this.state.num2.length == 1){
      this.setState({num2: ""});
    }
  }

  clearValues(e){
    e.preventDefault();
    this.setState({num1: ''});
    this.setState({num2: ''});
  }

  addition(e){
    e.preventDefault();
    if(this.state.num1 != "" && this.state.num2 != ""){
      this.setState({result: Number.parseInt(this.state.num1) + Number.parseInt(this.state.num2)});
      this.clearValues();
    }
  }

  subtraction(){
    if(this.state.num1 != "" && this.state.num2 != ""){
      this.setState({result: Number.parseInt(this.state.num1) - Number.parseInt(this.state.num2)});
      this.clearValues();
    }
  }

  multiplication(e){
    e.preventDefault();
    if(this.state.num1 != "" && this.state.num2 != ""){
      this.setState({result: Number.parseInt(this.state.num1) * Number.parseInt(this.state.num2)});
      this.clearValues();
    }
  }

  division(e){
    e.preventDefault();
    if(this.state.num1 != "" && this.state.num2 != ""){
      this.setState({result: Number.parseInt(this.state.num1) / Number.parseInt(this.state.num2)});
      this.clearValues();
    }
  }

  render() {
    return (
      <div>
        <h1>{this.state.result}</h1>
        <input value={this.state.num1} onChange={e => this.setNum1(e)}/>
        <input value={this.state.num2} onChange={e => this.setNum2(e)}/>
        <button onClick={this.clearValues}>Clear</button><br/>
        <button onClick={this.addition}>+</button>
        <button onClick={this.subtraction}>-</button>
        <button onClick={this.multiplication}>*</button>
        <button onClick={this.division}>/</button>
      </div>
    );
  }
}

export default Calculator;
