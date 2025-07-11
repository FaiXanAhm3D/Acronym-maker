total_bill_amount = int(input("Enter the total bill amount : "))
if total_bill_amount>=20000:
    discount=(15/100)*total_bill_amount
    net=total_bill_amount-discount
    print("Discount :",discount)
    print("Net payable amount :",net)
elif total_bill_amount>=15000 and total_bill_amount<20000:
    discount=(10/100)*total_bill_amount
    net=total_bill_amount-discount
    print("Discount :",discount)
    print("Net payable amount :",net)
elif total_bill_amount>=10000 and total_bill_amount<15000:
    discount=(5/100)*total_bill_amount
    net=total_bill_amount-discount
    print("Discount :",discount)
    print("Net payable amount :",net)
else:
    print("Discount : 0")
    print("Net payable amount :",total_bill_amount)
