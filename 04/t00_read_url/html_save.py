from helper import print_stderr, print_stdout
import requests as req
import re


def html_save(site, fpath):
    if not re.match("^(?:http(s)?:\/\/)[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:\/?#[\]@!\$&'\(\)\*\+,;=.]+$", site):
        print_stderr('The site URL format is invalid')
    print_stdout(f"Sending the request to the '{site}'")
    try:
        r = req.get(site)
    except req.ConnectionError as e:
        print_stderr(e)
    print_stdout(f"Request to the '{site}' has been sent")
    print_stdout(f'<Response [{r.status_code}]>')
    if r.status_code != 200:
        print_stderr('Request failed')
    else:
        print_stdout('Parsing page data')
        with open(fpath, 'wb')as f:
            print_stdout('Page data has been parsed')
            print_stdout(f"Saving page data to '{fpath}'")
            f.write(r.content)
            print_stdout('Page data has been saved')


#if __name__== '__main__':
#    print('*** Test 1 ***')
#    html_save('https://www.bbc.com/', 'bbc.html')
#    print('*** Test 2 ***')
#    html_save('bbc.com', 'bbc.html')