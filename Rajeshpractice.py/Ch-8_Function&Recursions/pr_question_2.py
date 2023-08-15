# write a python program using function to convert celcius to fahrenheit.
# °F = (°C x 1.8) + 32   or   (cel*(9/5)) +32

def farh(cel):
    return (cel*1.8) +32

cel = 0
f = farh(cel)
print("fahrenheit Temperature of "+ str(cel)+ " is: "+ str(f))