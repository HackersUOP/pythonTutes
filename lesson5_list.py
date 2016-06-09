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
List:
List is one of the most powerful data structure in python
It can used as
    1.List :
        Usual operations of list can be done using python
    2.Stack :
        append(element) - To insert(push) an element to the stack
        pop() - To pop element from the stack
    3.Queue :
        append(element) - To insert an element to Queue
        pop(0) - To pop element from the queue

'''
list = []
print 'List:', list, '\n'

numberList = [6,5,3,4,9,2,1]
print 'numberList:', numberList, '\n'

fruitList = ['orange', 'apple', 'banana']
print 'fruitList:', fruitList , '\n'


#Add new number to back
numberList.append(8)
print 'append 8 to numberList:', numberList, '\n'

#Poping numbers from any index
number1 = numberList.pop()
number2 = numberList.pop(3)
numberList.insert(3,10) #insert a number to given index
print 'popped numbers:', number1, number2
print 'After popping last and 3rd element of the list and adding 10 as 3rd element:\n', numberList, '\n'


numberList.sort(reverse=False)
print 'Sorted numberList:', numberList
fruitList.sort(reverse=False)
print 'Sorted fruitList', fruitList
numberList.sort(reverse=True)
print 'Reverse sorted numberList:', numberList
fruitList.sort(reverse=True)
print 'Reverse sorted fruitList:', fruitList, '\n'



#In below loop each element is taken from the list and printed
#This is one of the powerful feature in Python's 'for loop'
for fruit in fruitList:
    print fruit

numberList.sort()
print
for number in numberList[0:100]:
    print number



