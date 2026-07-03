import 'package:flutter/material.dart';

void main() {
  runApp(const CalculatorApp());
}

class CalculatorApp extends StatelessWidget {
  const CalculatorApp({super.key});

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return const MaterialApp(
        debugShowCheckedModeBanner: false,
        home: const CalculatorScreen());
  }
}

class CalculatorScreen extends StatefulWidget {
  const CalculatorScreen({super.key});

  @override
  State<CalculatorScreen> createState() => _CalculatorScreen();
}

class _CalculatorScreen extends State<CalculatorScreen> {
  String output = '0';
  String _output = '0';
  double num1 = 0;
  double num2 = 0;
  String operand = '';

  buttonPresses(String buttonText){
    if(buttonText == 'C'){
      _output='0';
      num1=0;
      num2=0;
      operand='';

    }
    else if (buttonText == '+' || buttonText == '-' ||buttonText == '*' || buttonText == '/' ){
      num1=double.parse(output);
      operand = buttonText;
      _output ='0' ;

    }
    else if (buttonText == '='){
      num2=double.parse(output);



      switch(operand){
        case '+':
          _output = (num1+num2).toString();
          break;
        case '-':
          _output = (num1-num2).toString();
          break;
        case '*':
          _output = (num1*num2).toString();
          break;
        case '/':
          _output = (num1/num2).toString();
          break;
      }

      num1=0;
      num2=0;
      operand='';



    }
    else{
      _output+=buttonText;
    }
    
    
    setState(() {
      
      output = double.parse(_output).toStringAsFixed(2).replaceAll(RegExp(r'\.00$'),'');
    });

  }




  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[900],
      appBar: AppBar(
        title: const Text("Calculator App ",style: TextStyle(
          color: Colors.white70
        ),),
        backgroundColor: Colors.grey[850],
      ),
      body: Column(
        children: [
          Container(
            alignment: Alignment.centerRight,
            padding: const EdgeInsets.symmetric(vertical: 24,horizontal: 12),
            child: Text(output,style:
              TextStyle(
                fontSize: 48,
                color: Colors.white
              ),),
          ),
          const Expanded(child: Divider(
            color: Colors.grey,
          )),

          Column(
            children: [
              Row(
                children: [
                  buildButton("7", Colors.grey[800]!),
                  buildButton("8", Colors.grey[800]!),
                  buildButton("9", Colors.grey[800]!),
                  buildButton("/", Colors.orangeAccent),

                ],
              ),
              Row(
                children: [
                  buildButton("4", Colors.grey[800]!),
                  buildButton("5", Colors.grey[800]!),
                  buildButton("6", Colors.grey[800]!),
                  buildButton("*", Colors.orangeAccent),

                ],
              ),
              Row(
                children: [
                  buildButton("1", Colors.grey[800]!),
                  buildButton("2", Colors.grey[800]!),
                  buildButton("3", Colors.grey[800]!),
                  buildButton("-", Colors.orangeAccent),

                ],
              ),
              Row(
                children: [
                  buildButton(".", Colors.grey[800]!),
                  buildButton("0", Colors.grey[800]!),
                  buildButton("C", Colors.grey[800]!),
                  buildButton("+", Colors.orangeAccent),

                ],
              ),
              Row(
                children: [
                  buildButton('=', Colors.green),
                ],
              )
            ],
          )
        ],
      )
    );
  }

  Widget buildButton(String buttonText, Color buttonColor) {
    return Expanded(
      child: Container(
        margin: const EdgeInsets.all(8),
        child: ElevatedButton(
          style: ElevatedButton.styleFrom(
            padding: const EdgeInsets.all(24),
            backgroundColor: buttonColor,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(8),
            ),
          ),
          onPressed: () {
            buttonPresses(buttonText);
          },
          child: Text(
            buttonText,
            style: TextStyle(fontSize: 24, color: Colors.white70),
          ),
        ),
      ),
    );
  }
}
