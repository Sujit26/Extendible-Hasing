import string
import random
import csv

def visulaize(directory):
    print("-"*13,"|     Directory Visualization     |","-"*13)
    for directory_record in directory.directory_records:
        print("Directory Record:",directory_record.hash_prefix)
        # print("\tlocal_depth:",directory_record.value.local_depth)
        if(directory_record.value!=None):
            for transaction in directory_record.value.index:
                print("\tBucket Number:", directory_record.value.id,"  ",transaction)

def hash_funtion(key):
    return  '{0:016b}'.format(key)

class Bucket:
    def __init__(self,local_depth,index,empty_spaces,id):
        self.id = id
        self.local_depth = local_depth
        self.index = index
        self.empty_spaces = empty_spaces

class Directory:
    def  __init__(self,global_depth,directory_records):
        self.global_depth = global_depth,
        self.directory_records = directory_records

class DirectoryRecord:
    def __init__(self,bucket,hash_prefix):
        self.hash_prefix = hash_prefix
        self.value = bucket


def GenerateData(number_of_trasaction):
    with open('dataset.csv', 'w') as dataset:
        csv_writer = csv.writer(dataset)
        for i in range(number_of_trasaction):
            t_id = i+1
            t_amount = random.randint(1, 500000)
            c_name = ''.join(
                random.choice(string.ascii_uppercase)
                for x in range(3)
            )
            c_item = random.randint(1, 1500)
            csv_writer.writerow([t_id, t_amount, c_name, c_item])
    return "dataset.csv"

