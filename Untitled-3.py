""" A Professor Pio homework assignment for Lesson 4 of Wed 6-26 nd completed Friday 6-28-2024 evening.
Assignement:    1) Take in 4 number entries
                    2) Print the following
                    3) Arithmetic mean of the inputs
                    4) Geometric mean 
                    5) Bonus: Root Mean Square (RMS)  """
print("This program computes averages - arithmetic, geometric, and RMS.")    
score1 = input("Enter four numbers separated by a comma: ")
score2 = input("Enter four numbers separated by a comma: ")
score3 = input("Enter four numbers separated by a comma: ")
score4 = input("Enter four numbers separated by a comma: ")
average = ( int(score1) + int(score2) + int(score3) + int(score4) ) / 4
print(average)

""" Geometric Mean"""
GeometricMean = ( int(score1) * int(score2) * int(score3) * int(score4) ) ** (0.25)
print(GeometricMean)

"""Root Mean Square (RMS)"""
rms = ( (( int(score1) **2 )  + ( int(score2) **2 ) + ( int(score3) **2 ) + ( int(score4) **2 ) ) / 4 ) ** (1 /2) 
""" above line is summ of squares and then divide by 4 """
print(rms)