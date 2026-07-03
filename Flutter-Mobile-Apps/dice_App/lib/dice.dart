
import 'dart:math';

import 'package:flutter/material.dart';
class Dice extends StatefulWidget{
  const Dice({super.key});

  @override
  State<Dice>createState(){
    return _DiceState();
  }
}



class _DiceState extends State<Dice>{

  int leftDice =1;
  int rightDice=1;
  
  
  void rollDice(){
    setState(() {
      leftDice=Random().nextInt(6)+1;
      rightDice=Random().nextInt(6)+1;
    });

  }



  @override
  Widget build(BuildContext context) {
    return  Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text(
            "Roll the dice ",
            style: TextStyle(
              fontSize: 28,
              fontWeight: FontWeight.bold,
              color: Colors.black87,
            ),
          ),
          SizedBox(height: 20),
          Container(
            margin: EdgeInsets.symmetric(horizontal: 30),
            padding: EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white70,
              borderRadius: BorderRadius.circular(25),
              boxShadow: [
                BoxShadow(
                  color: Colors.black,
                  blurRadius: 15,
                  offset: Offset(4, 4),
                ),
              ],
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Image.asset("assets/$leftDice.png", height: 100, width: 100),
                Image.asset("assets/$rightDice.png", height: 100, width: 100),
              ],
            ),
          ),
          SizedBox(height: 30),
          ElevatedButton(
            onPressed: rollDice,
            style: ElevatedButton.styleFrom(
              padding: EdgeInsets.symmetric(horizontal: 40, vertical: 20),
              backgroundColor: Colors.orangeAccent,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(30),
              ),
              shadowColor: Colors.black,
              elevation: 30,
            ),
            child: Text(
              "Roll Dice ",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
          ),
        ],);
  }
}