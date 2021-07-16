# Loops
1. What is the diffrence between = and ==
Answer: = is an asignmenet operator while == is a comparison operator

2. Can i leave out the collon in an if, while, or for statement? yes/No
Answer: No 

3. Should i Use tab character to indent my code? Yes/No
Answer: Yes

4. Compose a program that takes three integers comand line arguments and writes 'equal' if all three are equal, and 'not equal' otherwise
Answer: is in inputabc.py in the repository   

5. what is th e value of j after each of the following code fragments is executed
a. j = 0  
    for i in range(0, 10):  
        j += i  
ANswer: value of J is 45  

b. j = 1  
    for i in range(0, 10):  
        j += j  

Answer: value of J is 1024  

c. for j in range(0, 10):  
    j += j  

Answer: value of J is 18  

6. what are m and n after the following code is executed?
n = 123456789  
m = 0  
while n != 0:  
    m = (10 * m) + (n % 10)  
    n //= 10  

Answer: the value of m is 987654321  
Answer: the value of n is 0  

7. what does this code write?
f = 0  
g = 1  
for i in range (0, 16):  
    f = f + g  
    g = f - g  
    stdio.writeIn(f)  

Answer: NameError: name 'stdio' is not defined

8. Bonus Question: is there an example for when the following for and while loops are not equivalent?
for variable in range(start, stop):  
    statement 1  
    statement 2  
    ....  
      
    variable = start  
    while variable < stop
        statement1  
        statement2  
        ....  
        variable += 1  
    
    Answer : No  


    