def attach(s1,s2):
    s3=s1+s2
    print('Total String:',s3)
attach('New','York')
attach('York','New')






def grocery(item,price):
    print('Item;%s'%item)
    print('Price:%.2f'%price)
grocery('Sugar',56.89)
grocery(item='Sugar',price=56.89)
grocery(price=56.89,item='Sugar')










def grocery(item,price=50):
    print('Item;%s'%item)
    print('Price:%.2f'%price)
grocery('Sugar',56.89)
grocery(item='Sugar',price=56.89)
grocery(price=56.89,item='Sugar')
grocery('Sugar')













def add(*ags):
    total=0
    for x in args:
        total+=x
    print('Sum:',total)
    


    