import pywhatkit as kit

phonenumber = input("enter phone number with add area code\n")
hours = input("Enter the hours you want to send the message \n")
minutes = input("Enter the minutes you want to send the message \n")
print(hours + ":" + minutes)
print("enter your messege to stop press ctrl d")
contents = []
messege = ""
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
for i in range(len(contents)):
    messege += contents[i] + "\n"
print(messege)
try:
    kit.sendwhatmsg(str(phonenumber), messege, int(hours), int(minutes), 20)
    print("message sent")
except:
    print("some error")
