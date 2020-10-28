# Python3 code to demonstrate 
# consecutive element pairing  
# using zip() 
  
# initializing list 
test_list = [5, 4, 1, 3, 2] 
  
# printing original list 
print("The original list : " + str(test_list)) 
  
# using zip() 
# consecutive element pairing  
res = list(zip(test_list, test_list[1:])) 
  
# print result 
print("The consecutive element paired list is : " + str(res)) 
