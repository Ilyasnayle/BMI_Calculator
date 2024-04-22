#TEAM Members name:

    #Ilyas Nayle
    #Abdallah Adil Awad BASHIR
    #Robera T. Gobosho

#EXCERCISE ONE - a

#list examples:
list_one = [1,2,3,4,5,7,8,9,11]
list_two = [10,11,12,13,14,15,16,17,18]


def Create_New_List(odd_number,even_number):
    #new_list = []
    
    list_1 = ([num for num in odd_number if num % 2 != 0])
    list_2 = ([num for num in even_number if num %2 == 0])
    return list_1, list_2
        
        
odd_list, even_list = Create_New_List(list_one,list_two)
print(f"Odd Numubered list {odd_list}")
print(f"Even Numubered list {even_list}")

#EXCERCISE 1-b --> Count the lenght

def count_lenght(num):
 #   legnth = str(len(num))
  #  return lenght
    count = 0
    
    while num > 0:
        count = count +1 
        num = num // 10
    return count


number = 75869

print(f'Total count number {count_lenght(number)}')


#Excercise Two --> product of two integers

def product(int1,int2):
    if int1 * int2 <= 1000:
        return int1 * int2
    else:
        return int1 + int2
        
num1 = 10
num2 = 200

result = product(num1,num2)

print(f'Result {result}')


#Excercise Three --> Remove repeated 

def remove_item(a_list,item):
    while item in a_list:
        a_list.remove(item)
        
my_list = [1,2,20,3,20,4,5,20,75]
remove_from_list = 20

remove_item(my_list,remove_from_list)

print(f'Result after removing {remove_from_list} is {my_list}')



#Excercise Four --> Tuples

old_tuple = (1,2,3,44,55,66,77)

new_tuple = old_tuple[3:5]

print(new_tuple)
type(new_tuple)

####

firstTuple = (55, 2, 66, 45, 86)
toBeCopied = (45, 55)
 
def copyTupleElements(elements, myTuple):
    newTuple = ()
    for item in myTuple:
        if item in elements:
            newTuple = newTuple + (item,)
    return newTuple
 
result = copyTupleElements(toBeCopied, firstTuple)
print(result)



#Excercise five --> Dictionary 

sample_dict = {"name":"Kelly","age":25,"salary":8000,"city":"New York"}

k=["name", "salary"]

"""def extract_dict(extract_dict,keys):
    values = []
    for x in keys:
        if x in extract_dict:
            values.append(extract_dict[x])
        else:
            values.append(extract_dict[None])
            
value_to_extract = ["name","salary"]
"""

def extract(dict: dict, keys: list):
    result={}
    for key in keys:
        result[key]=dict.get(key)

    return result 


z = extract(sample_dict,k)

print("The result is: ", z)


# Excercise 7 --> Writing data into json file.

import json
import io

# Define data
data = {"id":1,"name":"value2","age":29}

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(data == data_loaded)


# Excercise 7--> Accessing the data from json file by key and sorting the data.
import json


with open('data.json') as file:
    data = json.load(file)

print(data)

name = data["name"]

print(f"The result is {name}\n")


sort = {}
for x in sorted(data):
    sort[x] = data[x]
    
print(f"After sorting the result is {sort}\n")

