import tls_client
from urllib.parse import unquote
import time
import json
def init():
    
    session = tls_client.Session(client_identifier="chrome110",
                                          random_tls_extension_order=True)
    return session


def get_email(session):
    session.get('https://www.emailnator.com')
    global xsrf_token
    global gmailnator_session
    xsrf_token = unquote(session.cookies["XSRF-TOKEN"])
    gmailnator_session = session.cookies["gmailnator_session"]
    cookies = {
        'XSRF-TOKEN': xsrf_token,
        'gmailnator_session': gmailnator_session}

    headers = {
        'authority': 'www.emailnator.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.emailnator.com',
        'referer': 'https://www.emailnator.com/',
        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': xsrf_token}

    json_data = {
        'email': [
            'plusGmail',
            'dotGmail',
        ],
    }

    emailreq = session.post('https://www.emailnator.com/generate-email', cookies=cookies, headers=headers, json=json_data)

    return emailreq.json()['email'][0]


def get_inbox(session,email):
    

    cookies = {
        'XSRF-TOKEN': xsrf_token,
        'gmailnator_session': gmailnator_session    }

    headers = { 
        'authority': 'www.emailnator.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://www.emailnator.com',
        'referer': 'https://www.emailnator.com/inbox/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': xsrf_token    }

    json_data = {
        'email' : email,
    }

    inbox = session.post('https://www.emailnator.com/message-list', cookies=cookies, headers=headers, json=json_data)
    return inbox.text


def get_content(session,email,messageid):
    cookies = {
        'XSRF-TOKEN': xsrf_token,
        'gmailnator_session': gmailnator_session    }

    headers = { 
        'authority': 'www.emailnator.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'origin': 'https://www.emailnator.com',
        'referer': 'https://www.emailnator.com/inbox/',
        'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': xsrf_token    }
    
    json_data = {
        'email' : email,
        'messageID': messageid
    }

    inbox = session.post('https://www.emailnator.com/message-list', cookies=cookies, headers=headers, json=json_data)
    return inbox.text   

