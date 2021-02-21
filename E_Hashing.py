#  For this question,you would have to create a synthetic table(simulating sales records of department stores)
#  containing 1 Lakh-records.
#  Each record in this file contains four fields:
#  (1)TransactionID(aninteger),
#  (2)Transaction sale amount(aninteger),
#  (3)Customer name(string)and,
#  (4)category of item.

#  TransactionID is an integer to identify each transaction uniquely in the dataset.
#  Transaction sale amount is a random integer between 1 and 500000.
#  Customer name is a random 3 letterstring.
#  You can model this as a character array of length3.
#  Category of the item is a random intege rbetween 1--1500  (uniformly distributed across the table).
#  Create 200 records in the mentioned format and store them in a file

from functions import *
import numpy as np
import os
def clear():
    return os.system('clear')

bucket_capacity = 2
bucket_number = 3
global_depth = 1


SECONDARY_MEMORY = []

####################### INITIALIZATION #############################
bucket1 = Bucket(local_depth=1, empty_spaces=bucket_capacity, index=[],id=1)
bucket2 = Bucket(local_depth=1, empty_spaces=bucket_capacity, index=[],id=2)

directory_records = list()  # list of hash prefix with bucket pointers

directory_records.append(DirectoryRecord(hash_prefix=0, bucket=bucket1))
directory_records.append(DirectoryRecord(hash_prefix=1, bucket=bucket2))

directory = Directory(global_depth=1, directory_records=directory_records)



def insert(index,lock):
    global directory
    global bucket_number
    t_id = index[0]
    hash_key = hash_funtion(int(t_id))
    
    hash_prefix = int(hash_key[-directory.global_depth[0]:], 2)

    bucket = directory.directory_records[hash_prefix].value
    bucket.index.append(index)
    bucket.empty_spaces = int(bucket.empty_spaces)-1

    if(lock):
        print()
        print("Global_depth\t:", directory.global_depth[0])
        print("Directory No\t:",hash_prefix)
        print("Bucket No\t:",bucket.id)
        print("local_depth\t:",bucket.local_depth)
        print("t_id\t\t:",index[0],"is added")

    if(bucket.empty_spaces < 0):

        tempopary_memory = bucket.index     #for rehashing
        # print("tempopary_memory:",tempopary_memory)
        bucket.empty_spaces = bucket_capacity
        bucket.index = []

        # print("GLOBAL DEPTH:",directory.global_depth)
        if(directory.global_depth[0] > bucket.local_depth):
            if(lock):
                print("BucketCapacity Exceeds,    waring --> bucket overflow")
            # NUMBER OF LINKED BUCKETS
            number_of_links = 2**(directory.global_depth[0]-bucket.local_depth)
            bucket.local_depth = bucket.local_depth + 1
            number_of_modify_links = number_of_links/2 

            new_bucket = Bucket(local_depth=bucket.local_depth,index=[],empty_spaces=bucket_capacity, id = bucket_number)


            for directory_record in directory.directory_records:
                # print(bucket)
                if(directory_record.value == bucket):
                    if(number_of_modify_links != 0):
                        number_of_modify_links = number_of_modify_links - 1
                    else:
                        directory_record.value = new_bucket
                        bucket_number = bucket_number+1

            for i in range(len(tempopary_memory)):
                if(lock):
                    print("INSETING->",tempopary_memory[i])
                insert(tempopary_memory[i],lock)
                # print(directory.global_depth)



        elif(directory.global_depth[0] == bucket.local_depth):
            if(lock):
                print("DirectoryCapacity Exceeds,    waring --> directory overflow")
            new_directory_len = 2* len(directory.directory_records)
            new_directory_records = []

            # CREATE NEW DIRECTORY TABLE WITH EMPTY DIRECTORIES
            for directory_record_number in range(new_directory_len):
                new_directory_records.append(DirectoryRecord(hash_prefix=directory_record_number,bucket=Bucket(local_depth=1,index=[],empty_spaces=bucket_capacity,id=bucket_number)))
                bucket_number=bucket_number+1
            new_directory = Directory(global_depth=directory.global_depth[0]+1,directory_records=new_directory_records)

            # REHASING

            for directory_record in directory.directory_records:
                haskey1 = '0'+hash_funtion(directory_record.hash_prefix)
                haskey2 = '1'+hash_funtion(directory_record.hash_prefix)
                new_index1 = int(haskey1[-directory.global_depth[0]:],2)
                new_index2 = int(haskey2[-directory.global_depth[0]:],2)

                new_directory.directory_records[new_index1].value = directory_record.value
                new_directory.directory_records[new_index2].value = directory_record.value

            directory= new_directory

            for i in range(len(tempopary_memory)):
                if(lock):
                    print("\t2nd for loop "+str(directory.global_depth[0]))
                    print("\tINSETING->",tempopary_memory[i])
                insert(tempopary_memory[i],lock)
    
    if(lock):
        
        visulaize(directory)
    # else:
    #     print("\n")


def simulate_secondary_memory(file_name, alpha):
    global SECONDARY_MEMORY
    with open(file_name, 'r') as fin:
        i = 1
        j = 1
        temp_storage = list()
        for line in fin:
            line_modified = line[0:].rstrip('\n').split(',')
            line_modified = [line_modified[i] if i != 1 else line_modified[i].strip(
                "\'") for i in range(len(line_modified))]
            if i != alpha:
                temp_storage.append(line_modified)
                i = i + 1
            else:

                SECONDARY_MEMORY.append(temp_storage)
                temp_storage = list()
                i = 1
                j = j + 1

def call_bulk_adder():
    print("-"*10)

    global SECONDARY_MEMORY
    # print(SECONDARY_MEMORY)
    
    for bucket1 in SECONDARY_MEMORY:
        for transaction in bucket1:
            # print(transaction)
            insert(transaction,lock= False)


if __name__ == '__main__':
    while(1):

        clear()
        print("1 : Data Generation")
        print("2 : Simulate Secondary Memory")
        print("3 : Add transaction in bulk")
        print("4 : Add single transaction")
        print("5 : Visualise")
        print("6 : Exit")
        print("---"*20)
        _input = int(input("Choose the option  : "))
        print("---"*20)

        number_of_transaction = 200
        FileName = "dataset.csv"

        if(_input==1):
            number_of_transaction = int(input("Enter number of transaction:"))
            print()
            print("Dataset is generating ....")
            FileName = GenerateData(number_of_transaction)
            print("Succesfully generated ",number_of_transaction," transactions.")
            print("Checout ",FileName," file")

        elif(_input==2):
            bucket_capacity = input("Enter bucket capacity:")
            SECONDARY_MEMORY.clear()
            simulate_secondary_memory(FileName, int(bucket_capacity))
            # print(SECONDARY_MEMORY)

        elif(_input==3):
            call_bulk_adder()

        elif(_input==4):
            t_id =      int(input("Transaction ID     : "))
            t_amount =  int(input("Transaction Amount : "))
            u_name =        input("User Name          : ")
            c_id =      int(input("Catergory ID       : "))
            insert([t_id,t_amount,u_name,c_id],lock = False)
        elif(_input==5):
            # print("d:",directory)
            visulaize(directory)
        elif(_input==6):
            break
        input("Enter any key to continue :)")


        