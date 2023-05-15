Modified Assignment 1 :
    The cloud server was modified by implementing prime factorization using the in-built function of SageMath 
    I have provided the cloud server in python code format which was generated from the sagemath code.
Query user :
    The query_user is the client here it take an input from the user and send it to the data_owner 
Data owner :
    It takes the number from the query user and multiply it with a randomly generated number (using "random" module of python) now this new number is sent back to the query_user, after this whole communication the server is still on for more requests as it is accepting connection requests in a loop.
Cloud :
    It takes the new number from the query_user and then sends back the prime factorization of that number using SageMath factor() function.

1. Run the cloud.py and data_owner.py it two seperate terminals. 
2. Run user.py in another terminal and enter the integer input as asked.
3. The cloud and data_owner will remain open for requests whole time so we can run user.py repetitively without the need to repeatedly run the cloud and data_owner.

Amicable Numbers :

    I have used the sigma() function of SageMath here which takes two arguments one for the number and second for the power of its divisors for the sum of them all.
    Amicable numbers are pair of numbers whose sum of divisors is equal to the second number and vica versa.
    The code transverses through the numbers until the counter 'num' = index (10 in this case) and check the sum of divisors for each number and their corresponding result of sigma().

    On running the code with python first 10 amicable numbers will be printed.
    This code prints only first 10 amicable numbers , but it can be changed by changing the 'index' variable to the required number

K digit prime :
    
    I have used random_prime(upper_bound , proof_status , lower_bound) function from sagemath to generate two random prime numbers 'p' and 'q' of given digits 'k'.
    Then i have declared a function solver() to recursively solve my a*p + b*q = 1 equation. Then printed the results some comments have been provided in the code to give reason for certain steps.

    On running the code with python Enter the number of digits you want in the primes 'p' and 'k'.
    Then the suitable coefficients for 'p' and 'q' will be printed in the format of (p,q,a,b) .

Carmichael Numbers :

    I have used is_prime() and euler_phi() function from sagemath as I used the fact that the definition condition of Euler Totient theorem is satisfied by euler_phi()
    as well as n-1. 

    On running the code Enter the number till which carmichael numbers are to be printed .This will print the carmichael numbers less than and equal to that number.
