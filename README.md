# Assignment1
First assignment for my SOC homomorphic encryption for k-NN on the cloud 
Query user :
The query_user is the client here it take an input from the user and send it to the data_owner 
Data owner :
It takes the number from the query user and multiply it with a randomly generated number (using "random" module of python) now this new number is sent back to the query_user, after this whole communication the server is still on for more requests as it is accepting connection requests in a loop.
Cloud :
It takes the new number from the query_user and then sends back the prime factorization of that number.

1. Run the cloud.py and data_owner.py it two seperate terminals. 
2. Run user.py in another terminal and enter the integer input as asked.
3. The cloud and data_owner will remain open for requests whole time so we can run user.py repetitively without the need to repeatedly run the cloud and data_owner.