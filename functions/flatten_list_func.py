def flattenlist(data,res=[]):
  '''
    flattening fuction for lists

  '''
    for i in data:
        
        if type(i) == list:
                flattenlist(i)
                
        else:
            res.append(i)
    

