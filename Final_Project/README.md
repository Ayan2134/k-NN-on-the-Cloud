# **SoC Final Project** 
## How to Run the Code ?
- ### Data Generation
    - Run the data_gen.py file to generate **10000 datapoint** which are of **50 dimensions each** using command : **python3 data_gen.py**
    - This will make a file named "database.txt"
    - The values of **data range from -10 to 10**

- ### Cloud_Server 
    - The Cloud Server folder contains the Dockerfile to run the docker container and cloud_server.py which runs the Cloud Server 
    - To build docker container use the command : **docker build -t cloud_server .**
    - To run the container use the command : **docker run -it -p 127.0.0.1:3001:3001 cloud_server**
    - This will start the Cloud Server in the docker container and it will start listening for requests on **port : 3001**.
    - Also the Cloud Server needs the number of Nearest Neighbours that it will send to the query user.

- ### Data Owner 
    - To start the Data Owner use the following command : **python3 data_owner.py**
    - This command will start the Data Owner which will listen on the **port : 3000**
    - After running the query_user and entering 50 values of datapoint the data owner will ask for approval in form of "1 and 0" i.e "Yes or No"
    - If 1 is entered then the query will be approved and the working will continue else in case of 0 the query will be declined and no further process will take place.
- ### Query User
    - To send query using query user run the code query_user.py using command : **python3 query_user.py**
    - Enter a query consisting 50 values each value ranging from **-10 to 10 both inclusive** 

## What is happening ?

- The Data Owner takes its database and it pertubs the vectors of database by using some vectros with random values and sends it over to Cloud Server 
- When you enter query point in the query user it sends it, after encrypting it using Paillier Cryptosystem to the Data Owner for its approval
- On denial the query is not processed further and the query user is denied of data point indexes
- If Data Owner accepts the query then the data owner perform certain operations on the new query point which is formed after adding a vector containing random values.
- During this whole process with data owner the query remainins in its encrypted form which is the beauty of Homomorphic encryption :) 
- Then this query is sent back to Query User which takes this query and decrypts it and sends this decrypted query to the cloud server
- The cloud server takes this query and calculate the k-NN entered, the k needs to be entered to the cloud server when it is executing for each query point.
- It then sends the index of the database that the k-NN of the query corresponds to , back to the Query User. 
- Using this the original query of the user is not revealed and also the data of the Data Owner is not leaked to the Cloud Server
