#                                   MIA HERLINAWATI
#   UAS_PEMROGRAMAN TERSTRUKTUR      191240000905
#                                  HOME CAKE & DRINK


import datetime
import time
now  = datetime.datetime.now()
date = now.date()
time = now.time()

d_code_cake = {"1":"1","2":"2","3":"3","4":"4","5":"5"}
d_name_cake = {"1":"Banana Crepes", "2":"Blueberry Polo Bun", "3":"Chicken BBQ Pizza Slice", "4":"Choco Bun", "5":"Lemon Creamcheese Bun"}
d_price_cake= {"Banana Crepes":8500,"Blueberry Polo Bun":12000,"Chicken BBQ Pizza Slice":12500,"Choco Bun":9000,"Lemon Creamcheese Bun":10000}

d_code_drink = {"1":"1", "2":"2", "3":"3", "4":"4", "5":"5"}
d_name_drink = {"1":"Strawberry Milkshake", "2":"Chocolate Milkshake", "3":"Classic Milk Tea", "4":"English Rose Tea", "5":"Cosmopolitan"}
d_price_drink= {"Strawberry Milkshake":13000,"Chocolate Milkshake":15000,"Classic Milk Tea":12500,"English Rose Tea":9000,"Cosmopolitan":15000}


d_cost_cake   = []
d_amount_cake = []
d_total_cake  = []
d_menu_cake   = []

d_cost_drink   = []
d_amount_drink = []
d_total_drink  = []
d_menu_drink   = []
i=0

logo = '''
===================================================================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~|      CAKE & DRINK      |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
===================================================================================
'''


def join():
    print '''
                      # SELECT MENU JOIN#
                     =====================
                           1. Admin      
                           2. Chasier
                           3. Exit       
                     ~~~~~~~~~~~~~~~~~~~~~
         '''
    while True:
        choice = raw_input('\t\t Enter Selection :')
        if choice == '1':
            login()
            break
        elif choice=='2':
            calculate()
            break
        elif choice=='3':
            break
        elif not choice:
            print
        else:
            print

print ' '


def add_cake():
    print '''
                        # ADD CAKE #
                     |-----------------|
                     
        '''
    kd_cake = raw_input('\t | Code Cake  | \t:')
    mn_cake = raw_input('\t | Name Cake  | \t:')
    pc_cake = input('\t | Price Cake | \t:')
    print

    d_code_cake [kd_cake] = kd_cake
    d_name_cake [kd_cake] = mn_cake
    d_price_cake [mn_cake] = int(pc_cake)
    
    view()
    while True:
        Q = raw_input('\t ~~~> Again (Y/N) :')
        if Q == 'y':
            add_cake()
        elif Q=='n':
            join()
            break
        elif not Q:
            print
        else:
            print

def add_drink():
    print '''
                        # ADD DRINK #
                     |-----------------|
                     
        '''
    kd_drink = raw_input('\t | Code Drink  | \t:')
    mn_drink = raw_input('\t | Name Drink  | \t:')
    pc_drink = input('\t | Price Drink | \t:')
    print

    d_code_drink [kd_drink] = kd_drink
    d_name_drink [kd_drink] = mn_drink
    d_price_drink [mn_drink] = int(pc_drink)
    
    view()
    while True:
        Q = raw_input('\t ~~~> Again (Y/N) :')
        if Q == 'y':
            add_drink()
        elif Q=='n':
            join()
            break
        elif not Q:
            print
        else:
            print



def add () :
    print '''
                       ; ; Add Menu ; ;
                     ********************
                           1. Cake
                           2. Drink
'''

    while True:
        select = raw_input('\t\t\t Enter Selection :')
        if select == '1':
            add_cake()
            break
        elif select == '2':
            add_drink()
            break
        elif not select:
            print
        else:
            print



def delete ():
    print '''

                    ; ; Delete Menu ; ;
                         1. Cake
                         2. Drink
        '''

    while True:
        choose = raw_input('\t      Enter Selection : ')
        if choose == '1':
            delete_cake()
            break
        elif choose == '2':
            delete_drink()
            break
        elif not choose:
            print
        else:
            print


def delete_cake ():
    print '''
                            ; ; Delete Cake ; ;
                        **************************

'''
    nm_cake = raw_input('\t  | Name Cake | \t : ')
    print ' \t          ~~~~>', d_name_cake[nm_cake],'Telah Terhapus'
    menu_cake = d_name_cake[nm_cake]
    del d_code_cake[nm_cake]
    del d_name_cake[nm_cake]
    del d_price_cake[menu_cake]
    print


    while True:
        q = raw_input ('\t      ----> Lagi (Y/N) : ')
        if q == 'y':
            delete_cake()
            break
        elif q == 'n':
            join()
            break
        elif not q:
            print
        else:
            print



def delete_drink():
    print '''
                            ; ; Delete Drink ; ;
                        **************************

        '''
    name_drink = raw_input('\t  | Name Drink | \t :')
    print ' \t          ~~~~>', d_name_drink[name_drink],'Telah Terhapus'
    menu_drink = d_name_drink[name_drink]
    del d_code_drink[name_drink]
    del d_name_drink[name_drink]
    del d_price_drink[menu_drink]
    print


    while True:
        q = raw_input ('\t      ----> Lagi (Y/N) : ')
        if q == 'y' :
            delete_drink()
            break
        elif q == 'n':
            join()
            break
        elif not q:
            print
        else:
            print



def edit ():
    print ('''

                    ; ; Edit Menu ; ;
                        1. Cake
                        2. Drink
        '''.center(75))

    while True:
        choose = raw_input('\t      Enter Selection : ')
        if choose == '1':
            edit_cake()
            break
        elif choose == '2':
            edit_drink()
            break
        elif not choose:
            print
        else:
            print


def edit_cake ():
    print ('''
               ; ; ; Edit Menu Cake ; ; ;
               **************************

        '''.center(50))

    code_cake = raw_input ('\t  | Code cake  | \t :')
    cake = d_name_cake[code_cake]
    print '\t  |Name Cake | \t : ',cake
    menu = raw_input('\t  | Replace With | \t : ')
    price= raw_input('\t  | The Price of The Menu | \t : ')
    print

    d_name_cake [code_cake]=menu
    d_price_cake[d_name_cake[code_cake]] = int(price)
    while True :
        q = raw_input ('\t      =====>> Lagi (Y\N) : ')
        if q == 'y':
            edit_cake()
            break
        elif q == 'n':
            join()
            break
        elif not q :
            print
        else:
            print


def edit_drink() :
    print ('''
               ; ; ; Edit Menu Drink ;
               **************************

        '''.center(50))

    code_drink = raw_input ('\t  | Code drink  | \t :')
    drink = d_name_drink[code_drink]
    print '\t  |Name Drink | \t : ',drink
    menu = raw_input('\t  | Replace With | \t : ')
    price= raw_input('\t  | The Price of The Menu | \t : ')
    print

    d_name_drink [code_drink]=menu
    d_price_drink[d_name_drink[code_drink]] = int(price)
    while True :
        q = raw_input ('\t      =====>> Lagi (Y\N) : ')
        if q == 'y':
            edit_drink()
            break
        elif q == 'n':
            join()
            break
        elif not q :
            print
        else:
            print



def view ():
    print ('''
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                           ; ; ; The View Menu ; ; ;                           %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            ''')

    print ' '
    print ' Code Cake  : ',d_name_cake
    print ' Price Cake : ',d_price_cake
    print ' Code Drink : ',d_name_drink
    print ' Price Drink: ',d_price_drink

    print ' '
    while True :
        Q = raw_input ('\t      =====>> Lagi (Y\N) : ')
        if Q == 'y':
            view()
            break
        elif Q == 'n':
            cashier()
            break
        elif not Q :
            print
        else:
            print


def views():
    print ('''
<%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%>
<%                          View Of Menu                                       %>
<%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%>
        ''')

    print ' '
    print ' Code Cake  : ',d_name_cake
    print ' Price Cake : ',d_price_cake
    print ' Code Drink : ',d_name_drink
    print ' Price Drink: ',d_price_drink

    print ' '


def cashier():
    print logo
    print ('''
````````````````````````````````````````````````````````````````````````````````
`                        ;;; Edit Menu ;;;                                     `
`                   ``````````````````````````                                 `
`                        1. The View Menu                                      `
`                        2. Add Menu Cake                                      `
`                        3. Add Menu Drink                                     `
`                        4. Delete Menu Cake                                   `
`                        5. Delete Menu Drink                                  `
`                        6. Edit Menu Cake                                     `
`                        7. Edit Menu Drink                                    `
`                        8. Exit                                               `
````````````````````````````````````````````````````````````````````````````````
''')
    print ' '
    choose = raw_input ('\t\t\t Enter Selection : ')
    if choose == '1':
        view()
    elif choose == '2':
        add_cake()
    elif choose == '3':
        add_drink()
    elif choose == '4':
        delete_cake()
    elif choose == '5':
        delete_drink()
    elif choose == '6':
        edit_cake()
    elif choose == '7':
        edit_drink()
    elif choose == '8':
        join()
    else:
        print (' The Choice You includeed is Incorrect')
        calculate()


def Rp (money):
    y=str(money)
    if len(y) <=3:
        return y
    else:
        p=y[-3:]
        q=y[:-3]
        return Rp (q)+','+p
    print Rp(q)+','+p



def calculate ():
    print logo
    views()


    while True:
        print ('# Press P/p When Finished Ordering to Continue Payment #')
        print ' '
        print ('Enter Purchase')
        print ' '
        cd_a = raw_input('Enter The Cake Code : ')
        cd_b = raw_input('Enter Drink Code    : ')
        print ' '
        print 75*'='
        print ' '



        if cd_a == 'p' or cd_b == 'P':
            break
        elif cd_a == d_code_cake[cd_a] or cd_b == d_code_drink[cd_b]:
            mn_cake     = d_name_cake [cd_a]
            mn_drink    = d_name_drink[cd_b]
            pc_cake     = d_price_cake [d_name_cake [cd_a]]
            pc_drink    = d_price_drink [d_name_drink[cd_b]]

            d_cost_drink.append(pc_drink)
            d_cost_cake.append(pc_cake)
            d_menu_cake.append(mn_cake)
            d_menu_drink.append(mn_drink)


            print ' '
            
            print ' '
            print '     |',mn_cake,'\t\t = Rp', Rp(pc_cake)
            qty = input('   | The Amount of Cake \t = ')
            d_amount_cake.append(qty)
            sum_cake= qty*pc_cake
            print '         | The Amount of The Price \t\t = Rp',Rp(pc_cake)
            d_total_cake.append(sum_cake)
            total = sum(d_total_cake)

            print ' '
            print '     |',mn_drink,'\t\t = Rp',Rp(pc_drink)
            qty = input('   | The Amount of Drink \t = ')
            d_amount_drink.append(qty)
            sum_drink= qty*pc_drink
            print '         | The Amount of The Price \t\t = Rp',Rp(pc_drink)
            d_total_drink.append(sum_drink)
            total = sum(d_total_drink)
            print ' '


    total = sum(d_total_cake)+sum(d_total_drink)
    print 75*'-'
    print '     The Amount of The Purchase \t = Rp',Rp(total)
    money = input('     money \t\t = Rp')
    print '     Change \t\t = Rp',Rp(money-total)

    print
    for n in range(20):
        print

        
    print '''
                                    HOME CAKE & DRINK
                                 Jln . Matoa Raya KM. 3
                                          Pati
                               NPWP : 01.223.876.8-98.098
    '''
    print '\t\t ========================================================'
    for n in range(len(d_menu_cake)):
        n+1
    for a in range(len(d_menu_drink)):
        n+1
        print '\t\t  %s \t\t %s \t%s \t%s'%(d_menu_cake[n],d_amount_cake[n],Rp(d_cost_cake[n]),Rp(d_total_cake[n]))
        print '\t\t  %s \t\t %s \t%s \t%s'%(d_menu_drink[n],d_amount_drink[n],Rp(d_cost_drink[n]),Rp(d_total_drink[n]))
        d_sum = sum_cake+sum_drink

    print '\t\t --------------------------------------------------------'
    print '\t\t  Total Items\t', sum((d_amount_cake)+(d_amount_drink)), '\t\t',Rp(total)
    print '\t\t  Cash\t\t\t\t',Rp(money)
    print '\t\t  Change\t\t\t\t', Rp(money-total)
    print '\t\t ========================================================'
    print '\t\t\t      Date. %s-%s-%s  %s:%s:%s '%(date.day,date.month,date.year,time.hour,time.minute,time.second), 'V.1'
    print'''\t\t --------------------------------------------------------
                                 Thanks You for Visiting
                                            at
                                   Home Cake and Drink
                                 Don't Forget Come Back
    '''
    while True:
        q= raw_input('\t    ~~~> Again (Y/N) : ')
        if q == 'y' or 'Y':
            join()
        elif q == 'n' or 'N':
            join()
            break
        elif not q:
            print
        else:
            print



            


def login ():
    print logo
    print '''
                            ;;; LOGIN ;;;
                     ------------------------------
'''
    username = raw_input('\t\t  Enter Your Username :')
    password = raw_input('\t\t  Enter Your Password :')
    username_from_db = 'admin'
    password_from_db = 'admin'
    print ' '
    if username == username_from_db and password == password_from_db:
        cashier()
    elif username != username_from_db and password != password_from_db:
        print ' Only admins have access here'
    else:
        print "Sorry you can't come in here"
    return join()

    
    
print logo
print '''
                             ;;;     LOG IN    ;;;
                             ~~~~~~~~~~~~~~~~~~~~~
                                    1. Admin
                                    2. Cashier
                                    3. Exit
 '''

while True:
    choice = raw_input('\t\t masukkan pilihan : ')
    if choice == "1":
        login()
        break
    elif choice == '2':
        calculate()
        break
    elif choice == '3':
        break
    elif not choice:
        print
    else:
        print














            
