name = input("Enter name :")
status = "Pass"

urdu_marks = int(input("Enter urdu marks :"))
if (urdu_marks < 40):
    print("Fail in urdu.")
    status = "Fail"

eng_marks = int(input("Enter engl marks :"))
if (eng_marks < 40):
    print("Fail in english.")
    status = "Fail"

math_marks = int(input("Enter math marks :"))
if (math_marks < 40):
    print("Fail in math.")
    status = "Fail"

isl_marks = int(input("Enter isl marks :"))
if (isl_marks < 40):
    print("Fail in islamiyat.")
    status = "Fail"

phy_marks = int(input("Enter phy marks :"))
if (phy_marks < 40):
    print("Fail in physics.")
    status = "Fail"

chem_marks = int(input("Enter chem marks :"))
if (chem_marks < 40):
    print("Fail in chemistry.")
    status = "Fail"

bio_marks = int(input("Enter bio marks :"))
if (bio_marks < 40):
    print("Fail in biology.")
    status = "Fail"

print(f"Name : {name}")
print("Total marks : 700")
obtained_marks = urdu_marks + eng_marks + math_marks + isl_marks + phy_marks + chem_marks + bio_marks
print(f"Obtained marks : {obtained_marks}")

percentage = (obtained_marks/700)*100
print(f"Percentage : {percentage:.2f}%")



if (percentage >= 90):
    Grade = "A"
    status = "Distinction"

elif (percentage >= 80):
    Grade = "B"
    if (percentage > 85):
        status = "Distinction"

elif (percentage >= 70):
    Grade = "C"

elif (percentage >= 60):
    Grade = "D"

elif (percentage >= 50):
    Grade = "E"

else:
    Grade = "F"


print(f"Grade : {Grade}")
print(f"Status : {status}")


