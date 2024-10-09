# Tanu and Head-bob

def determine_nationality(gestures):

    if 'I' in gestures:
        return "INDIAN"
    
    elif 'Y' in gestures:
        return "NOT INDIAN"
    
    else:
        return "NOT SURE"
    
T = int(input())

for _ in range(T):
    N = int(input())
    gestures = input()

print(determine_nationality(gestures))