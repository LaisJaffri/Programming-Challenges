from dataclasses import dataclass
@dataclass
class Student:
    name:str
    year_group: int
    predicted_grade: str
kai = Student("Kai",12,"A")
mai = Student("Mai",13,"C")
james = Student("James",12,"A*")
flavour = Student("Flavour",12,"D")
list = [kai,mai,james,flavour]
len_list = len(list)
for i,namecheck in enumerate(list,1):
    if namecheck.predicted_grade == "A" or namecheck.predicted_grade == "A*":
        print(f"{i} {namecheck.name} (Year {namecheck.year_group}) - {namecheck.predicted_grade}")

