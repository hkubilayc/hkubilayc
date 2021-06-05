def reverselist(data,res=[]):
'''
reversing list, if there is a list in the list, it will also be affected.
'''
    data.reverse()
    for item in data:
        if type(item) == list:
            item.reverse()
        else:
            pass

