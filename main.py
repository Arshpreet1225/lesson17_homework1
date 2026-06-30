bill_amount=int(input("enter the amount of total bill:"))
paid_amount=int(input("enter the amount you have paid:"))
while paid_amount>0:
    if paid_amount<=0:
        break
    elif paid_amount<=bill_amount:
        print("you have a due")
        continue
    elif paid_amount==bill_amount:
        print("you have paid the full amount")
        pass
    else:
        print("invalid")
