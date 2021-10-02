from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Bitmap and images test")
root.iconbitmap('C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/dinal_deal.ico')

my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/imagens/me1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/imagens/me2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/imagens/me3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/imagens/me4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/simao/OneDrive/Ambiente de Trabalho/Projects/Python/imagens/me5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    my_label.grid(row=0, column=0, columnspan=3)

    button_forward=Button(root, text=">>", command=lambda:forward(image_number+1))
    button_forward.grid(row=1, column=2)
    button_back=Button(root, text="<<",command=lambda:backward(image_number-1))
    button_back.grid(row=1, column=0)

    if image_number==4:
        button_forward=Button(root, text=">>",state=DISABLED)

def backward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number])
    my_label.grid(row=0, column=0, columnspan=3)

    button_forward=Button(root, text=">>", command=lambda:forward(image_number+1))
    button_forward.grid(row=1, column=2)




button_back=Button(root, text="<<", command=backward, state=DISABLED)
button_exit=Button(root, text="Exit Program", command=root.quit)
button_forward=Button(root, text=">>", command=lambda:forward(1))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()