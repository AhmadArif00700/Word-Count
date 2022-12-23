
import threading
import re
import time

def CountFrequency(my_list):
 
    file1 = open("frequencycount.txt","w")
    total = sum(d.values())
    for key in list(my_list.keys()):
        str1 = "The word '" + key + "' frequncy count is " + str((my_list[key]/total)*100) +"%\n"
        file1.write(str1)

def wordcount(d, word1):
    print (word1, " : ", d[word1] )

# Open the file in read mode

text = open("The Escape of Alice.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    # Convert the characters in line lowercase to avoid case mismatch
    line = line.strip()
    line = line.lower()
    line = re.sub(r'[^\w\s]','',line)
  
    # Split the line into words
    words = line.split(" ")
                         
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
start = time.time()
t1 = threading.Thread(target = wordcount, args=(d,"the"))    
t2 = threading.Thread(target = wordcount, args=(d,"by"))  
t3 = threading.Thread(target = wordcount, args=(d,"and"))
t4 = threading.Thread(target = wordcount, args=(d,"so")) 
t5 = threading.Thread(target = wordcount, args=(d,"because")) 
t6 = threading.Thread(target = wordcount, args=(d,"find")) 
t7 = threading.Thread(target = wordcount, args=(d,"can")) 
t8 = threading.Thread(target = wordcount, args=(d,"has")) 
# # # starting thread 1
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()



# # wait until thread 1 is completely executed
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
end = time.time()
    
CountFrequency(d)





 
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end - start)*1000)
    
    