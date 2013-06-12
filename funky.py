def daimFunc (number1, number2):
    return number1 * number2

print daimFunc(2, 2)


class MyClass:
    variable = "blah"
    
    def function(self):
        print "This is a message inside the class."

myobjectx = MyClass()
 
print myobjectx.variable

myobjectx.variable = "yackity"

myobjectx.variable2 = "boo"

print "variable is now: " + myobjectx.variable
print "variable2 is now: " + myobjectx.variable2