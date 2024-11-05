from cat import Cat 

print ('Welcome to my cat game!')

name=input('Enter a cat name: ')
colour= input ('Enter a cat colour: ')
my_cat=Cat(name,colour)
while True:
    action= input('''
What would you like to do :
1. Train
2. Feed
3.Play
4.Sleep 
         ''')