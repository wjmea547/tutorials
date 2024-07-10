var1 = 0
var2 = 1
#only one of the conditionals below will execute the code in their body. They are mutually exclusive.
if var1 < var2:#header this is read by default and evaluated.
    print("var1 is lesser")#body this line is only executed if the above clause evaluates to 'True'
elif var1 > var2:#this clause is only evaluated, aka read by the interpreter, if the previous clause evaluated to 'False', and as such did not execute its body
    print("var1 is greater")#body once more, this line only executes if the clause in its header evaluates to 'True'
else:#this runs if and only if all of the previous clauses do not meet the criteria necessary to evaluate to 'True'. Think of it as the last resort for if any of the
    #previous statements did not execute their body.
    """#nondeterminate(while-loop);implicit
#Boolean operators/evaluators: used to evaluate if conjunctive elements of a conditional clause or expression should be evaluated to 'True' or 'False'
#== : 'equals'
#!= : 'does not equal'
#> : 'greater than', opposite/complement of <=
#< : 'less than', opposite/complement of >=
#>= : 'greater than OR equal to'
#<= : 'less than OR equal to'
#AND : Boolean 'AND'
#OR : Boolean 'OR'"""
while var1 < var2:
    print(var1)
    var1+=1


