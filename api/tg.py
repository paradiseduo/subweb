# coding=utf-8
import sys
import  requests
if __name__ == '__main__':
    message = ''
    for i in range(1,len(sys.argv)):
        message = message +' '+ sys.argv[i]
    requests.post('https://api.telegram.org/bot{token}?chat_id={id}&text={text}'.format(token='',id='',text=message))      
