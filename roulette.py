#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 22:32:09 2023

@author: giannidiarbi

 Gianni Diarbi
 DS2000
 Spring 2023
 HW 3 Problem 3
 roulette.py
"""

import random

import matplotlib.pyplot as plt

KAYLA_PAYOUT = 5
LANEY_PAYOUT = 50
STOPPING_THRESHOLD = 50000

def main():
    
    # Initialize variables
    money_kayla = 0
    money_laney = 0
    wins_kayla = 0
    wins_laney = 0

  
    # Spin the wheel
    # Determine who won the round, how much money each player
    # has earned, and the number of games each player has won 
    while money_kayla < STOPPING_THRESHOLD and money_laney \
        < STOPPING_THRESHOLD:
            
        spin = random.randint(0, 36)
       # print(spin)
        if spin % 2 == 1:
          money_kayla += KAYLA_PAYOUT
          wins_kayla += 1
        #  print("Kayla won!")
          
        if spin == 31 or 32:
          money_laney += LANEY_PAYOUT
          wins_laney += 1
         # print("Laney won!")  
          
    # Sanity Check - report totals
         # print ("Kayla has $", int(money_kayla), "and won", \
               #  int(wins_kayla), "games.")
        #  print ("Laney has $", int(money_laney), "and won", \
              #   int(wins_laney), "games.")
    
    # Make a bar chart comparing the number of wins each player has
    plt.bar(1, wins_kayla, color = "magenta")
    plt.bar(2, wins_laney, color = "navy")
    
    
    # Add a title, label the axes, and add x-ticks
    plt.title("Player vs Number of Wins")
    plt.xticks([1, 2], ["Kayla", "Laney"])
    plt.xlabel("Player Name")
    plt.ylabel("Number of Wins")
   
    # Make a bar chart comparing the amount of money each player wins
    plt.show()
    plt.bar(1, money_kayla, color = "magenta")
    plt.bar(2, money_laney, color = "navy")
    
    
    # Add a title, label the axes, and add x-ticks
    plt.title("Player vs Amount of Money Won ($)")
    plt.xticks([1, 2], ["Kayla", "Laney"])
    plt.xlabel("Player Name")
    plt.ylabel("Amount of Money Won ($)")
    
    
main()