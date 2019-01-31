
def composition_bluda ():
    composition=list()
    cook_book ={}
    with open('blyda.txt', encoding='utf-8') as f:
        #print(f.read())
        for line in f:
            str=line.rstrip('\n')
            bludo=str.rstrip('\n')
            str = f.readline()
            ll_menu=[]
            #print ('bludo',bludo)
            kol_vo= int(str.rstrip('\n'))
            #print('kol-vo',kol_vo)
            for massiv in range(kol_vo):
                composition = []
                str=f.readline()
                str=str.rstrip('\n')
                for i in str.split(' | '):
                    composition.append(i)
                ll_menu.append({'ingridient_name': composition[0] , 'quantity': int(composition[1]), 'measure': composition[2]})
            cook_book[bludo] = ll_menu
    print('=============================================')
    print('========cook_book============================')
    print('=============================================')
    print(cook_book)
    print('=============================================')
    return cook_book

def get_shop_list_by_dishes(dish,person,cook_book):
    len_dish = len(dish)
    dict_dish = {}
    for d in dish:
        for key, val in cook_book.items():
            if key == d:
                l_menu=[]
                for l in val:
                    #print (l)
                    #print(l['ingridient_name'])
                    #print(l['quantity'])
                    #print(l['measure'])
                    #print()
                    dict_dish[l['ingridient_name']] = {'measure':l['measure'], 'quantity': l['quantity']*person}

    #print(dict_dish)
    return dict_dish



cook_book_rez = composition_bluda()
dishes_list=['Омлет','Утка по-пекински','Запеченный картофель']
print('======================================================')
print('=====Список покупок для блюд {} ===='.format(dishes_list))
print('======================================================')
rezult = get_shop_list_by_dishes(dishes_list,2,cook_book_rez)
print(rezult)
print('======================================================')

