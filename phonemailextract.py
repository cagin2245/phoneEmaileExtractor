import re, pyperclip

# regex for phone number
phoneRegexTR = re.compile(r'''
    
                          
                          
                          
                          ''', re.VERBOSE)
phoneRegexUS =  re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
   [a-zA-Z0-9._%+-]+      # username
   @                      # @ symbol
   [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)


text = pyperclip.paste()

extractedPhone = phoneRegexUS.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
allEmails = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
for email in extractedEmail:
    allEmails.append(email[0])

results =  str('\n'.join(allPhoneNumbers))+ '\n' + '\n' +str('\n'.join(allEmails))
pyperclip.copy(results)
