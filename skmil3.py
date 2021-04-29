import sys
import imaplib
import getpass
import email
import email.header
import datetime
from datetime import datetime as skdate


EMAIL_ACCOUNT = "dbtestingsk@gmail.com"

# Use 'INBOX' to read inbox.  Note that whatever folder is specified, 
# after successfully running this script all emails in that folder 
# will be marked as read.
EMAIL_FOLDER = "Inbox" #"Top Secret/PRISM Documents"


def process_mailbox(M):
    """
    Do something with emails messages in the folder.  
    For the sake of this example, print some headers.
    """

    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Message %s: %s' % (num, subject))
        # print('Subject was',subject)
        # print('Raw Date:', msg['Date'])
        
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print ("Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S"))
            ######Difference
            # from datetime import datetime
            then = skdate(2021, 4, 28, 19, 2, 13)  
            if local_date>then:
                vs=local_date.strftime("%a, %d %b %Y %H:%M:%S")
                print('diffeence date.......................... ',vs)
                print('ALL DIR',dir(msg.set_payload))

            # then = datetime(2021, 4, 27, 9, 37, 13) 
            # if local_date<
            


M = imaplib.IMAP4_SSL('imap.gmail.com')

try:
    rv, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)

print(rv, data)

rv, mailboxes = M.list()
if rv == 'OK':
    print("Mailboxes:")
    print(mailboxes)

rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    print("Processing mailbox...\n")
    process_mailbox(M)
    M.close()
else:
    print("ERROR: Unable to open mailbox ", rv)


###############
from datetime import datetime
import numpy as np
then = datetime(2021, 4, 27, 9, 37, 13)        # Random date in the past (2012, 3, 5, 23, 8, 15) 
now  = datetime.now()                         # Now
duration = now - then  
print("duration",duration,then)



M.logout()



################################################



import email
import imaplib

EMAIL = "dbtestingsk@gmail.com"
PASSWORD = "Selva_12345"
SERVER = 'imap.gmail.com'

# connect to the server and go to its inbox
mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
# we choose the inbox but you can select others
mail.select('inbox')

# we'll search using the ALL criteria to retrieve
# every message inside the inbox
# it will return with its status and a list of ids
status, data = mail.search(None, 'ALL')
# the list returned is a list of bytes separated
# by white spaces on this format: [b'1 2 3', b'4 5 6']
# so, to separate it first we create an empty list
mail_ids = []
# then we go through the list splitting its blocks
# of bytes and appending to the mail_ids list
for block in data:
    # the split function called without parameter
    # transforms the text or bytes into a list using
    # as separator the white spaces:
    # b'1 2 3'.split() => [b'1', b'2', b'3']
    mail_ids += block.split()

# now for every id we'll fetch the email
# to extract its content
for i in mail_ids:
    # the fetch function fetch the email given its id
    # and format that you want the message to be
    status, data = mail.fetch(i, '(RFC822)')

    # the content data at the '(RFC822)' format comes on
    # a list with a tuple with header, content, and the closing
    # byte b')'
    for response_part in data:
        # so if its a tuple...
        if isinstance(response_part, tuple):
            # we go for the content at its second element
            # skipping the header at the first and the closing
            # at the third
            message = email.message_from_bytes(response_part[1])

            # with the content we can extract the info about
            # who sent the message and its subject
            mail_from = message['from']
            mail_subject = message['subject']
            print('subject was',mail_subject)

            # then for the text we have a little more work to do
            # because it can be in plain text or multipart
            # if its not plain text we need to separate the message
            # from its annexes to get the text
            if message.is_multipart():
                mail_content = ''

                # on multipart we have the text message and
                # another things like annex, and html version
                # of the message, in that case we loop through
                # the email payload
                for part in message.get_payload():
                    # if the content type is text/plain
                    # we extract it
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                # if the message isn't multipart, just extract it
                mail_content = message.get_payload()

            # and then let's show its result
            cont=f'Content: {mail_content}'
            # print(f'From: {mail_from}')
            # print(f'Subject: {mail_subject}')
            # print(f'Content: {mail_content}')
            print('Contents_ne',len(cont),'result......',type(cont))
            #######################################################
            #######################################################
            import re
            import requests

            # email = '<email text here> Maybe I have a URL like http://cnn.com or maybe it is something more complex like https://stackoverflow.com/questions/49654499/python-extract-urls-from-email-messages'
            # email = "http://cnn.com"
            regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

            match = re.findall(regex, cont)
            import os
            c=0
            for m in match:
                print(m)
                # filePath2 = os.path.join('D:/Work/Development/Automation/mailfilt/mailfilter/out','https://drive.google.com/file/d/1ZSTADvi2bVNL2EUmY_DsgJh-PfWXEl9Q/view?usp=sharing/C-V-Raman.jpg')
                filePath=str(m)
                print('pathname',filePath)
                from googleDriveFileDownloader import googleDriveFileDownloader
                a = googleDriveFileDownloader()
                a.downloadFile(filePath)
                # print(a)
                url = filePath
                if mail_subject=='cvraman':
                    
                    import wget

                    url =r"https://drive.google.com/file/d/1ZSTADvi2bVNL2EUmY_DsgJh-PfWXEl9Q/view?usp=sharing"

                    wget.download(url,r'D:\Work\Development\Automation\mailfilt\mailfilter\out\fg.jpg')

                    # from google_drive_downloader import GoogleDriveDownloader as gdd

                    # gdd.download_file_from_google_drive(file_id=r"https://drive.google.com/file/d/1ZSTADvi2bVNL2EUmY_DsgJh-PfWXEl9Q/view?usp=sharing",dest_path='D:\Work\Development\Automation\mailfilt\mailfilter\out\sk.jpg')
                    # print('download....................')
                                                        

                    nwurl=url+'cvraman.jpg'
                    print('cvraman url',nwurl)
                    r = requests.get(nwurl, allow_redirects=True)
                    name='img'+str(c)+'.jpg'
                    open(name, 'wb').write(r.content)
                    c=c+1


                # if not os.path.isfile(filePath2) :
                #     fp = open(filePath2, 'wb')
                #     fp.write(part.get_payload(decode=True))
                #     fp.close()
                # subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            ########################################################
            #########################################################
            # for mail in emails: 
            #     # check for attachment; 
            #     for part in mail.walk(): 
            #         if not mail.is_multipart(): 
            #             continue 
            #         if mail.get('Content-Disposition'): 
            #             continue 
            #         file_name = part.get_filename() 
            #         # check if email park has filename --> attachment part 
            #         if file_name: 
            #             file = open(file_name,'w+') 
            #             file.write(part.get_payload(decode=True)) 
            #             file.close() 
