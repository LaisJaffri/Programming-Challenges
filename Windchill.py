"""
display = {}
temps = [10,0,-10]
speed = [15,25,35]
for i in range(3):
    display[f"row{i}"] = {
        "temp":temps[i],
        "speed":speed[i]
    }
    windchill = 35.74 +0.6215 * temps[i] - 35.75 * speed[i]**0.16 + 0.4275 * temps[i] * speed[i]**0.16
    print(f"Temperature of {display[f"row{i}"]["temp"]} and speed of {display[f"row{i}"]["temp"]} gives windchill of: {windchill}")
"""
temps = [10,0,-10]
speed = [15,25,35]
windchill = [0,0,0]
for i in range(3):
    windchill[i] = 35.74 +0.6215 * temps[i] - 35.75 * speed[i]**0.16 + 0.4275 * temps[i] * speed[i]**0.16
    print(f"Temperature of {temps[i]} and speed of {speed[i]} gives windchill of: {windchill[i]}")
temp = float(input("Temperature: "))
speed = float(input("Speed: "))
windchill = 35.74 +0.6215 * temp - 35.75 * speed**0.16 + 0.4275 * temp * speed**0.16
print(f"Winchill: {windchill}")