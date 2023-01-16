####  importing modules #################

from tkinter import *
from copy import deepcopy
import pandas.io.sql as sql
import mysql.connector as msqc
import pyttsx3
import datetime

#############voice engine ###############
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
##dbms connection and window creation####
root_window = Tk()
cart = {}
bill = ''
mydb = msqc.connect(
    host='localhost',
    user='root',
    passwd='rssbrssb',
    database='ordersdb'
)
cursor = mydb.cursor()
##############  button logics ###################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good MORNING ")
    if hour >= 12 and hour < 16:
        speak("good Afternoon")
    if hour >= 16 and hour < 23:
        speak("good evening ")
    speak("Welcome to McDonald's")
#################################################
def menu():
    ################    sub button logics   ##############
    global main_screen_frame
    global root_menu
    global voiceactivation
    root_menu = Toplevel()
    root_menu.title('Menu')
    root_menu.geometry('750x500')
    root_menu.configure(bg='black')
    upper_frame_menu = Frame(root_menu, bg="red")
    upper_frame_menu.pack(side=TOP, fill="x")
    greet_text_menu = Label(upper_frame_menu, text="MENU", bg="yellow", fg="red", font="Helvetica 32 bold")
    greet_text_menu.pack()
    side_bar_menu_frame = Frame(root_menu, bg='black')
    side_bar_menu_frame.pack(side=LEFT, fill=Y)
    main_screen_frame = Frame(root_menu, bg='black')
    main_screen_frame.pack(side=RIGHT, fill=X)

    def burger():
        main_screen_frame.pack_forget()
        main_screen_frame2 = Frame(root_menu, bg='black')
        main_screen_frame2.pack(fill=X)
        ################################
        alootiki_burger = Label(main_screen_frame2, text="Aloo Tikki", bg="black", fg="white", font="Helvetica 16")
        alootiki_burger.grid(row=0, column=0, padx=30, pady=20)
        at_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        at_price_menu.grid(row=1, padx=30, pady=0)
        atq = IntVar()
        atq_entry = Entry(main_screen_frame2, textvariable=atq)
        atq_entry.grid(row=2, padx=30, pady=0)
        mcspicy_burger = Label(main_screen_frame2, text="McSpicey", bg="black", fg="white", font="Helvetica 16")
        mcspicy_burger.grid(row=0, column=3, padx=30, pady=20)
        mcspicy_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        mcspicy_price_menu.grid(row=1, column=3, padx=30, pady=0)
        mcspicyq = IntVar()
        mcspicy_entry = Entry(main_screen_frame2, textvariable=mcspicyq)
        mcspicy_entry.grid(row=2, column=3, padx=30, pady=0)
        maharaja_mac_burger = Label(main_screen_frame2, text="Maharaja Mac", bg="black", fg="white",
                                    font="Helvetica 16")
        maharaja_mac_burger.grid(row=0, column=5, padx=30, pady=20)
        maharaja_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        maharaja_price_menu.grid(row=1, column=5, padx=30, pady=0)
        maharajaq = IntVar()
        maharaja_entry = Entry(main_screen_frame2, textvariable=maharajaq)
        maharaja_entry.grid(row=2, column=5, padx=30, pady=0)
        mcpaneer_burger = Label(main_screen_frame2, text="Mc Paneer", bg="black", fg="white", font="Helvetica 16")
        mcpaneer_burger.grid(row=3, column=0, padx=30, pady=20)
        mcp_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        mcp_price_menu.grid(row=4, column=0, padx=30, pady=0)
        mcpq = IntVar()
        mcpq_entry = Entry(main_screen_frame2, textvariable=mcpq)
        mcpq_entry.grid(row=5, column=0, padx=30, pady=0)
        big_mac_burger = Label(main_screen_frame2, text="Big Mac", bg="black", fg="white", font="Helvetica 16")
        big_mac_burger.grid(row=3, column=3, padx=30, pady=20)
        bm_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        bm_price_menu.grid(row=4, column=3, padx=30, pady=0)
        bmq = IntVar()
        bmq_entry = Entry(main_screen_frame2, textvariable=bmq)
        bmq_entry.grid(row=5, column=3, padx=30, pady=0)
        doublecheese_burger = Label(main_screen_frame2, text="Double cheeseBurger", bg="black", fg="white",
                                    font="Helvetica 16")
        doublecheese_burger.grid(row=3, column=5, padx=30, pady=20)
        dcb_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        dcb_price_menu.grid(row=4, column=5, padx=30, pady=0)
        dcbq = IntVar()
        dcbq_entry = Entry(main_screen_frame2, textvariable=dcbq)
        dcbq_entry.grid(row=5, column=5, padx=30, pady=0)

        def add_to_cartb():
            global at
            global bm
            global maharaja
            global dcb
            global mcp

            # getting values
            at = atq.get()
            bm = bmq.get()
            maharaja = maharajaq.get()
            dcb = dcbq.get()
            mcp = mcpq.get()
            mcspicy = (mcspicyq.get())
            burgermenu = {'Aloo tiki': (at, 100), 'Big Mac': (bm, 100), 'Double Cheese Burger': (dcb, 100),
                          "Mc Paneer": (mcp, 100),
                          "Mc spicy": (mcspicy, 100)}
            b = deepcopy(burgermenu)
            for k, (v, r) in b.items():
                if v == 0:
                    del burgermenu[k]
            cart.update(burgermenu)
            print(cart)
            main_screen_frame2.forget()

        add_to_cart_buttonb = Button(main_screen_frame2, text='ADD TO CART | CLOSE', bg="black", fg="white",
                                     font="Helvetica 12 bold", command=add_to_cartb)

        add_to_cart_buttonb.grid(row=6, column=3, padx=10, pady=10)
        ####################################################

    def pizza():
        main_screen_frame.pack_forget()
        main_screen_frame2 = Frame(root_menu, bg='black')
        main_screen_frame2.pack(fill=X)
        ################################
        margherita = Label(main_screen_frame2, text="Margherita", bg="black", fg="white", font="Helvetica 16")
        margherita.grid(row=0, column=0, padx=30, pady=20)
        marg_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        marg_price_menu.grid(row=1, padx=30, pady=0)
        margq = IntVar()
        margq_entry = Entry(main_screen_frame2, textvariable=margq)
        margq_entry.grid(row=2, padx=30, pady=0)
        Supreme_mexicana = Label(main_screen_frame2, text="Supreme Mexicana", bg="black", fg="white",
                                 font="Helvetica 16")
        Supreme_mexicana.grid(row=0, column=3, padx=30, pady=20)
        sup_mex_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        sup_mex_price_menu.grid(row=1, column=3, padx=30, pady=0)
        supmexq = IntVar()
        supmexq_entry = Entry(main_screen_frame2, textvariable=supmexq)
        supmexq_entry.grid(row=2, column=3, padx=30, pady=0)
        Italian_delight = Label(main_screen_frame2, text="Italian Delight", bg="black", fg="white",
                                font="Helvetica 16")
        Italian_delight.grid(row=0, column=5, padx=30, pady=20)
        it_del_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        it_del_price_menu.grid(row=1, column=5, padx=30, pady=0)
        it_del_q = IntVar()
        it_del_entry = Entry(main_screen_frame2, textvariable=it_del_q)
        it_del_entry.grid(row=2, column=5, padx=30, pady=0)
        farmerhouse = Label(main_screen_frame2, text="Farmhouse", bg="black", fg="white", font="Helvetica 16")
        farmerhouse.grid(row=3, column=0, padx=30, pady=20)
        farm_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        farm_price_menu.grid(row=4, column=0, padx=30, pady=0)
        farmq = IntVar()
        farmq_entry = Entry(main_screen_frame2, textvariable=farmq)
        farmq_entry.grid(row=5, column=0, padx=30, pady=0)
        chilliyexpress = Label(main_screen_frame2, text="Chilly Express", bg="black", fg="white", font="Helvetica 16")
        chilliyexpress.grid(row=3, column=3, padx=30, pady=20)
        ce_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        ce_price_menu.grid(row=4, column=3, padx=30, pady=0)
        ceq = IntVar()
        ceq_entry = Entry(main_screen_frame2, textvariable=ceq)
        ceq_entry.grid(row=5, column=3, padx=30, pady=0)
        doublecheese = Label(main_screen_frame2, text="Double cheese", bg="black", fg="white",
                             font="Helvetica 16")
        doublecheese.grid(row=3, column=5, padx=30, pady=20)
        dcp_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        dcp_price_menu.grid(row=4, column=5, padx=30, pady=0)
        dcpq = IntVar()
        dcpq_entry = Entry(main_screen_frame2, textvariable=dcpq)
        dcpq_entry.grid(row=5, column=5, padx=30, pady=0)

        def add_to_cartp():
            global marg
            global ita
            global supmex
            global dcp
            global ce
            global farm

            # getting values
            marg = margq.get()
            ita = it_del_q.get()
            supmex = supmexq.get()
            dcp = dcpq.get()
            ce = ceq.get()
            farm = (farmq.get())
            pizzamenu = {'Margherita': (marg, 100), 'Italian Delight': (ita, 100), 'Double Cheese Pizza': (dcp, 100),
                         "Chilly Express": (ce, 100)
                , "FarmHouse": (farm, 100)}
            p = deepcopy(pizzamenu)
            for k, (v, r) in p.items():
                if v == 0:
                    del pizzamenu[k]
            cart.update(pizzamenu)
            main_screen_frame2.forget()
            print(cart)

        add_to_cart_buttonp = Button(main_screen_frame2, text='ADD TO CART', bg="black", fg="white",
                                     font="Helvetica 12 bold", command=add_to_cartp)

        add_to_cart_buttonp.grid(row=6, column=3, padx=10, pady=10)
        ####################################################

    def sides():
        main_screen_frame.pack_forget()
        main_screen_frame2 = Frame(root_menu, bg='black')
        main_screen_frame2.pack(fill=X)
        ################################
        garlic_bread = Label(main_screen_frame2, text="Garlic Bread", bg="black", fg="white", font="Helvetica 16")
        garlic_bread.grid(row=0, column=0, padx=30, pady=20)
        gb_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        gb_price_menu.grid(row=1, padx=30, pady=0)
        gbq = IntVar()
        gbq_entry = Entry(main_screen_frame2, textvariable=gbq)
        gbq_entry.grid(row=2, padx=30, pady=0)
        potato_poppers = Label(main_screen_frame2, text="Potato poppers", bg="black", fg="white",
                               font="Helvetica 16")
        potato_poppers.grid(row=0, column=3, padx=30, pady=20)
        pp_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        pp_price_menu.grid(row=1, column=3, padx=30, pady=0)
        ppq = IntVar()
        ppq_entry = Entry(main_screen_frame2, textvariable=ppq)
        ppq_entry.grid(row=2, column=3, padx=30, pady=0)
        pasta = Label(main_screen_frame2, text="Pasta Arrabiata", bg="black", fg="white",
                      font="Helvetica 16")
        pasta.grid(row=0, column=5, padx=30, pady=20)
        pasprice_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        pasprice_menu.grid(row=1, column=5, padx=30, pady=0)
        pasq = IntVar()
        pas_entry = Entry(main_screen_frame2, textvariable=pasq)
        pas_entry.grid(row=2, column=5, padx=30, pady=0)
        Paneer_tikka = Label(main_screen_frame2, text="Paneer_tikka", bg="black", fg="white", font="Helvetica 16")
        Paneer_tikka.grid(row=3, column=0, padx=30, pady=20)
        pt_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        pt_price_menu.grid(row=4, column=0, padx=30, pady=0)
        ptq = IntVar()
        ptq_entry = Entry(main_screen_frame2, textvariable=ptq)
        ptq_entry.grid(row=5, column=0, padx=30, pady=0)
        frenchfries = Label(main_screen_frame2, text="French Fries", bg="black", fg="white", font="Helvetica 16")
        frenchfries.grid(row=3, column=3, padx=30, pady=20)
        ff_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        ff_menu.grid(row=4, column=3, padx=30, pady=0)
        ffq = IntVar()
        ffq_entry = Entry(main_screen_frame2, textvariable=ffq)
        ffq_entry.grid(row=5, column=3, padx=30, pady=0)
        cheese_garlic_bread = Label(main_screen_frame2, text="Cheese Garlic Bread", bg="black", fg="white",
                                    font="Helvetica 16")
        cheese_garlic_bread.grid(row=3, column=5, padx=30, pady=20)
        cgb_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        cgb_price_menu.grid(row=4, column=5, padx=30, pady=0)
        cgbq = IntVar()
        cgbq_entry = Entry(main_screen_frame2, textvariable=cgbq)
        cgbq_entry.grid(row=5, column=5, padx=30, pady=0)

        def add_to_cartp():
            global gb
            global pp
            global pas
            global cgb
            global pt
            global ff

            # getting values
            gb = gbq.get()
            pp = ppq.get()
            pas = pasq.get()
            cgb = cgbq.get()
            pt = ptq.get()
            ff = (ffq.get())
            sidesmenu = {'Garlic Bread': (gb, 100), 'Potato Poppers': (pp, 100), 'Cheese Garlic Bread': (cgb, 100),
                         "Paneer Tikka": (pt, 100),
                         "French Fries": (ff, 100)}
            s = deepcopy(sidesmenu)
            for k, (v, r) in s.items():
                if v == 0:
                    del sidesmenu[k]
            cart.update(sidesmenu)
            main_screen_frame2.forget()
            print(cart)

        add_to_cart_buttonp = Button(main_screen_frame2, text='ADD TO CART', bg="black", fg="white",
                                     font="Helvetica 12 bold", command=add_to_cartp)

        add_to_cart_buttonp.grid(row=6, column=3, padx=10, pady=10)
        ####################################################

    def dessert():
        main_screen_frame.pack_forget()
        main_screen_frame2 = Frame(root_menu, bg='black')
        main_screen_frame2.pack(fill=X)
        ################################
        Chocolate_icecream = Label(main_screen_frame2, text="Choclate Ice cream", bg="black", fg="white",
                                   font="Helvetica 16")
        Chocolate_icecream.grid(row=0, column=0, padx=30, pady=20)
        ci_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        ci_price_menu.grid(row=1, padx=30, pady=0)
        ciq = IntVar()
        ciq_entry = Entry(main_screen_frame2, textvariable=ciq)
        ciq_entry.grid(row=2, padx=30, pady=0)
        Chocalate_cake = Label(main_screen_frame2, text="Chocolate Cake", bg="black", fg="white",
                               font="Helvetica 16")
        Chocalate_cake.grid(row=0, column=3, padx=30, pady=20)
        cc_price_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        cc_price_menu.grid(row=1, column=3, padx=30, pady=0)
        ccq = IntVar()
        ccq_entry = Entry(main_screen_frame2, textvariable=ccq)
        ccq_entry.grid(row=2, column=3, padx=30, pady=0)
        Vanilla_icecream = Label(main_screen_frame2, text="Vanilla Ice cream", bg="black", fg="white",
                                 font="Helvetica 16")
        Vanilla_icecream.grid(row=0, column=5, padx=30, pady=20)
        viprice_menu = Label(main_screen_frame2, text="RUPEES 100", bg='black', fg='white', font="Helvetica 8")
        viprice_menu.grid(row=1, column=5, padx=30, pady=0)
        viq = IntVar()
        vi_entry = Entry(main_screen_frame2, textvariable=viq)
        vi_entry.grid(row=2, column=5, padx=30, pady=0)

        def add_to_cartp():
            global ci
            global cc
            global vi
            # getting values
            ci = ciq.get()
            cc = ccq.get()
            vi = viq.get()

            dessertmenu = {'Chocolate Ice Cream': (ci, 100), 'Chocolate Cake': (cc, 100),
                           'Vanilla Ice Cream': (vi, 100)}
            d = deepcopy(dessertmenu)
            for k, (v, r) in d.items():
                if v == 0:
                    del dessertmenu[k]
            cart.update(dessertmenu)
            main_screen_frame2.forget()
            print(cart)

        add_to_cart_buttonp = Button(main_screen_frame2, text='ADD TO CART', bg="black", fg="white",
                                     font="Helvetica 12 bold", command=add_to_cartp)

        add_to_cart_buttonp.grid(row=6, column=3, padx=10, pady=10)

    burger_button = Button(side_bar_menu_frame, text='Burgers', bg="black", fg="white", font="Helvetica 12 bold",
                           command=burger)
    burger_button.grid(row=0, column=0, pady=20)
    pizza_button = Button(side_bar_menu_frame, text='Pizza', bg="black", fg="white", font="Helvetica 14 bold",
                          command=pizza)
    pizza_button.grid(row=1, column=0, pady=20)
    dessert_button = Button(side_bar_menu_frame, text='Desert', bg="black", fg="white", font="Helvetica 12 bold",
                            command=dessert)
    dessert_button.grid(row=2, column=0, pady=20)
    sides_button = Button(side_bar_menu_frame, text='Sides', bg="black", fg="white", font="Helvetica 14 bold",
                          command=sides)
    sides_button.grid(row=3, column=0, pady=20)
    root_menu.update()
    speak("we have Burgers, Pizzas, Sides and Desserts,Please Select One")
    root_menu.mainloop()
#################################################
def checkout():
    ##########window parameters#######################
    root_checkout = Toplevel()
    root_checkout.title('Checkout')
    root_checkout.geometry('750x750')
    root_checkout.configure(bg='black')
    upper_frame_checkout = Frame(root_checkout, bg="red")
    upper_frame_checkout.pack(side=TOP, fill="x", pady=50)
    greet_text_checkout = Label(upper_frame_checkout, text="Checkout", bg="yellow", fg="red", font="Helvetica 32 bold")
    greet_text_checkout.pack()

    #############button logics##########################
    def cart_unloader1():
        ###################################################
        # cart unloading#
        print(cart)
        bill = ""
        f = []
        for k, (v, r) in cart.items():
            a = v * r
            f.append((k, v, r, a))
        insertinginbill = "INSERT INTO bill (item,quantity,price,net_amount) VALUES (%s,%s,%s,%s)"
        cursor.executemany(insertinginbill, f)

        insertinginorders = "INSERT INTO allorders (item,quantity,price,net_amount) VALUES (%s,%s,%s,%s)"

        mydb.commit()
        df = sql.read_sql('select * from bill', mydb)
        lower_frame_checkout = Frame(root_checkout, bg="black")
        lower_frame_checkout.pack(side=TOP, fill="x")
        bill_text_checkout = Label(lower_frame_checkout, text=df, bg="black", fg="white", font="Helvetica 12 ")
        bill_text_checkout.pack()
        cursor.executemany(insertinginorders, f)

    def fc():
        global root_checkout
        df = sql.read_sql('select * from bill', mydb)
        print(df)
        df.to_excel('bill.xls')
        cursor.execute("DELETE FROM bill")
        mydb.commit()
        speak("Thank you for visiting us, your order will get ready soon")
        root_window.quit()

    cart_unloader = Button(root_checkout, text="BILL DISPLAY", bg="black", fg="white", font="Helvetica 12 bold",
                           command=cart_unloader1)
    cart_unloader.pack()
    finalcheckout = Button(root_checkout, text="CHECKOUT", bg="black", fg="white", font="Helvetica 12 bold",
                           command=fc)
    finalcheckout.pack(pady=10)
    root_checkout.mainloop
##############  window parameters ###############
root_window.title("BILLING SOFTWARE")
root_window.geometry("600x300")
upper_frame = Frame(root_window, bg="red")
upper_frame.pack(side=TOP, fill="x")
greet_text = Label(upper_frame, text="Welcome to Mc Donald's", bg="yellow", fg="red", font="Helvetica 32 bold")
greet_text.pack()
root_window.configure(bg='black')
lower_frame = Frame(root_window, bg='black')
lower_frame.pack(side=TOP, pady=50)
ORDER_B = Button(lower_frame, text="MENU&ORDER", bg="black", fg="white", font="Helvetica 16 bold", command=menu)
ORDER_B.grid(row=8, column=9)
checkout_B = Button(lower_frame, text="CHECKOUT", bg="black", fg="white", font="Helvetica 12 bold", command=checkout)
checkout_B.grid(row=10, column=9, pady=50)
####################################################
root_window.update()
wishme()
root_window.mainloop()
#####################################################
