"""
This Implementation deals with the Graphical User Interface using the Python Framework Tkinter
"""

__author__ = '7358841, Singh'
__email__ = 's3842317@stud.uni-frankfurt.de'

import csv
from tkinter import *
from tkinter import ttk
import random


def home():
    """Displays the Home Screen , with a Button to see the Menu."""

    root = Tk()

    # ---------------Adjusted Windows Dimensions according to the need----------------------------

    width = 1000
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Tops deals with Frame widget of Tkinter , assign Text to the side Top

    Tops = Frame(root, bg='light green', width=5000, height=2500,
                 relief=SUNKEN)
    Tops.pack(side=TOP)

    # f1 deals with Frame widget of Tkinter , assign Text to the side Left

    f1 = Frame(root, width=700, height=700, relief=SUNKEN)
    f1.pack(side=BOTTOM)

    # Titles

    title = Label(
        Tops,
        font=('georgia', 20, 'bold'),
        text='Welcome',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    title.grid(row=5, column=0)

    title2 = Label(
        Tops,
        font=('georgia', 10, 'bold'),
        text='To',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    title2.grid(row=10, column=0)

    main_title = Label(
        Tops,
        font=('garamond', 100, 'bold'),
        text='BURPIZ',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    main_title.grid(row=40, column=0)

    tag_line = Label(
        Tops,
        font=('futura', 25, 'bold'),
        text='Eat. Drink. Love.',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    tag_line.grid(row=150, column=0)

    btn_menu = Button(
        f1,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('georgia', 16, 'bold'),
        width=10,
        text='Menu',
        bg='green',
        command=menu_items,
        )
    btn_menu.grid(row=5, column=0)

    root.mainloop()


def menu_items():
    """Displays the Menu after reading CSV file using Tkinter Treeview"""

    root = Tk()
    root.title('Burpiz Menu')

    # Tops deals with Frame widget of Tkinter , assign Text to the side Top

    Tops = Frame(root, bg='light green', width=5000, height=250,
                 relief=SUNKEN)
    Tops.pack(side=TOP)

    # f1 deals with Frame widget of Tkinter , assign Text to the side Bottom

    f1 = Frame(root, width=900, height=700, relief=SUNKEN)
    f1.pack(side=BOTTOM)

    # ---------------Adjusted Windows Dimensions according to the need----------------------------

    width = 1000
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Titles

    title = Label(
        Tops,
        font=('georgia', 20, 'bold'),
        text='Our Menu Card for Today ',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    title.grid(row=5, column=0)

    # Treeview initialised

    TableMargin = Frame(root, width=1000)
    TableMargin.pack(side=TOP)

    # Scrollbar Widget for both axes (x&y)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(
        TableMargin,
        columns=('name', 'typ', 'categories', 'price'),
        height=400,
        selectmode='extended',
        yscrollcommand=scrollbary.set,
        xscrollcommand=scrollbarx.set,
        )
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    # Columns of Table initialised including the Ghost Column

    tree.heading('name', text='name', anchor=W)
    tree.heading('typ', text='typ', anchor=W)
    tree.heading('categories', text='categories', anchor=W)
    tree.heading('price', text='price', anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=300)
    tree.pack()

    # Reading CSV file with csv
    # Inserting into table with loop working till number of Rows.

    with open('food (1).csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            name = row['name']
            typ = row['typ']
            categorie = row['categorie']
            price = row['price']
            tree.insert('', 0, values=(name, typ, categorie, price))
    btn_menu = Button(
        f1,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('georgia', 16, 'bold'),
        width=10,
        text='Get your Table',
        bg='green',
        command=no_of_persons,
        )
    btn_menu.grid(row=7, column=0)

    root.mainloop()


def no_of_persons():
    """This interactive Function deals to get number of Person from User """

    root = Tk()
    root.title('More Information Required!')

    # ---------------Adjusted Windows Dimensions according to the need----------------------------

    width = 1000
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)

    # Tops deals with Frame widget of Tkinter , assign Text to the side Top

    Tops = Frame(root, bg='light green', width=5000, height=250,
                 relief=SUNKEN)
    Tops.pack(side=TOP)

    # f1 deals with Frame widget of Tkinter , assign Text to the side left

    f1 = Frame(root, width=900, height=700, relief=SUNKEN)
    f1.pack(side=LEFT)

    # f2 deals with Frame widget of Tkinter , assign Text to the side right

    f2 = Frame(root, width=400, height=700, relief=SUNKEN)
    f2.pack(side=RIGHT)

    # f3 deals with Frame widget of Tkinter , assign Text to the side bottom

    f3 = Frame(root, width=400, height=700, relief=SUNKEN)
    f3.pack(side=BOTTOM)

    # Titles

    title = Label(
        Tops,
        font=('georgia', 10, 'bold'),
        text='Let us Begin with the Basics.. ',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    title.grid(row=0, column=0)

    title = Label(
        Tops,
        font=('georgia', 10, 'bold'),
        text='Please enter how many people are there? ',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    title.grid(row=5, column=0)

    l2 = Label(root, bg='light green', fg='black', width=20,
               text='Hi Welcome ')
    l2.pack()

    def print_selection(person):
        """This Function only deals provide the Output based on Scale"""

        l2.config(text='So , You are  ' + person)

    # Scale

    s = Scale(
        root,
        label=' Use Scale ',
        from_=1,
        to=8,
        orient=HORIZONTAL,
        length=200,
        showvalue=0,
        tickinterval=1,
        command=print_selection,
        )
    s.pack()

    l2 = Label(
        root,
        bg='light green',
        fg='black',
        width=50,
        text='Press NEXT to Confirm.... ',
        font=('georgia', 15),
        )
    l2.pack()
    label = Label(root)
    label.pack()

    # -----------------------------Buttons----------------------------------

    btn_next = Button(
        f2,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('ariel', 16, 'bold'),
        width=10,
        text='Next',
        bg='dark orange',
        command=table,
        )

    btn_next.grid(row=7, column=2)

    btn_cancel = Button(
        f1,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('georgia', 16, 'bold'),
        width=10,
        text='Go Back',
        bg='maroon',
        command=root.destroy,
        )
    btn_cancel.grid(row=7, column=0)

    btnreset = Button(
        f3,
        padx=16,
        pady=8,
        bd=10,
        fg='dark gray',
        font=('ariel', 16, 'bold'),
        width=10,
        text='RESET',
        bg='dark green',
        command=no_of_persons,
        )
    btnreset.grid(row=7, column=2)

    root.mainloop()


def table():
    """This Function generally assigns a Table number,
    gives a Menu Overview , and provides a Order Button."""

    root = Tk()
    root.title('Table Assigned!')

    # ---------------Adjusted Windows Dimensions according to the need----------------------------

    width = 1000
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width / 2 - width / 2
    y = screen_height / 2 - height / 2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    x = random.randrange(1, 10)

    # Tops deals with Frame widget of Tkinter , assign Text to the side Top

    Tops = Frame(root, bg='light green', width=5000, height=250,
                 relief=SUNKEN)
    Tops.pack(side=TOP)

    # f3 deals with Frame widget of Tkinter , assign Text to the side Left

    f3 = Frame(root, width=400, height=700, relief=SUNKEN)
    f3.pack(side=BOTTOM)

    # Titles

    title = Label(
        Tops,
        font=('georgia', 20, 'bold'),
        text='You have been assigned Table Number .. ',
        fg='black',
        bg='light green',
        bd=10,
        anchor='w',
        )
    title.grid(row=0, column=0)

    w = Label(
        root,
        bg='light green',
        fg='black',
        width=30,
        text=x,
        font=('georgia', 20),
        )
    w.pack()
    w1 = Label(
        root,
        bg='light green',
        fg='black',
        width=30,
        text='Please have a look at the Menu Again',
        font=('georgia', 10),
        )

    w1.pack()

    # Treeview initialised

    TableMargin = Frame(root, width=1000)
    TableMargin.pack(side=TOP)

    # Scrollbar Widget for both axes (x&y)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(
        TableMargin,
        columns=('name', 'typ', 'categories', 'price'),
        height=400,
        selectmode='extended',
        yscrollcommand=scrollbary.set,
        xscrollcommand=scrollbarx.set,
        )
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    # Columns of Table initialised including the Ghost Column

    tree.heading('name', text='name', anchor=W)
    tree.heading('typ', text='typ', anchor=W)
    tree.heading('categories', text='categories', anchor=W)
    tree.heading('price', text='price', anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=200)
    tree.column('#4', stretch=NO, minwidth=0, width=300)
    tree.pack()

    # Reading CSV file with csv
    # Inserting into table with loop working till number of Rows.

    with open('food (1).csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            name = row['name']
            typ = row['typ']
            categorie = row['categorie']
            price = row['price']
            tree.insert('', 0, values=(name, typ, categorie, price))

    w2 = Label(
        f3,
        bg='light green',
        fg='black',
        width=50,
        text='When you are Ready PLease Press Place an Order ',
        font=('georgia', 10),
        )
    w2.pack()

    # -----------------------------Button----------------------------------

    btn_menu = Button(
        f3,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('georgia', 16, 'bold'),
        width=10,
        text='Place an Order',
        bg='green',
        command=lambda : order(),
        )
    btn_menu.pack()
    root.mainloop()


def order():
    """Important Function Implementation , which deals with the calculation of
    Bill based on User Input"""

    root = Tk()

    # ---------------Windows Dimensions----------------------------

    root.title('Order PLease!')
    root.geometry('1600x700+0+0')

    f1 = Frame(root, width=900, height=700, relief=SUNKEN)
    f1.pack(side=LEFT)

    f2 = Frame(root, width=400, height=700, relief=SUNKEN)
    f2.pack(side=RIGHT)

    f3 = Frame(root, width=400, height=700, relief=SUNKEN)
    f3.pack(side=BOTTOM)

    def calc_bill():
        """Getters , Setters Function's of Tkinter used to calculate the Cost(incl. Taxes) . """

        master = Tk()

        # ---------------Adjusted Windows Dimensions according to the need----------------------------

        width = 1000
        height = 500
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = screen_width / 2 - width / 2
        y = screen_height / 2 - height / 2
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        master.resizable(0, 0)

        Tops = Frame(master, bg='light green', width=5000, height=2500,
                     relief=SUNKEN)
        Tops.pack(side=TOP)

        f11 = Frame(master, width=900, height=700, relief=SUNKEN)
        f11.pack(side=LEFT)

        f22 = Frame(master, width=400, height=700, relief=SUNKEN)
        f22.pack(side=RIGHT)

        f33 = Frame(master, width=400, height=700, relief=SUNKEN)
        f33.pack(side=BOTTOM)

        title = Label(
            Tops,
            font=('georgia', 30, 'bold'),
            text='BILL',
            fg='black',
            bg='light green',
            bd=10,
            anchor='w',
            )
        title.grid(row=5, column=0)

        # Assigning the Local Variables the Values obtained from Global Variables "

        vburger = float(vu_burg.get())
        faburger = float(be_burg.get())
        cburger = float(cl_burg.get())
        chburger = float(ch_burg.get())
        fburger = float(f_burg.get())
        chiburger = float(chi_burg.get())
        mpizza = float(m_piz.get())
        hpizza = float(h_piz.get())
        mopizza = float(mo_piz.get())
        water1 = float(wa1.get())
        water2 = float(wa2.get())
        cola1 = float(co1.get())
        cola2 = float(co2.get())
        fanta1 = float(fa1.get())
        fanta2 = float(fa2.get())
        icet1 = float(ic1.get())
        icet2 = float(ic2.get())
        beer = float(be.get())
        i1 = float(ing1.get())
        i2 = float(ing2.get())
        i3 = float(ing3.get())
        i4 = float(ing4.get())
        i5 = float(ing5.get())
        i6 = float(ing6.get())

        vburgerp = vburger * 12
        faburgerp = faburger * 13
        cburgerp = cburger * 9
        chburgerp = chburger * 10
        fburgerp = fburger * 12
        chiburgerp = chiburger * 12
        mpizzap = mpizza * 9
        hpizzap = hpizza * 10
        mopizzap = mopizza * 10
        waterp1 = water1 * 2
        waterp2 = water2 * 3.5
        colap1 = cola1 * 3.5
        colap2 = cola2 * 2.5
        fantap1 = fanta1 * 3.5
        fantap2 = fanta2 * 2.5
        icetp1 = icet1 * 4
        icetp2 = icet2 * 4
        beerp = beer * 4
        ip1 = i1 * 1
        ip2 = i2 * 1
        ip3 = i3 * 1
        ip4 = i4 * 1
        ip5 = i5 * 1
        ip6 = i6 * 1

        # Declaring Variables to be used for calculation later in the funcction.

        cost = IntVar(master)
        Service_Charge = IntVar(master)
        Subtotal = IntVar(master)
        Total = IntVar(master)
        Tax = IntVar(master)

        # Everything will be calculated here

        dinnercost = (str('%.2f' % (vburgerp + faburgerp + cburgerp
                      + chburgerp + fburgerp + chiburgerp + mpizzap
                      + hpizzap + mopizzap + waterp1 + waterp2 + colap2
                      + colap1 + fantap2 + fantap1 + icetp2 + icetp1
                      + beerp + ip1 + ip2 + ip3 + ip4 + ip5 + ip6)),
                      '€')
        PayTax = (vburgerp + faburgerp + cburgerp + chburgerp
                  + fburgerp + chiburgerp + mpizzap + hpizzap
                  + mopizzap + waterp1 + waterp2 + colap2 + colap1
                  + fantap2 + fantap1 + icetp2 + icetp1 + beerp + ip2
                  + ip3 + ip4 + ip5 + ip6) * 0.19
        Totalcost = vburgerp + faburgerp + cburgerp + chburgerp \
            + fburgerp + chiburgerp + mpizzap + hpizzap + mopizzap \
            + waterp1 + waterp2 + colap2 + colap1 + fantap2 + fantap1 \
            + icetp2 + icetp1 + beerp + ip2 + ip3 + ip4 + ip5 + ip6
        Ser_Charge = (vburgerp + faburgerp + cburgerp + chburgerp
                      + fburgerp + chiburgerp + mpizzap + hpizzap
                      + mopizzap + waterp1 + waterp2 + colap2 + colap1
                      + fantap2 + fantap1 + icetp2 + icetp1 + beerp
                      + ip2 + ip3 + ip4 + ip5 + ip6) / 99
        Service = (str('%.2f' % Ser_Charge), '€')
        OverAllCost = (str(PayTax + Totalcost + Ser_Charge),
                       '€')
        PaidTax = (str('%.2f' % PayTax), '€')

        # Setting the calculated Variables to get the desired result displayed in the Entry Widgets

        Service_Charge.set(Service)
        cost.set(dinnercost)
        Tax.set(PaidTax)
        Subtotal.set(dinnercost)
        Total.set(OverAllCost)

        # Entry Widgets and Label Widgets to display the desire Results as a part of GUI.

        lblcost = Label(
            f11,
            font=('georgia', 16, 'bold'),
            text='Cost',
            fg='brown',
            bd=10,
            anchor='w',
            )
        lblcost.grid(row=10, column=0)
        txtcost = Entry(
            f11,
            font=('ariel', 16, 'bold'),
            textvariable=cost,
            bd=6,
            insertwidth=4,
            bg='white',
            justify='right',
            )
        txtcost.grid(row=10, column=1)

        lblService_Charge = Label(
            f11,
            font=('georgia', 16, 'bold'),
            text='Service Charge',
            fg='brown',
            bd=10,
            anchor='w',
            )
        lblService_Charge.grid(row=10, column=2)
        txtService_Charge = Entry(
            f11,
            font=('ariel', 16, 'bold'),
            textvariable=Service_Charge,
            bd=6,
            insertwidth=4,
            bg='white',
            justify='right',
            )
        txtService_Charge.grid(row=10, column=3)

        lblTax = Label(
            f11,
            font=('georgia', 16, 'bold'),
            text='Tax',
            fg='brown',
            bd=10,
            anchor='w',
            )
        lblTax.grid(row=13, column=0)
        txtTax = Entry(
            f11,
            font=('ariel', 16, 'bold'),
            textvariable=Tax,
            bd=6,
            insertwidth=4,
            bg='white',
            justify='right',
            )
        txtTax.grid(row=13, column=1)

        lblSubtotal = Label(
            f11,
            font=('georgia', 16, 'bold'),
            text='Subtotal',
            fg='brown',
            bd=10,
            anchor='w',
            )
        lblSubtotal.grid(row=13, column=2)
        txtSubtotal = Entry(
            f11,
            font=('ariel', 16, 'bold'),
            textvariable=Subtotal,
            bd=6,
            insertwidth=4,
            bg='white',
            justify='right',
            )
        txtSubtotal.grid(row=13, column=3)

        lblTotal = Label(
            f11,
            font=('georgia', 20, 'bold'),
            text='Total',
            fg='brown',
            bd=10,
            anchor='w',
            )
        lblTotal.grid(row=15, column=1)
        txtTotal = Entry(
            f11,
            font=('ariel', 16, 'bold'),
            textvariable=Total,
            bd=6,
            insertwidth=4,
            bg='white',
            justify='right',
            )
        txtTotal.grid(row=15, column=2)

        btn_cancel = Button(
            f11,
            padx=16,
            pady=8,
            bd=10,
            fg='white',
            font=('georgia', 16, 'bold'),
            width=10,
            text='Go Back',
            bg='maroon',
            command=master.destroy,
            )
        btn_cancel.grid(row=16, column=2)

        master.mainloop()

    # Global Variables being declared to assign the Values for calculation cost, taxes etc.

    vu_burg = IntVar(root)
    be_burg = IntVar(root)
    ch_burg = IntVar(root)
    f_burg = IntVar(root)
    cl_burg = IntVar(root)
    chi_burg = IntVar(root)
    m_piz = IntVar(root)
    h_piz = IntVar(root)
    mo_piz = IntVar(root)
    wa1 = IntVar(root)
    wa2 = IntVar(root)
    co1 = IntVar(root)
    co2 = IntVar(root)
    fa1 = IntVar(root)
    fa2 = IntVar(root)
    ic1 = IntVar(root)
    ic2 = IntVar(root)
    be = IntVar(root)
    ing1 = IntVar(root)
    ing2 = IntVar(root)
    ing3 = IntVar(root)
    ing4 = IntVar(root)
    ing5 = IntVar(root)
    ing6 = IntVar(root)

    # Representation of Food-Items with Entry and Label Widgets

    lbl1a = Label(
        f1,
        font=('georgia', 17, 'bold'),
        text="BURGER'S",
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl1a.grid(row=0, column=0)
    lbl1a = Label(
        f1,
        font=('ariel', 16, 'bold'),
        text='Quantity',
        fg='black',
        bd=10,
        anchor='w',
        )
    lbl1a.grid(row=1, column=1)

    lbl1 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='VUNKY-BURGER',
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl1.grid(row=2, column=0)
    txt1 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=vu_burg,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt1.grid(row=2, column=1)

    lbl2 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='FALAFEL-BURGER',
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl2.grid(row=3, column=0)
    txt2 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=be_burg,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt2.grid(row=3, column=1)

    lbl3 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='CLASSIC-BURGER',
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl3.grid(row=4, column=0)
    txt3 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=cl_burg,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt3.grid(row=4, column=1)

    lbl4 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='CHEESE-BURGER',
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl4.grid(row=5, column=0)
    txt4 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=ch_burg,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt4.grid(row=5, column=1)

    lbl5 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='FOREST-BURGER',
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl5.grid(row=6, column=0)
    txt5 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=f_burg,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt5.grid(row=6, column=1)

    lbl6 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='CHILLI-BURGER',
        fg='red',
        bd=10,
        anchor='w',
        )
    lbl6.grid(row=6, column=0)
    txt6 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=chi_burg,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt6.grid(row=6, column=1)

    lbl1a = Label(
        f1,
        font=('georgia', 17, 'bold'),
        text="PIZZA'S",
        fg='navy blue',
        bd=10,
        anchor='w',
        )
    lbl1a.grid(row=8, column=0)
    lbl1a = Label(
        f1,
        font=('ariel', 16, 'bold'),
        text='Quantity',
        fg='black',
        bd=10,
        anchor='w',
        )
    lbl1a.grid(row=9, column=1)

    lbl7 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='PIZZA-MARGARITA',
        fg='navy blue',
        bd=10,
        anchor='w',
        )
    lbl7.grid(row=10, column=0)
    txt7 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=m_piz,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt7.grid(row=10, column=1)

    lbl8 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='PIZZA-HAWAI',
        fg='navy blue',
        bd=10,
        anchor='w',
        )
    lbl8.grid(row=11, column=0)
    txt8 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=h_piz,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt8.grid(row=11, column=1)

    lbl8a = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='PIZZA-MOZZARELLA',
        fg='navy blue',
        bd=10,
        anchor='w',
        )
    lbl8a.grid(row=12, column=0)
    txt8a = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=mo_piz,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt8a.grid(row=12, column=1)

    lbl1a = Label(
        f1,
        font=('georgia', 17, 'bold'),
        text="DRINK'S",
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl1a.grid(row=0, column=2)
    lbl1a = Label(
        f1,
        font=('ariel', 16, 'bold'),
        text='Quantity',
        fg='black',
        bd=10,
        anchor='w',
        )
    lbl1a.grid(row=1, column=3)

    lbl9 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='WASSER(0.3)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl9.grid(row=2, column=2)
    txt9 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=wa1,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt9.grid(row=2, column=3)

    lbl10 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='WASSER(0.5)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl10.grid(row=3, column=2)
    txt10 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=wa2,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt10.grid(row=3, column=3)

    lbl11 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='COLA(0.4)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl11.grid(row=4, column=2)
    txt11 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=co1,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt11.grid(row=4, column=3)

    lbl12 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='FANTA(0.4)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl12.grid(row=5, column=2)
    txt12 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=fa1,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt12.grid(row=5, column=3)

    lbl13 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='COLA(0.2)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl13.grid(row=6, column=2)
    txt13 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=co2,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt13.grid(row=6, column=3)

    lbl14 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='FANTA(0.2)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl14.grid(row=7, column=2)
    txt14 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=fa2,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt14.grid(row=7, column=3)

    lbl15 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='ICE-TEE(Peach)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl15.grid(row=8, column=2)
    txt15 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=ic1,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt15.grid(row=8, column=3)

    lbl16 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='ICE-TEE(LEMON)',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl16.grid(row=9, column=2)
    txt16 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=ic2,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt16.grid(row=9, column=3)

    lbl17 = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='BEER',
        fg='purple',
        bd=10,
        anchor='w',
        )
    lbl17.grid(row=10, column=2)
    txt17 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=be,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt17.grid(row=10, column=3)

    lbl18a = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='AddOns - For Your Burger',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl18a.grid(row=0, column=7)
    lbl18a = Label(
        f1,
        font=('aria', 16, 'bold'),
        text='Quantity',
        fg='black',
        bd=10,
        anchor='w',
        )
    lbl18a.grid(row=1, column=7)

    lbl18 = Label(
        f1,
        font=('aria', 16, 'bold'),
        text='Extra Cheese',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl18.grid(row=2, column=6)
    txt18 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=ing1,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt18.grid(row=2, column=7)

    lbl19 = Label(
        f1,
        font=('aria', 16, 'bold'),
        text='Olives',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl19.grid(row=3, column=6)
    txt19 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=ing2,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt19.grid(row=3, column=7)

    lbl20 = Label(
        f1,
        font=('aria', 16, 'bold'),
        text='Extra Chicken ',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl20.grid(row=4, column=6)
    txt20 = Entry(
        f1,
        font=('ariel', 16, 'bold'),
        textvariable=ing3,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt20.grid(row=4, column=7)

    lbl20a = Label(
        f1,
        font=('georgia', 16, 'bold'),
        text='AddOns - For Your Pizza',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl20a.grid(row=6, column=7)
    lbl18a = Label(
        f1,
        font=('aria', 16, 'bold'),
        text='Quantity',
        fg='black',
        bd=10,
        anchor='w',
        )
    lbl18a.grid(row=7, column=7)

    lbl21 = Label(
        f1,
        font=('ariel', 16, 'bold'),
        text='Extra Cheese',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl21.grid(row=8, column=6)
    txt21 = Entry(
        f1,
        font=('oscar', 16, 'bold'),
        textvariable=ing4,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt21.grid(row=8, column=7)

    lbl22 = Label(
        f1,
        font=('ariel', 16, 'bold'),
        text='Garlic',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl22.grid(row=9, column=6)
    txt22 = Entry(
        f1,
        font=('oscar', 16, 'bold'),
        textvariable=ing5,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt22.grid(row=9, column=7)

    lbl23 = Label(
        f1,
        font=('ariel', 16, 'bold'),
        text='Extra Pepper',
        fg='green',
        bd=10,
        anchor='w',
        )
    lbl23.grid(row=10, column=6)
    txt23 = Entry(
        f1,
        font=('oscar', 16, 'bold'),
        textvariable=ing6,
        bd=6,
        insertwidth=4,
        bg='white',
        justify='right',
        )
    txt23.grid(row=10, column=7)

    def qexit():
        """To Destroy the Functionality"""

        root.destroy()

    def reset():
        """Function used to reset the Values , to obtain the result from the beginning."""

        vu_burg.set('0')
        be_burg.set('0')
        ch_burg.set('0')
        f_burg.set('0')
        cl_burg.set('0')
        chi_burg.set('0')
        m_piz.set('0')
        h_piz.set('0')
        mo_piz.set('0')
        wa1.set('0')
        wa2.set('0')
        co1.set('0')
        co2.set('0')
        fa1.set('0')
        fa2.set('0')
        ic1.set('0')
        ic2.set('0')
        be.set('0')
        ing1.set('0')
        ing2.set('0')
        ing3.set('0')
        ing4.set('0')
        ing5.set('0')
        ing6.set('0')

    # -----------------------------Buttons------------------------------------------

    btnPay = Button(
        f1,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('ariel', 16, 'bold'),
        width=10,
        text='PAY',
        bg='dark orange',
        command=calc_bill,
        )
    btnPay.grid(row=13, column=7)

    btnreset = Button(
        f1,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('ariel', 16, 'bold'),
        width=10,
        text='RESET',
        bg='dark gray',
        command=reset,
        )
    btnreset.grid(row=13, column=3)

    btnexit = Button(
        f1,
        padx=16,
        pady=8,
        bd=10,
        fg='white',
        font=('ariel', 16, 'bold'),
        width=10,
        text='EXIT',
        bg='maroon',
        command=qexit,
        )
    btnexit.grid(row=13, column=1)

    root.mainloop()


home()