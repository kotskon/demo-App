import tkinter as tk

HEIGHT = 300
WIDTH = 400 


def my_func(a,b):
    # print("the two values are {} {} ".format(a,b))
    
    N=int(b)-int(a)+1
    m=N//2

    if ((N % 2)==0): 
        # (N mod 2) = 0.
       
        A = int(a)+m-1
        list1 = []
        list2 = []
    
        if ((m % 2)==0):
            for i in range(m//2):
                list1.append(A-2*i)
                list1.append(A+2*i+1)
                list2.append(A+2+2*i)
                list2.append(A-1-2*i)
        else:
            for i in range(m//2):
                list1.append(A-2*i)
                list1.append(A+2*i+1)
                list2.append(A+2+2*i)
                list2.append(A-1-2*i)
            list1.append(int(a))
            list1.append(int(b))
    
        s1 = ','.join(str(x) for x in list1)
        s2 = ','.join(str(x) for x in list2)
        # print(s1)
        # print(s2)
    
    else:
        # (N mod 2) = 1.
        
        A = int(a)+m
        list1 = []
        list2 = []
            
        if ((m % 2)==0):    
            for i in range(m//2):
                list1.append(A-2*i)
                list1.append(A+2*i+1)
                list2.append(A+2+2*i)
                list2.append(A-1-2*i)
            list1.append(int(a))
        else:
            for i in range(m//2):
                list1.append(A-2*i)
                list1.append(A+2*i+1)
                list2.append(A+2+2*i)
                list2.append(A-1-2*i)
            list1.append(int(a)+1)
            list1.append(int(b)-1)
            list2.append(int(a))    
        
        s1 = ','.join(str(x) for x in list1)
        s2 = ','.join(str(x) for x in list2)
        # print(s1)
        # print(s2)

    # First delete current outputs.
    out1.delete(1.0, tk.END)
    out2.delete(1.0, tk.END)

    # Print to outputs.
    out1.insert(tk.END, s1)
    out2.insert(tk.END, s2) 



# Create the main window object.
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

 

frame = tk.Frame(root ,bg='#9EA4CE')
frame.place(relx=.01, rely=.01,relwidth=.98, relheight=.98)

# Basic Compute Button.
button = tk.Button(frame, text='Compute', bg='gray', command=lambda: my_func(entry1.get(),entry2.get()))
button.place(relx=.25, rely=.3, relwidth=.5, relheight=.1)

# Labels Up.
label1 =tk.Label(frame, text='No. of first page', bg='white')
label1.place(relx=.05, rely=.05, relwidth=.4, relheight=.08)

label2 =tk.Label(frame, text='No. of last page', bg='white')
label2.place(relx=.05, rely=.13, relwidth=.4, relheight=.08)

# Entries
entry1 = tk.Entry(frame, font=40)
entry1.place(relx=.45, rely=.05, relwidth=.1, relheight=.08)

entry2 = tk.Entry(frame, font=40)
entry2.place(relx=.45, rely=.13, relwidth=.1, relheight=.08)

#Labels Down.
label3 =tk.Label(frame, text='Pages for printing 1st:', bg='gray')
label3.place(relx=.5, rely=.5, relwidth=.4, relheight=.08, anchor='n')

label4 =tk.Label(frame, text='No. of last page last:', bg='gray')
label4.place(relx=.5, rely=.7, relwidth=.4, relheight=.08, anchor='n')

# Labels  for output.
out1 =tk.Text(frame,  bg='white')
out1.place(relx=.5, rely=.6, relwidth=.9, relheight=.08, anchor='n')

out2 =tk.Text(frame,  bg='white')
out2.place(relx=.5, rely=.8, relwidth=.9, relheight=.08, anchor='n')



root.mainloop()