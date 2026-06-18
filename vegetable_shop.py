#DATA
items = ['ONION','BRINJAL','CARROT','BEETROOT','DRUMSTICK']
quantity_kgs = [20,20,15,20,10]
price_kg = [35,24,18,36,15]
cost_price = [20,18,16,30,12]
all_userdetails = []
total_sales = 0

#START
while True:
    start = input('Do you want to open the shop(1.YES/2.NO):')
    print()
    if start == '1':


        #ROLE
        while True:
            role = input('Which role do you want(1.OWNER/2.USER/3.EXIT):')
            print()


            #OWNER
            if role == '1':
                print('*'*10,'Welcome to owner section','*'*10)
                print()
                while True:
                    choose = input('Which option do you want(1.ADDITEMS/2.REMOVEITEMS/3.UPDATEITEMS/4.INVENTORY/5.USERDETAILS/6.REPORT/7.TEMIZEDPROFIT/8.EXIT):')
                    print()


                    #ADD ITEMS
                    if choose == '1':
                        while True:
                            print('The avialable items are:')
                            for i in zip(items,quantity_kgs,price_kg):
                                    print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','PRICE = ',i[2])
                            print()
                            add_items = input('Do you want to add items to inventory?(1.YES/2.NO):')
                            print()
                            if add_items == '1':
                                addingitem_name = input('Enter the item name to add in inventory:')
                                if addingitem_name in items:
                                    print('Item already exisits')
                                    print()
                                else:
                                    items.append(addingitem_name)
                                    print('Item added succsessfully')
                                    print()
                                    addingitem_quantity = float(input('Enter how many quantities you want to add:'))
                                    quantity_kgs.append(addingitem_quantity)
                                    print('quantity added succsessfully')
                                    print()
                                    addingitem_price = float(input('Enter the price of the item you had added:'))
                                    price_kg.append(addingitem_price)
                                    print('price added succsessfully')
                                    print()
                                    adding_costprice = float(input('Enter the item cost price:'))
                                    cost_price.append(adding_costprice)
                                    print('cost price added succsessfully')
                                    print()
                            elif add_items == '2':
                                break
                            else:
                                print('Choose correct option:')
                                print()


                    #REMOVE ITEMS
                    elif choose == '2':
                        while True:
                            print('The avialable items are')
                            for i in zip(items,quantity_kgs,price_kg):
                                    print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','PRICE = ',i[2])
                            print()
                            remove_items = input('Do you want to remove items from inventory?(1.YES/2.NO):')
                            print()
                            if remove_items == '1':
                                print('The available items are:',items)
                                print()
                                removingitem_name = input('Enter the item name to remove from inventory:')
                                if removingitem_name in items:
                                    index = items.index(removingitem_name)
                                    items.pop(index)
                                    quantity_kgs.pop(index)
                                    price_kg.pop(index)
                                    cost_price.pop(index)
                                    print('Item removed successfully')
                                    print()
                                else:
                                    print('Entered item is not exists')
                                    print()
                            elif remove_items == '2':
                                break
                            else:
                                print('Choose correct option:')
                                print()


                    #UPDATE ITEMS
                    elif choose == '3':
                        while True:
                            print('The avialable items are')
                            for i in zip(items,quantity_kgs,price_kg):
                                print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','PRICE = ',i[2])
                            print()
                            update_items = input('Do you want to update any items in inventory?(1.YES/2.NO):')
                            print()
                            if update_items == '1':
                                data = input('Which data want to be update(1.ITEMS/2.QUANTITY/3.PRICE/4.COSTPRICE):')
                                print()
                                if data == '1':
                                    existing_name = input('Enter the exsisting name:')
                                    print()
                                    if existing_name in items:
                                        new_name = input('Enter new name:')
                                        print()
                                        index = items.index(existing_name)
                                        items[index] = new_name
                                        print('Item name updated successfully')
                                        print()
                                    else:
                                        print('Item not in list')
                                        print()
                                elif data == '2':
                                      quantity_name = input('Enter the quantity item name:')
                                      print()
                                      if quantity_name in items:
                                        new_quantity = float(input('Enter the new quantity:'))
                                        print()
                                        index = items.index(quantity_name)
                                        quantity_kgs[index] = new_quantity
                                        print('Item quantity updated successfully')
                                        print()
                                      else:
                                        print('Item not in list')
                                        print()
                                elif data == '3':
                                        price_name = input('Enter the price item name:')
                                        print()
                                        if price_name in items:
                                            new_price = float(input('Enter the new price:'))
                                            print()
                                            index = items.index(price_name)
                                            price_kg[index] = new_price
                                            print('Item price updated successfully')
                                            print()
                                        else:
                                            print('Item not in list')
                                            print()
                                elif data == '4':
                                        costprice_name = input('Enter the new cost price name:')
                                        print()
                                        if costprice_name in items:
                                            new_costprice = float(input('Enter the new cost price:'))
                                            print()
                                            index = items.index(costprice_name)
                                            cost_price[index] = new_costprice
                                            print('Item cost price updated successfully')
                                            print()
                                        else:
                                            print('Item not in list')
                                            print()
                                else:
                                    print('Choose correct option')
                                    print()
                            elif update_items == '2':
                                break
                            else:
                                print('Choose correct option')
                                print()



                    #INVENTORY
                    elif choose == '4':
                        while True:
                             inventory = input('Do you want to see inventory(1.YES/2.NO):')
                             print()
                             if inventory == '1':
                                 for i in zip(items,quantity_kgs,price_kg):
                                     print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','PRICE = ',i[2])
                                 print()
                             elif inventory == '2':
                                 break
                             else:
                                 print('Choose correct option:')
                                 print()
                                 
                         

                    #USER DETAILS
                    elif choose == '5':
                        while True:
                            ask_user_details = input('Do you want to see user details:(1.YES/2.NO)')
                            print()
                            if ask_user_details == '1':
                                for individual in all_userdetails:
                                    print('USER:')
                                    for each in individual:
                                        print(each)
                                    print()
                            elif ask_user_details == '2':
                                break
                            else:
                                print('Choose correct option')
                                print()




                    #VIEW REPORT
                    elif choose == '6':
                        while True:
                            report = input('Do you want final report(1.YES/2.NO):')
                            print()
                            if report == '1':
                                print('*'*20,'Today total sales:', total_sales,'*'*20)
                                print()
                                print('The remaining stock details:')
                                for i in zip(items,quantity_kgs,price_kg):
                                    print('ITEM = ',i[0],'     ','QUANTITY = ',i[1],'     ')
                                print()
                            elif report == '2':
                                break
                            else:
                                print('Enter correct option')
                                print()



                    #ITEMIZED PROFIT
                    elif choose == '7':
                        while True:
                            itemized_profit = input('Do you want to open itemized profit(1.YES/2.NO):')
                            print()
                            if itemized_profit == '1':
                                total_profit = 0
                                for veg_name in items:
                                    profit = 0
                                    index = items.index(veg_name)
                                    for user in all_userdetails:
                                        for data in user[:-1]:
                                            if data[0] == veg_name:
                                                profit = profit + (price_kg[index] - cost_price[index]) * data[1]
                                    print('ITEM =',veg_name, 'PROFIT =',profit)
                                    total_profit = total_profit + profit
                                print()
                                print('*'*20,'TOTAL PROFIT =', total_profit,'*'*20)
                                print()
                            elif itemized_profit == '2':
                                break
                            else:
                                print('Choose correct option')
                                print()


                    elif choose == '8':
                        break
                    else:
                        print('Choose correct option')
                        print()


            #USER
            elif role == '2':
                print('*'*10,'Welcome to user section','*'*10)
                print()
                cart_items = []
                cart_quantity = []
                cart_price = []
                total = 0
                while True:
                    choose = input('Which option do you want(1.ADDITEMS/2.REMOVEITEMS/3.MODIFYITEMS/4.VIEWCART/5.BILLING/6.EXIT):')
                    print()
                    #ADD CART
                    if choose == '1':
                        print('The avialable items in shop are:')
                        for i in zip(items,quantity_kgs,price_kg):
                            print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','PRICE = ',i[2])
                        print()
                        while True:
                            print('The avialable items in cart:')
                            print()
                            for i in zip(cart_items,cart_quantity,cart_price):
                                print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','AMOUNT = ',i[2])
                            print('TOTAL AMOUNT:',total)
                            print()
                            ask = input('What do you want:')
                            print()
                            if ask in items:
                                quantity_ask = float(input('How many kgs do you want:'))
                                index = items.index(ask)
                                if quantity_ask <= quantity_kgs[index]:
                                    if ask in cart_items:
                                        print('Item already in cart. Use MODIFY CART option.')
                                        print()
                                    else:
                                        amount = quantity_ask*price_kg[index]
                                        cart_items.append(ask)
                                        cart_quantity.append(quantity_ask)
                                        cart_price.append(amount)
                                        total = total+amount
                                        print('Item added to cart suuccesfully')
                                        print()
                                else:
                                    print('That much quantity is not avaialble')
                                    print()
                            elif ask == 'DONE':
                                break
                            else:
                                print('ITEM IS NOT AVAILABLE')
                                print()

                    #REMOVE CART
                    elif choose == '2':
                        while True:
                            print('The avialable items in cart:')
                            for i in zip(cart_items,cart_quantity,cart_price):
                                print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','AMOUNT = ',i[2])
                            print('TOTAL AMOUNT:',total)
                            print()
                            remove_ask = input('Do you want to remove any item from cart(1.YES/2.NO):')
                            print()
                            if remove_ask == '1':
                                removeitem_ask = input('Enter the item to remove from cart:')
                                if removeitem_ask in cart_items:
                                    removeitem_askindex = cart_items.index(removeitem_ask)
                                    total = total - cart_price[removeitem_askindex]
                                    cart_items.pop(removeitem_askindex)
                                    cart_quantity.pop(removeitem_askindex)
                                    cart_price.pop(removeitem_askindex)
                                    print('Item removed from cart successfully')
                                    print()
                                else:
                                    print('Enter correct item')
                                    print()
                            elif remove_ask == '2':
                                break
                            else:
                                print('Choose correct option')
                                print()

                    #MODIFY CART
                    elif choose == '3':
                        while True:
                            print('The avialable items in cart:')
                            for i in zip(cart_items,cart_quantity,cart_price):
                                print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','AMOUNT = ',i[2])
                            print('TOTAL AMOUNT:',total)
                            print()
                            modify_ask = input('Do you want to modify the cart(1.YES/2.NO):')
                            print()
                            if modify_ask == '1':
                                modify_cart = input('Enter the item name to modify the quantity:')
                                print()
                                if modify_cart in cart_items:
                                    new_modifyquantity = float(input('Enter the new quantity:'))
                                    new_modifyquantityindex = cart_items.index(modify_cart)
                                    if new_modifyquantity <= quantity_kgs[new_modifyquantityindex]:
                                        cart_quantity[new_modifyquantityindex] = new_modifyquantity
                                        old_price = cart_price[new_modifyquantityindex]
                                        cart_price[new_modifyquantityindex] = (new_modifyquantity)*price_kg[new_modifyquantityindex]
                                        total = total - old_price + cart_price[new_modifyquantityindex]
                                        print('Quantity modified in cart successfully')
                                        print()
                                    else:
                                        print('That much quantity is not there')
                                        print()
                                else:
                                    print('Choose correct option')
                                    print()
                            elif modify_ask == '2':
                                break
                            else:
                                print('Choose correct option')
                                print()


                    #VIEW CART
                    elif choose == '4':
                        while True:
                            view_cart = input('Do you want to view the cart(1.YES/2.NO):')
                            print()
                            if view_cart == '1':
                                for i in zip(cart_items,cart_quantity,cart_price):
                                    print('ITEM = ',i[0],'/','QUANTITY = ',i[1],'/','AMOUNT = ',i[2])
                                print('TOTAL AMOUNT:',total)
                                print()
                            elif view_cart == '2':
                                break
                            else:
                                print('Choose corret option')
                                print()

                    #BILLING
                    elif choose == '5':
                        while True:
                            if len(cart_items) == 0:
                                print('Cart is empty')
                                print()
                                break
                            print('-'*25,'FINAL BILL','-'*25)
                            for i in zip(cart_items,cart_quantity,cart_price):
                                    print('ITEM = ',i[0],'     ','QUANTITY = ',i[1],'     ','AMOUNT = ',i[2])
                            print('-'*60)
                            print('TOTAL AMOUNT:','                                     ',total)
                            print()
                            billing = input('Do you want to pay the bill?(1.YES/2.NO):')
                            print()
                            if billing == '1':
                                name = input('Enter customer name: ')
                                print()
                                while True:
                                    mobile = input('Enter mobile number: ')
                                    print()
                                    if mobile.isdigit() and len(mobile) == 10:
                                        break
                                    else:
                                        print('Mobile number must contain exactly 10 digits')
                                        print()
                                user_details = []
                                user_details.append(('NAME', name))
                                user_details.append(('MOBILE', mobile))
                                for change_item in cart_items:
                                    if change_item in items:
                                        first_index = items.index(change_item)
                                        second_index = cart_items.index(change_item)
                                        quantity_kgs[first_index] = quantity_kgs[first_index]-cart_quantity[second_index]
                                for i in zip(cart_items,cart_quantity,cart_price):
                                    user_details.append(i)
                                user_details.append(('TOTAL', total))
                                all_userdetails.append(user_details)
                                total_sales = total_sales + total
                                break
                            elif billing == '2':
                                print('Please pay the bill:')
                                print()
                            else:
                                print('Choose correct option')
                                print()
                    elif choose == '6':
                        break
                    else:
                        print('Choose correct option')
                        print()
            #ROLE
            elif role == '3':
                print('Store clsoed successfully')
                print()
                break
            else:
                print('Choose correct option')
                print() 
        if role == '3':
            break      
                
    #START
    elif start == '2':
        close = input('Do you want to close the shop(1.YES/2.NO):')
        print()
        if close == '1':
            print('Store closed successfully')
            break
        elif close == '2':
            start
        else:
            print('Choose correct option')
            print()
    else: 
        print('Choose correct option')
        print()
