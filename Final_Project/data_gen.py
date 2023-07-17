import numpy as np
m=10000
d=50
with open('./Final_Project/database.txt','w') as data :
    for i in range(m) :
        point_vector=np.random.uniform(-1000,1000,(d,1))
        for point in point_vector :
            data.write(str(float(point)))
            data.write(" ")
        data.write("\n")
            