"""
richter_dict = {
    "richter": 0, 
    "Joules": 0,

}
richter_value = 1
richter_dict["richter"] = 1
richter_dict["Joules"]= 10**((1.5*richter_value)+4.8)
richter_dict["TNT"] = richter_dict["Joules"]/(4.184*(10**(9)))
print(richter_dict["richter"], richter_dict["Joules"], richter_dict["TNT"])
"""
richter_dict = {}
richter =float(input("Enter richter value: "))
count = 1
while richter != "stop":
    richter_dict[f"richter{count}"]= {
        "richter":richter,
        "joules":0,
        "TNT": 0 
    }
    richter_dict[f"richter{count}"]["joules"]= 10**((1.5*richter)+4.8)
    richter_dict[f"richter{count}"]["TNT"] = richter_dict[f"richter{count}"]["joules"]/(4.184*(10**(9)))
    count+=1
    richter =input("Enter richter value or stop to stop: ")
    if richter!="stop":
        richter = float(richter)
print(f"{"Richter": <10} {"Joules": <25} {"TNT": <25}")
for i in range(1,count):
    print(f"{richter_dict[f"richter{i}"]["richter"]: <10} {richter_dict[f"richter{i}"]["joules"]: <25} {richter_dict[f"richter{i}"]["TNT"]: <25}")