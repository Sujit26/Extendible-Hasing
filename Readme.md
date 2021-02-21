NAME    ::  SUJIT JAIWALIYA             ROLL NO ::  2017CSB11115

# EXTENDIBLE HASING


HOW TO RUN
----------
    1. Extract the zip file
    3. To run the code type `python3 E_Hashing.py`
    4. This will start the code and will ask you to enter the metadata required to run the code. viz. bucket_size and a boolean to show logs.
    5. The code will present you with multiple options which can be used to check the correctness of the code.
# Options
    ------------Menu------------
    1 : Data Generation
    2 : Simulate Secondary Memory
    3 : Add transaction in bulk
    4 : Add single transaction
    5 : Visualise
    6 : Exit

    1 : Data Generation
    This option will let you generate a new random dataset in which you have the option to change the number of transactions.

    2 : Simulate Secondary Memory 
    This will ask you bucket size & read data from "dataset.csv"

    3 : Add transaction in bulk
    This will all transactions from secondary memory to our functionality

    4 : Add single transaction
    This option can be used to add transaction one at a time by providing it with 
        (1) Transaction ID, 
        (2) Transaction sale amount, 
        (3) Customer name and, 
        (4) category of item.
    
    5. Visualise 
    This option is to print the formed extendible hash in a readable format. 
    Note: This will print a bucket multiple times which are linked by the bucket address table multiple times.

    7. `Exit:` This option is to exit the code.


Directory Structure
----------------------

                                           |------> Transaction1
    Directory                              |------> Transaction2
        Directory_Record1  ---> bucket ----|------> Transaction3
        Directory_Record2                  |------> Transaction4
        Directory_Record3 
        Directory_Record4
        ..
        ..
