'''
* Copyright 2016 Hackers' Club, University Of Peradeniya
* Author : Irunika Weeraratne E/11/431
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*
'''

'''
TASK 1:
add dict dictionary object to myList
sort array by index
select first 4 elements
sort it by name
print the list
'''


#Answer
dict = {'id':4, 'name': 'Amare'} #This is a dictionary in Python which is similar data structure like 'struct' in C
print 'id :', dict['id'] #Extract 'id' from the dictionary 'a'
print 'name :', dict['name'] #Extracted 'name' from the dictionary 'a'

myList = [
    {'id':2, 'name':'Bhagya'},
    {'id':1, 'name':'Irunika'},
    {'id':7, 'name':'Tharinda'},
    {'id':3, 'name':'Ruchira'},
    {'id':6, 'name':'Namodya'},
    {'id':5, 'name':'Menaka'}
]

myList.append(dict) #add dict dictionary object to myList
myList.sort(key=lambda x:x['id']) #Sort array by index
myList_new = myList[0:4] #select first 4 elements
myList_new.sort(key=lambda item:item['name']) #sort it by name

#print the list
for item in myList_new:
    print item

