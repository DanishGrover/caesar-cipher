
from tkinter import *
def circle(l,n):
    if n < (len(l) - 1):
        return(l[n])
    else:
        return(l[n % (len(l))])

def my_formatting(string):
    for i in string:                                     
        if i in ".,1234567890?!;:_;-/()[]{}+-*\"'":
            string = string.replace(i,'')               
    string = string.lower()
    return(string)

def encode(string,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    string = my_formatting(string)
    for i in string:
        if i == " ":
            new_string += " "
        else:
            position = alphabet.index(i)
        new_string += circle(alphabet,position + key)
    return(new_string)

def decode(string,key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    string = my_formatting(string)
    for i in string:
        if i == " ":
            new_string += " "
        else:
            position = alphabet.index(i)
        new_string += circle(alphabet,position - key)
    return(new_string)


def brute_force_decode(string):
    new_string = ""
    for key in range(1,26):
        new_string += decode(string,key)
        new_string += '-'
    return(new_string)


def GUI():
    

    master = Tk()

    master.wm_title("Caesar cipher")

    key_label = Label(master, text="Key")
    key_label.pack()

    key_slider = Scale(master, from_=1, to=25, orient=HORIZONTAL,length=300)
    key_slider.pack()

    text_label = Label(master, text="Enter your text down here")
    text_label.pack()

    text_field = Text(master, height=5, width=30)
    text_field.pack()

    result_field = Text(master,height = 10,width = 40)

    def allow_to_paste(string):
        master.clipboard_clear()
        master.clipboard_append(string)

    def encode_and_show():
        temp1 = encode(text_field.get("1.0","end-1c"),key_slider.get())
        set_result_field(temp1)

    def set_result_field(inp_string):
        result_field.delete(1.0,END)
        result_field.insert(END,inp_string)

    b = Button(master, text="Encode", command=encode_and_show)
    b.pack()
   
    def decode_and_show():
        temp3 = decode(text_field.get("1.0","end-1c"),key_slider.get())
        set_result_field(temp3)
        allow_to_paste(temp3)

    b = Button(master, text="Decode", command=decode_and_show)
    b.pack()

    def brute_force_decode_and_show():
        temp4= brute_force_decode(text_field.get("1.0","end-1c"))
        set_result_field(temp4)
        allow_to_paste(temp4)

    b = Button(master, text="Brute force decode", command=brute_force_decode_and_show)
    b.pack()

    
    result_field.pack()

    mainloop()

if __name__ == "__main__":
    GUI()
