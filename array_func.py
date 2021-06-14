'''
@Author : Nida Jawre
@Date: 2021-06-14
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-14
@Title: Data Structure Array
'''

from numpy import array
from logging_configuration import logging_config
logger = logging_config.get_logger()

class MyArray:
    def __init__(self):
        pass
    def accept_elements(self):
        '''
        Description: Function to accept the elements of array
        paramenter: None
        return: Array
        '''
        row = int(input("Enter number of rows for first matrix "))
        col = int(input("Enter number of column for first matrix "))
        matric = []
        for r in range(row):
            arr = []
            print('Enter elements: ')
            for c in range(col):
                arr.append(int(input()))
            matric.append(arr)
        return matric

      
    def display_elements(self,my_array):
        '''
        Description: Function to print the elements of array
        paramenter: Array
        return: None
        '''
        print(my_array)
        
    def reverse_array(self,my_array):
        '''
        Description: Function to reverse the elements in row of array
        paramenter: Array
        return: row elements reversed Array
        '''
        for i in range(len(my_array)):
            my_array[i].reverse()
            # print(my_array[i])
        return my_array

        
    def number_occurence(self,element):
        '''
        Description: Function to accept the an element of array and print the count of occurences of that element
        paramenter: element
        return: count
        '''
        c=0
        for i in range(len(my_array)):
            c +=my_array[i].count(element)
        return c
    def remove_element(self):
        pass

if __name__ == '__main__':
    obj = MyArray()
    try:
        my_array = obj.accept_elements()
        obj.display_elements(my_array)
        my_array = obj.reverse_array(my_array)
        print('After reverse')
        obj.display_elements(my_array)
        element = int(input('Enter the value to find its occurence count: '))
        if obj.number_occurence(element) > 0:
            print(f'The nummber of times {element} ocuurs = {obj.number_occurence(element)}')
        else:
            print('Not found')
    except Exception as e:
        logger.exception(e)
        # print(e)
