import re
data = raw_input("Enter the text to match the pattern\n")
match_a = re.match('^harini+[a-zA-Z0-9_.+-]*@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9-.]+$',data)
#matches with an email that starts with harini
if match_a:
    print(data + " matched with pattern")
    match_b = re.match('^harini?!pradeep+[a-zA-Z0-9_.+-]*@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9-.]+$',data)
    if match_b:
        print(data + " email starts with harini and does not followed by pradeep")
    else:
        print(data + "email starts with harini but followed by pradeep")
else:
    print(data + "does not matched with pattern")



#$ python regex.py 
#Enter the text to match the pattern
#harini12@a.c
#harini12@a.c matched with pattern
#harini12@a.cemail starts with harini but followed by pradeep
#harini@harini-HP-ProBook-440-G2:~/Documents/Exercises$ python regex.py 
#Enter the text to match the pattern
#ha@qwqe.cadc
#ha@qwqe.cadcdoes not matched with pattern
#harini@harini-HP-ProBook-440-G2:~/Documents/Exercises$ python regex.py 
#Enter the text to match the pattern
#aSCZX@1qd.sdcw
#aSCZX@1qd.sdcwdoes not matched with pattern
#harini@harini-HP-ProBook-440-G2:~/Documents/Exercises$ python regex.py 
#Enter the text to match the pattern
#harinipradeep1312@qw.cdv
#harinipradeep1312@qw.cdv matched with pattern
#harinipradeep1312@qw.cdvemail starts with harini but followed by pradeep



