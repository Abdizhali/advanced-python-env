ticket = input("Enter a 6-digit ticket number: ")

if len(ticket) != 6 or not ticket.isdigit():
    print("Error: Enter exactly 6 digits")
else:
    sum_first = sum(int(digit) for digit in ticket[:3])
    sum_last = sum(int(digit) for digit in ticket[3:])
    
    print("YES" if sum_first == sum_last else "NO")
