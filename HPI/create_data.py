import  pandas as pd
import numpy as np
import os


dir_to_create_data = raw_input("Please enter directory to create data : ")
records = int(raw_input("Please enter number of records for each file : "))
num_of_files = int(raw_input("Please enter number of files to create : "))
for i in range(num_of_files):
    userlist =[]
    namelist = np.random.choice(["tim", "bob", "alice", "tom", "ben", "roy"], size=records)
    domainlist = np.random.choice(["hotmail.com", "yahoo.com", "msn.com", "gmail.com"], size=records)

    for p in range(records):
        line = [namelist[p], "@".join([namelist[p],domainlist[p]])]
        userlist.append(line)
        #print line

    userlist = np.array(userlist)
    users = pd.DataFrame(userlist,columns=["name","email"])
    users.to_csv(os.path.join(dir_to_create_data,"userlist_{}.csv".format(i)) ,index=False)