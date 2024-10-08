#importing required packages
import re

#demonstration of use of raw strings
#print("\tTab")
#print(r"\tTab")

#generating text to search through
txt = r'''
This is a long string of text that contains many things such as,
phone numbers:0143831967
07411 375 322
0741 385 4316
333-555-123
as you can see the phone number are in multiple formats.
There are also we addresses:
contact@darthvader.co.uk
michealphelps86@gmail.com
daddyyankee22@gmail.com
iang@costco.com
spankmonkey27@aol.com
trevor_paulson@hotmail.com
ddanniel@london.ac.uk
special.agent.123@washington.gov.uk

Finally we also have domain names: beansonfire.com
cheeseontoast.co.uk
wwww.cheeseymonkeytoast.org.uk
http://www.helpiburnedmytoast.net
http://cheeseontoastlive.co.uk
https://www.theinternet.com/bazooka-joe
https://the-internet.gov.uk/bazooka-david/test-124
ww2.testnet.gov.uk
http://gmail.com
https://www.hotmail.com
www.aol.com/the-news-from-1999/

This should be a good chunk of text for searching through
'''

#printing text
#print(txt)

#creating the regex patter that we want to search for
#pattern = re.compile(r"abc") #this will literally search for "abc" (no regex) <- this finds no matches
#pattern = re.compile(r".com") #this will literally search for ".com" (no regex) <- matches are found
#pattern = re.compile(r".+@.+(\.[A-z]{2}[A-z]?)") #example pattern that extracts emails
pattern = re.compile(r"(http(s)?:\/\/)?(ww(w|2)\.)?([A-z0-9-])+\.[A-z]{2,3}(\.[A-z]{2,3})?((\/[A-z0-9-]+)?){1,10}(?![A-z])") #pattern that extracts domains

#finding "compiled regex"
matches = pattern.finditer(txt)

#this creates a callable_iterator
#print(type(matches))  #realistically we need to convert this into a list

#once we turn it into a list it is "consumed" and cannot be re-used
match_list = list(matches)

#if statement to make sure something was found
if len(match_list) == 0:

    #printing no match found
    print("No regex match found")

#if at least one match was found
else:

    # initiating list to store domains
    domains = []

    #running through all found matches
    for match in match_list:

        #printing match
        #print(match) # print match
        #print(match.span()) #prints spans

        #printing found match (this makes more sense for a regex match)
        #print(txt[match.span()[0]:match.span()[1]])

        #gather url
        url = txt[match.span()[0]:match.span()[1]]

        #removing http:// & https://
        url = re.sub(r"^(http(s)?:\/\/)","",url)

        #removing www & ww2
        url = re.sub(r"^(ww(w|2)\.)","",url)

        #removing subfolders
        url = re.sub(r"/.*$","",url)

        #storing domains
        domains.append(url)

#de duping list
domains = list(dict.fromkeys(domains))

print(domains)

#generating second set of text
txt_2 = '''
\\x0c test test test \\x1c \\n \\n \\n \\n 
123 4445 8123\\n
test 7 123
\\x0c \\x9c \\n
'''

#printing without replacement
print(txt_2)

#directly removing special characters
reg_1 = re.compile("\\\\x[0-9]c") #compiling to remove anything like \x0c backslashes have to be tripple escaped eg \\\\=\
reg_2 = re.compile("[^0-9]")  #compiling to remove anything other than a number

txt_2 = reg_1.sub("", txt_2) #performing first replacement

print(reg_2.sub("",txt_2)) #performing second replacement and printing.

#stop point for debug
print("The code has run")