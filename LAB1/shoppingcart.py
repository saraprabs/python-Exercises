'''
Shopping Cart Program 
Simulate a shopping cart using lists. 
Steps: 
1. Start with an empty list cart = [] 
2. Ask user 5 times to input an item and append it 
3. After all items are added: 
o Print the full cart 
o Remove the last item 
o Show how many items remain 
o Print only the first and last items 
Goal: Combine lists, len(), append(), pop(), indexing.
'''
lst_cart = []
for _ in range(5):
    item = input("Enter item: ")
    lst_cart.append(item)

print("Shopping cart: ")
for i in lst_cart:
    print(i)

lst_cart.pop()

print("NUmber of items remaining: ", len(lst_cart))

print(lst_cart[0], lst_cart[-1])

