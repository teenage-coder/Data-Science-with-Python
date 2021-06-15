
fd = open('emails.txt','r')

data = fd.read()

fd.close()

emails = data.split('\n')

for email in emails:

    email_id = email.split("@")[1].split('.')[0]
    user_name = email.split("@")[0]

    
    print(user_name , email_id)

