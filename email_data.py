import imaplib
import email
import os

# must change host name/site to run this program on other email services
host = 'imap.gmail.com'
username = # gmail username string goes here
password = # gmail password string goes here
mail = imaplib.IMAP4_SSL(host)
mail.login(username,password)
# selects which inbox you're in (can see available folders using mail.list())
mail_select = '"[Gmail]/Sent Mail"'
mail.select(mail_select)

def search_inbox(status, info):
    _,search_data = mail.search(None,status)
    # status can be 'SEEN', 'UNSEEN', or 'ALL'


    for item in search_data[0].split():
        _, data = mail.fetch(item, '(RFC822)')
        _ , b = data[0]
        email_message = email.message_from_bytes(b)

        # info is one of the following items in the list, taken as a dictionary key binding for the email_message dictionary ['subject','to','from','date']    
        
        with open((f'{status}_mail.txt'.format()).lower(),'a') as f:
        # must directly substitute info (subject,to,from,date) for subject here. WILL NOT WORKL BY SIMPLY PUTTING INFO VARIABLE PARAM
            if email_message['to'][0:2] != '=?':                
                    f.write(email_message['to'])
                    f.write('\n')

    with open((f'{status}_mail.txt'.format()).lower(),'r') as f:        
        file_contents = f.read()
        _list = file_contents.split('\n')
        rep_dict = {}
        for i in _list:
            if i in rep_dict:
                rep_dict[i] += 1
                #sus
            else:
                rep_dict[i] = 1
        if '' in rep_dict:
            del rep_dict['']
        sort_dict = sorted(rep_dict.items(),key=lambda x:x[1],reverse = True)
        with open(f'{info}.txt'.format(),'w') as file_object:
            for i in sort_dict:
                file_object.write(i[0] + ': ' + str(i[1]))
                file_object.write('\n')
    os.remove((f'{status}_mail.txt'.format()).lower())
    return sort_dict   

search_inbox('ALL','to')

            



