msg1="WeLcOME"
msg2="GueSTs"
msg3=""
for i in range(0,len(msg2)+1):
    if msg1[i]>="A" and msg1[i]<="M":
        msg3=msg3+msg1[i]
    elif msg1[i]>='N' and msg1[i]<='Z':
        msg3=msg3+msg2[i]
    else:
        msg3=msg3+"*"
print(msg3)
