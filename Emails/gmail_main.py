import Emails.Gmail_API_Handlers as handler
from Emails import send_mail
from Emails.email_content import data_901, data_bad_phone, data_bad_addy, \
data_sv, loa_term
from Emails.email_lists import isss, test_list, redundancy_test, my_email
from Banner_Connections.Initialize_Oracle_Connection import \
banner_ods_handler, banner_ODSP_emails
import Banner_Connections.queries as query


e_content_list = \
    {'a': data_bad_addy,
    'p': data_bad_phone,
    's': data_sv,
    'f': data_901,
    'lt': loa_term}

e_group_list = {'is': isss, 'rd': redundancy_test, 'ts': test_list}

email_group_choices = ['is - ISSS Staff','ts - Test', 'rd - Redundant Test',
                       'sl - student list']

email_content_choices = \
    ['a - Bad Address Email',
    'p - Bad Phone Email',
    's - Status Verification Incomplete Email',
    'f - I-901 Fee Unpaid',
    'lt - LOA Termination Email'
    '\nHit Enter to skip and create a custom message']


def get_email_message_content(e_content_list):
    """:returns a user's choice from the email content list"""
    print('\nWhich message would you like to send: ')
    for choice in email_content_choices:
        print(choice)
    content = input('\nYour Choice: ')
    for x in e_content_list.keys():
        if x == content:
            return e_content_list[x]


def get_email_blast_list(e_group_list):
    """:returns a user's choice from the email e_group_list"""
    print('\nPick a target group:')
    for choice in email_group_choices:
        print(choice)
    which_list = input('\nInput a group you like to blast message: ')
    for x in e_group_list.keys():
        if x == which_list:
            return e_group_list[x]


def singular_email(get_emessage_content):
    """
    Function takes in input from a user to specify the receiver and the email
    subject and then sends a message with a defined body of content
    """
    sendInstance = send_mail.SendEmail(handler.service)
    receiver_input = input('Receiver Email: ')
    try:
        if get_emessage_content != None:
            subject_input = input('Email Subject: ')
            message = sendInstance.create_message(my_email,
            receiver_input, subject_input, get_emessage_content)
            sendInstance.send_message('me',message)
            print(f'\nEmail sent to {receiver_input}!')
        if get_emessage_content == None:
            subject_input = input('Email Subject: ')
            content = input('Please type your message: ')
            message = sendInstance.create_message(my_email,
            receiver_input, subject_input, content)
            sendInstance.send_message('me', message)
            print(f'\nEmail sent to {receiver_input}!')
    except:
        print('You must type a message body if one is not chosen '
              'from get_emessage_content')


def multiple_emails(get_eblast_list, get_emessage_content):
    """
    Function takes in input from a user to specify the email
    subject and then sends a message with a defined body of content to several
    email addresses by looping through a list of emails [i].
    """
    sendInstance = send_mail.SendEmail(handler.service)
    try:
        if get_emessage_content != None:
            subject_input = input('Email Subject: ')
            for email in get_eblast_list:
                message = sendInstance.create_message(my_email,
                email, subject_input, get_emessage_content)
                sendInstance.send_message('me', message)
                print(f'\nEmail sent to {email} in email list!')
        if get_emessage_content == None:
            subject_input = input('Email Subject: ')
            content = input('Please type your message: ')
            for email in get_eblast_list:
                message = sendInstance.create_message(my_email,
                email, subject_input, content)
                sendInstance.send_message('me', message)
                print(f'\nEmail sent to {email} in email list!')
    except:
        print('You must type a message body if one is not chosen '
              'from get_emessage_content')


def banner_query_singular_email(get_email_message_content):
    """
    Function takes in input from a user to specify the receiver and the email
    subject and then sends a message with a defined body of content
    """
    sendInstance = send_mail.SendEmail(handler.service)
    receiver_input = banner_ODSP_emails(banner_ods_handler(),
                                        query.run_single_email_query())
    try:
        if get_email_message_content != None:
            subject_input = input('Email Subject: ')
            message = sendInstance.create_message(my_email,
            receiver_input, subject_input, get_email_message_content)
            sendInstance.send_message('me',message)
            print(f'\nEmail sent to {receiver_input}!')
        if get_email_message_content == None:
            subject_input = input('Email Subject: ')
            content = input('Please type your message: ')
            message = sendInstance.create_message(my_email,
            receiver_input, subject_input, content)
            sendInstance.send_message('me', message)
            print(f'\nEmail sent to {receiver_input}!')
    except:
        print('You must type a message body if one is not chosen '
              'from get_emessage_content')


def banner_query_blast_email(get_email_message_content):
    """
    Function takes takes a list of emails generated from the active_emails
    banner query, prompts the user for an email subject and then sends a message
    with a defined body of content to several
    email addresses by looping through a list of emails.
    """
    sendInstance = send_mail.SendEmail(handler.service)
    get_email_banner_list = banner_ODSP_emails(banner_ods_handler(),
                                               query.active_emails)
    try:
        if get_email_message_content != None:
            subject_input = input('Email Subject: ')
            for email in get_email_banner_list:
                message = sendInstance.create_message(my_email,
                email, subject_input, get_email_message_content)
                sendInstance.send_message('me', message)
                print(f'\nEmail sent to {email} in email list!')
        if get_email_message_content == None:
            subject_input = input('Email Subject: ')
            content = input('Please type your message: ')
            for email in get_email_banner_list:
                message = sendInstance.create_message(my_email,
                email, subject_input, content)
                sendInstance.send_message('me', message)
                print(f'\nEmail sent to {email} in email list!')
    except:
        print('You must type a message body if one is not chosen '
        'from get_emessage_content')
