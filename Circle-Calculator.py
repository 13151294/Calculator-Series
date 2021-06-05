#Made by Ace Fhid
#Python 3.9.5
"""
This Python code is use to calculate circle thing
"""
import math
def num_text(num1,num2):
    case_ans = {
        1:"Radius",
        2:"Diameter",
        3:"Circle Area",
        4:"Circle Circumference",
        5:"Chord",
        6:"Arc",
        7:"Sector",
        8:"Segment",
    }
    case_in = {
        1:"Radius",
        2:"Diameter",
        3:"Circle Area",
        4:"Circle Circumference",
        5:"Arc",
        6:"Sector",
        7:"Chord",
    }
    return case_ans.get(num1,"Error"), case_in.get(num2,"Error")
def input_choice(ans_Index):
    case = {
        1:"Diameter Length = 2\nCircle Area = 3\nCircle Circumference = 4\nArc Length = 5\nSector Area = 6\nChord Length = 7",
        2:"Radius Length = 1\nCircle Area = 3\nCircle Circumference = 4\nArc Length = 5\nSector Area = 6\nChord Length = 7",
        3:"Radius Length = 1\nDiameter Length = 2\nCircle Circumference = 4\nArc Length = 5\nSector Area = 6\nChord Length = 7",
        4:"Radius Length = 1\nDiameter Length = 2\nCircle Area = 3\nArc Length = 5\nSector Area = 6\nChord Length = 7",
        5:"Radius Length = 1\nDiameter Length = 2\nCircle Area = 3\nCircle Circumference = 4\nArc Length = 5\nSector Area = 6",
        6:"Radius Length = 1\nDiameter Length = 2\nCircle Area = 3\nCircle Circumference = 4\nSector Area = 6\nChord Length = 7",
        7:"Radius Length = 1\nDiameter Length = 2\nCircle Area = 3\nCircle Circumference = 4\nArc Length = 5\nChord Length = 7",
        8:"Radius Length = 1\nDiameter Length = 2\nCircle Area = 3\nCircle Circumference = 4\nArc Length = 5\nSector Area = 6\nChord Length = 7"
    }
    return case.get(ans_Index, "ERROR")
def Input_():
    print("\033[38;2;255;255;0m-------π Value-------\033[38;2;255;255;255m")
    pi = float(input("Enter π(Pi) Value : "))
    #pi = 22/7
    print("\033[38;2;255;255;0m-------Answer Type-------\033[38;2;255;255;255m")
    print("Radius Length = 1\nDiameter Length = 2\nCircle Area = 3\nCircle Circumference = 4\nChord Length = 5\nArc Length = 6\nSector Area = 7\nSegment Area = 8")
    ans_type = int(input("Enter Answer Type : "))
    print("\033[38;2;255;255;0m-------Answer Type End-------\033[38;2;255;255;255m")
    if ans_type > 8 or ans_type < 0:
        print("\033[38;2;255;66;66m",end="")
        if ans_type > 8:
            raise ValueError("\033[38;2;255;66;66m<!-ERROR ANSWER TYPE-!>\033[38;2;255;255;0m \"{}\" is More than 8\033[38;2;255;255;255m".format(ans_type))
        elif ans_type < 0:
            raise ValueError("\033[38;2;255;66;66m<!-ERROR ANSWER TYPE-!>\033[38;2;255;255;0m \"{}\" is Less than 0\033[38;2;255;255;255m".format(ans_type))

    print("\033[38;2;255;255;0m-------Input Type-------\033[38;2;255;255;255m")
    print(input_choice(ans_type))
    input_type = int(input("Enter Input Type : "))
    print("\033[38;2;255;255;0m-------Input Type End-------\033[38;2;255;255;255m")
    ans_type_word, In_type_word = num_text(ans_type,input_type)
    if ans_type > 8 or ans_type < 0:
        print("\033[38;2;255;66;66m",end="")
        if ans_type > 8:
            raise ValueError("\033[38;2;255;66;66m<!-ERROR ANSWER TYPE-!>\033[38;2;255;255;0m \"{}\" is More than 7\\033[38;2;255;255;255m".format(ans_type))
        elif ans_type < 0:
            raise ValueError("\033[38;2;255;66;66m<!-ERROR ANSWER TYPE-!>\033[38;2;255;255;0m \"{}\" is Less than 0\033[38;2;255;255;255m".format(ans_type))
    In_Angle = 360
    Ans_Angle = 360
    if ans_type > 4:
        Ans_Angle = float(input("Enter {} Angle : ".format(ans_type_word)))
    if input_type > 4:
        In_Angle = float(input("Enter {} Angle : ".format(In_type_word)))
    if (1 <= input_type <= 2) or (4 <= input_type <= 5) or input_type == 7:
        unit = "Length"
    else:
        unit = "Area"
    Length_Area = float(input("Enter {} {} : ".format(In_type_word, unit)))
    return ans_type, ans_type_word, input_type, In_type_word, Length_Area, Ans_Angle, In_Angle, pi
def Input_to_Radius(Input_type, ValueA, angle, pi):
    formula = {
        1:ValueA,
        2:ValueA/2,
        3:math.sqrt(ValueA/pi),
        4:ValueA/(2*pi),
        5:(180*ValueA)/(angle*pi),
        6:math.sqrt((360*ValueA)/(angle*pi)),
        7:ValueA/(2*math.sin(math.radians(angle/2)))
    }
    return formula.get(Input_type,"none")
def Calculator(Answer_type, radius, angle, pi):
    r = radius
    formula = {
        1:r,
        2:r*2,
        3:pi*(r**2),
        4:2*pi*r,
        5:2*r*math.sin(math.radians(angle/2)),
        6:(pi*r*angle)/180,
        7:(pi*(r**2)*angle)/360,
        8:(((angle*pi)/360)-(math.sin(math.radians(angle))/2))*(r**2)
    }
    return formula.get(Answer_type,IndexError)
def Output(ans_type, ans_word, input_type, Input_word, Length_Area, ans_angle, in_angle, pi):
    Radius = Input_to_Radius(input_type, Length_Area, in_angle, pi)
    Result = Calculator(ans_type, Radius, ans_angle, pi)
    if (1 <= ans_type <= 2) or (4 <= ans_type <= 6):
        name = "Length"
    else:
        name = "Area"
    if (1 <= input_type <= 2) or (4 <= input_type <= 5) or input_type == 7:
        unit = "Length"
    else:
        unit = "Area"
    print("\033[38;2;0;255;0m〜〜〜〜〜〜〜〜Answer〜〜〜〜〜〜〜〜\033[38;2;255;255;255m")
    print("{} {} is : {}".format(ans_word, name, Result))
    print("{} {} is : {}".format(Input_word, unit, Length_Area))
    print("\033[38;2;0;255;0m〜〜〜〜〜〜〜〜Answer〜〜〜〜〜〜〜〜\033[38;2;255;255;255m")
    repeat()
def repeat():
    try:
        repeatOption = int(input("Wanna Calculate Again?(1/0) : "))
    except:
        raise TypeError("Repeat Option is equal to 1 or 0")
    if repeatOption > 0:
        ans_Int, ans_word, input_Int, Input_word, Length_Area, AnsAngle, InputAngle, pi = Input_()
        Output(ans_Int, ans_word, input_Int, Input_word, Length_Area, AnsAngle, InputAngle, pi)
    else:
        print("\033[38;2;255;120;255mGood Bye <3\033[38;2;255;255;255m")
def Start():
    ans_Int, ans_word, input_Int, Input_word, Length_Area, AnsAngle, InputAngle, pi = Input_()
    Output(ans_Int, ans_word, input_Int, Input_word, Length_Area, AnsAngle, InputAngle, pi)
Start()