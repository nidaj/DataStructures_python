'''
@Author : Nida Jawre
@Date: 2021-06-14
@Last Modified by: Nida Jawre
@Last Modified time: 2021-06-14
@Title: Data Structure Dictionary
'''
from logging_configuration import logging_config
logger = logging_config.get_logger()

class My_dictionary:
    
    def accept_items(self):
        '''
        Description: Method accepting items in dictionary
        param:None
        return: dictionary
        '''
        dict = {}
        size = int(input('Enter the size of dictionary'))
        for i in range(size):
            key = input('Enter the key value:')
            item = input('Enter the value:')
            if key in dict.keys():
                print('key is repeated')
                key = input('Enter the new key value:')
                dict[key] = item
            else:
                dict[key] = item
        return dict

        
    def display_keys(self,dict):
        '''
        Description:Method to display keys of a dictionay
        param:dictionary
        return:None
        '''
        for key in dict.keys():
            print(key)

    def display_values(self,dict):
        '''
        Description: Method to display values of a dictionary
        param: Dictionary
        return: None
        '''
        for item in dict.values() :
            print(item)
        
    def display_key_value(self, dict):
        '''
        Description: Method to display key value pair in a dictionary
        param: Dictionary
        return: None
        '''
        for key,value in dict.items():
            print(f'{key} : {value} ')
        
    def sort_by_value(self,dict):
        '''
        Description: Sort dictionary with respect to value
        param: Dictionary
        return: Dictionary
        '''

        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}
        return dict
        
    def sort_by_keys(self,dict):
        '''
        Description: Sort dictionary with respect to Keys
        param: Dictionary
        return: Dictionary
        '''
        print('Dictionary Sorted by key')
        dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[0])}
        return dict
        

if __name__ == '__main__':
    obj = My_dictionary()
    try:
        dict = obj.accept_items()
        obj.display_keys(dict)
        obj.display_values(dict)
        obj.display_key_value(dict)
        print('Sorted by value: ')
        obj.display_key_value(obj.sort_by_value(dict))
        print('Sorted by key: ')
        obj.display_key_value(obj.sort_by_keys(dict))
    except Exception as e:
        logger.exception(e)