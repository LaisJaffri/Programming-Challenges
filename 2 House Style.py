Tuple = (1,2,3)
Set = {6,7,8}
Dict = {"Name":"Lais"}
print(f"Tuple's original memory address {id(Tuple)}")
Tuple = (99,19,29)
print(f"After changing the tuple it's memory address is {id(Tuple)}, thus it is immutable")
print(f"Set's original memory address {id(Set)}")
Set.add(9)
print(f"After changing the set it's memory address is {id(Set)} thus it is mutable")
print(f"Dict's original memory address {id(Dict)}")
Dict["Age"] = 16
print(f"After changing the dict it's memory address is {id(Dict)} thus it is mutable")