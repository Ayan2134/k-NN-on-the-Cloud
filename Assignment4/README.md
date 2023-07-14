# **Assignment 4**
## *Instructions about running the code* :
 
- **Cloud Server** : 
     - First locate the the folder name Cloud_Server within the Assignment 4 directory. Run the following commands for cloud_server within that folder.
     - Then we need to build the docker container using the following command : **docker build -t cloud_server .**
     - Then we need to run the container along with its volume and bind mount using this command : 

        **docker run -it -p 127.0.0.1:2002:2002 --mount type=volume,src=factors-db,target=/database/query_data --mount type=bind,src=/tmp/data,target=/database/factor_data cloud_server**
     - This will create two mounts targeted at /database where I have made two seperate folders query_data and factor_data which stores the querys and factorizations respectively
     - The data is stored in two seperate files namely query.txt and prime_factors.txt 
- **Data Owner** :
     - To run data_owner.py use the command : **python3 data_owner.py**
     - The server will start and it will be listening on 127.0.0.1 port:2000
- **Query User** :
     - To run user.py use the command : **python3 user.py**
     - Then the user will start and will ask for the input of a number which will be used for further computation within data_owner and cloud_server