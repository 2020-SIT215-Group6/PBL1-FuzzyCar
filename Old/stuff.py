def zmf(x, a, b):
    if x <= a:
        return 1
    elif a <= x and x <= ((a+b)/2):
        return 1 - 2*((x-a)/(b-a))**2
    elif ((a+b)/2) <= x and x <= b:
        return 2*((x-b)/(b-a))**2
    elif x >= b:
        return 0
    else:
        raise Exception()
        
def smf(x, a, b):
    if x <= a:
        return 0
    elif a <= x and x <= ((a+b)/2):
        return 2*((x-a)/(b-a))**2
    elif ((a+b)/2) <= x and x <= b:
        return 1 - 2*((x-b)/(b-a))**2
    elif x >= b:
        return 1
    else:
        raise Exception()
        
def trimf(x, a, b, c):
    if x <= a:
        return 0
    elif a <= x and x <= b:
        return ((x-a)/(b-a))
    elif b <= x <= c:
        return ((c-x)/(c-b))
    elif c <= x:
        return 0
    else:
        raise Exception()
        
def Slow(x):
	return trimf(x, 20, 35.01, 50.01)
	
def Medium(x):
	return trimf(x, 40, 50, 60)
	
def Close(x):
	return trimf(x, 5, 25, 45)
	
def Near(x):
	return trimf(x, 30, 45, 60)
	
def Wet(x):
	return smf(x, 0, 10)
	
def Dry(x):
	return zmf(x, 0, 10)

print("Slow: ", end="")
slow = Slow(42)
print(slow)
print("Medium: ", end="")
medium = Medium(42)
print(medium)
print("Near: ", end="")
near = Near(33)
print(near)
print("Close: ", end="")
close = Close(33)
print(close)
print("Wet: ", end="")
wet = Wet(7)
print(wet)
print("Dry: ", end="")
dry = Dry(7)
print(dry)

print("Rule 7: ", end="")
print(min(slow, close, dry))
print("Rule 8: ", end="")
print(min(slow, near, dry))
print("Rule 12: ", end="")
print(min(medium, close, dry))
print("Rule 13: ", end="")
print(min(medium, near, dry))
print("Rule 32: ", end="")
print(min(medium, near, wet))