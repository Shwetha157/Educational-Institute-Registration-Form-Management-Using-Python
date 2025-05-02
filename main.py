from tkinter import *
window = Tk()
window.title("Simple App")

def getdata():
    print("Besant Technologies:", ebesant.get())
    print("Enquiry Form:", eenquiry.get())
    print("Date:", eDate.get())
    print("Name:", eName.get())
    print("Mobile No:", eMobileno.get())
    print("Alternate No:", eAlternateno.get())
    print("Email ID:", eEmailid.get())
    print("Address:", eAddress.get())
    print("Course Interested:", eCourse.get())
    print("Batch Preference:", eBatch.get())
    print("How You Came to Know Us:", eHowknown.get())
    print("Experience Level:", eExperience.get())
    print("Contact Person from Besant:", eContact.get())
    print("Counselor:", eCounselor.get())
    print("Fees:", eFees.get())
    print("Comment:", eComment.get())

Label(window, text="Besant Technologies", font=("Arial", 14, "bold")).grid(row=0, column=1, pady=5)
Label(window, text="Enquiry Form", font=("Arial", 12, "bold")).grid(row=1, column=1, pady=5)

fields = [
    ("Date:", 2), ("Name:", 3), ("Mobile No:", 4), ("Alternate No:", 5),
    ("Email ID:", 6), ("Address:", 7), ("Course Interested:", 8),
    ("Batch Preference:", 9), ("How You Came to Know Us:", 10),
    ("Experience Level:", 11), ("Contact Person from Besant:", 12),
    ("Counselor:", 13), ("Fees:", 14), ("Comment:", 15)
]

entries = {}

for text, row in fields:
    Label(window, text=text, anchor="w").grid(row=row, column=0, padx=10, pady=2, sticky="w")
    entry = Entry(window, width=30)
    entry.grid(row=row, column=1, padx=10, pady=2)
    entries[text] = entry  

varReg = IntVar()
varEnqui = IntVar()

def clicked(value):
    print("Checkbox value:", value)

Checkbutton(window, text="Registration", variable=varReg,  
            command=lambda: clicked(varReg.get())).grid(row=16, column=1, sticky=W, padx=10)

Checkbutton(window, text="Enquiry", variable=varEnqui,  
            command=lambda: clicked(varEnqui.get())).grid(row=16, column=2, sticky=W)

Button(window, text="Submit", bg="green", command=getdata).grid(row=17, column=1, pady=10)
Button(window, text="Cancel", bg="red", command=window.quit).grid(row=17, column=2, pady=10)

window.mainloop()
