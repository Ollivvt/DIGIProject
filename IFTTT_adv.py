#! /usr/bin/python

# Imports
import time
import requests
import random

LINE_event_name = 'LLLLLLLLLLLLLLLLLLLL'
LINE_key = 'KKKKKKKKKKKKKKKKKKKKKKKKK'

SHEETS_event_name = 'SSSSSSSSSSSSSSSSSSS'
SHEETS_key = 'KKKKKKKKKKKKKKKKKKKKKKKKK'

#設定時(24小時制)
set_H = []

#設定分(0~59分)
set_M = []

#設定發送訊息內容
set_Message = []

try:
    times = int(input("請輸入要發送訊息的次數= "))
    print('')


    for i in range(times):
        H_data = int(input('請輸入第 ' + str(i+1) + ' 次發送時間(時，24小時制)= '))
        M_data = int(input('請輸入第 ' + str(i+1) + ' 次發送時間(分，0~59分)= '))
        Message_data = input('請輸入第 ' + str(i+1) + ' 次發送的訊息內容= ')

        print('')
        
        set_H.append(H_data)
        set_M.append(M_data)
        set_Message.append(Message_data)

    # Loop until users quits with CTRL+C
    while True:

        h0 = str(random.randint(0,30))
        t0 = str(random.randint(0,30))

        now_H = int(time.strftime('%H'))
        now_M = int(time.strftime('%M'))
        now_S = int(time.strftime('%S'))

        for i in range(times):
            if (now_H == set_H[i]) and (now_M == set_M[i]) and (now_S == 0):
                # Your IFTTT LINE_URL with event name, key and json parameters (values)
                LINE_URL='https://maker.ifttt.com/trigger/' + LINE_event_name + '/with/key/' + LINE_key
                r = requests.post(LINE_URL, params={"value1":h0,"value2":t0,"value3":set_Message[i]})

                # Your IFTTT SHEETS_URL with event name, key and json parameters (values)
                SHEETS_URL='https://maker.ifttt.com/trigger/' + SHEETS_event_name + '/with/key/' + SHEETS_key
                r = requests.post(SHEETS_URL, params={"value1":h0,"value2":t0,"value3":set_Message[i]})

                print('已於 ' + str(now_H) + ':' + str(now_M) + ' 完成發送第 ' + str(i+1) + ' 次訊息發送')
                
except KeyboardInterrupt:
    print(" Quit")
