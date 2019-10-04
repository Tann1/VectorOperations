from tkinter import *
from tkinter import ttk
from vectors import Vector

#repeated info in other paramters
backGround = '#778b8b'

#button clicked functions here
def populateCompents(arg1 = []): #arg1 = components of 1st vector and arg2 = components of the 2nd
    try:
        for component in arg1:
            arg1.append(float(component.get()))
    except ValueError:
        pass
    return arg1

def addVector():
    components1 = []
    components2 = []
    try:
        for component in vector1:
            components1.append(float(component.get()))
        for component in vector2:
            components2.append(float(component.get()))
    except ValueError:
        pass
    v1 = Vector.from_list(components1)
    v2 = Vector.from_list(components2)
    sum = v1.sum(v2)
    answer.set(sum)
  

def dotProduct():
    components1 = []
    components2 = []
    try:
        for component in vector1:
            components1.append(float(component.get()))
        for component in vector2:
            components2.append(float(component.get()))
    except ValueError:
        pass
    v1 = Vector.from_list(components1)
    v2 = Vector.from_list(components2)
    sum = v1.dot(v2)
    answer.set(sum)

def crossProduct():
    components1 = []
    components2 = []
    try:
        for component in vector1:
            components1.append(float(component.get()))
        for component in vector2:
            components2.append(float(component.get()))
    except ValueError:
        pass
    v1 = Vector.from_list(components1)
    v2 = Vector.from_list(components2)
    solution = v1.cross(v2)
    answer.set(solution)

def subtractVector():
    components1 = []
    components2 = []
    try:
        for component in vector1:
            components1.append(float(component.get()))
        for component in vector2:
            components2.append(float(component.get()))
    except ValueError:
        pass
    v1 = Vector.from_list(components1)
    v2 = Vector.from_list(components2)
    solution = v1.sum(v2.multiply(-1))
    answer.set(solution)



root = Tk()
#root.configure(background="#778B8B")
root.title('Vector Calculator')
root.configure(background=backGround)

answer = StringVar()
#create Labels
xCompLabel = Label(root,text='x-component', bg=backGround, fg='white')
xCompLabel.grid(row=1, column=2, sticky=W)
yCompLabel = Label(root,text='y-component', bg=backGround, fg='white')
yCompLabel.grid(row=1, column=3, sticky=W)
zCompLabel = Label(root,text='z-component', bg=backGround, fg='white')
zCompLabel.grid(row=1, column=4, sticky=W)
vector1Label = Label(root,text='Vector 1: ', bg=backGround, fg='white')
vector1Label.grid(row=2, column=1, sticky=W)
Vector2Label = Label(root, text='Vector 2: ', bg=backGround, fg='white')
Vector2Label.grid(row=3, column=1, sticky=W)
SolutionLabel = Label(root, text='Solution: ', bg=backGround, fg='white')
SolutionLabel.grid(row=5, column=1, sticky=W)
AnswerLabel = Label(root, textvariable=answer, bg=backGround, fg='white')
AnswerLabel.grid(row=5, column=2, sticky=W, columnspan=2)

#create Entry Boxes for the xyz-components
vector1 = []
vector2 = []

for i in range(0,3):
    vector1Input = StringVar()
    vector2Input = StringVar()
    vector1.append(vector1Input)
    vector2.append(vector2Input)
    componentEntry1 = Entry(root, width=5, bg=backGround, fg='white', textvariable=vector1[i])
    componentEntry1.grid(row=2,column=2+i)
    componentEntry2 = Entry(root, width=5, bg=backGround, fg='white', textvariable=vector2[i])
    componentEntry2.grid(row=3,column=2+i)


#creating buttons
addVectorButton = Button(root, text='Add Vectors', bg=backGround, command=addVector)
addVectorButton.grid(row=4,column=1, sticky=W)
DotProductButton = Button(root, text='Dot Product', bg=backGround, command=dotProduct)
DotProductButton.grid(row=4, column=2, sticky=W, ipadx=5)
CrossProductButton = Button(root, text='Cross Product', bg=backGround, command=crossProduct)
CrossProductButton.grid(row=4, column=3, sticky=W, ipadx=5)
subtractVectorButton = Button(root, text='Subtract Vectors', bg=backGround, command=subtractVector)
subtractVectorButton.grid(row=4, column=4, sticky=W, ipadx=5)



root.mainloop()