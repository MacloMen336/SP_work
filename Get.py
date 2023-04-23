from bs4 import BeautifulSoup
import requests
from Web_site import settings

import re

print('Расписание группы И-101 или Всех групп на день? вывести 1 или 2?')
what_need = int(input())
if what_need == 1:
    site_url = settings['rasp_i_101']
    num_delete_line = 104
elif what_need == 2:
    site_url = settings['rasp_all_grups']
    num_delete_line = 98
else:
    site_url = settings['rasp_i_101']
    num_delete_line = 104
url = site_url #website 
resp = requests.get(url) #get all from site ()
resp.encoding = 'windows-1251' #because site biik.ru rasp use cp-1251 need do that 
#print(resp) #write site answer code
if resp == 404: #check if site not work
    print('Not Found')
else:
    all_web_code = resp.text #take text chapter from site 
    bs = BeautifulSoup(all_web_code,"html.parser") #bs html.parser needed site 
    Lesson = bs.findAll('td') #find all class in tag 'td'

    file = open("Rasp.txt", "w") #write in file
    for item in Lesson: #write all text from html tag in txt file
        file.write(item.text +"\n")
    file.close()
    
    line = open("Rasp.txt").readlines() #list all line in txt file 
    for i in range(num_delete_line): #Delete first 104 line, because they unused
        line.pop(0)

    #--Добавление разделения на подгруппы--
    for j in range(len(line)):
        i = line[j]
        if (i[0].isnumeric()) and (i[1] == ' ') and (i[0]!='8'):
            if line[j+2][:1].isnumeric():
                line[j+1] = str('Общая пара) ' + line[j+1])

            if line[j+3][:1].isnumeric():
                line[j+1] = str('1-подгр) ' + line[j+1])
                line[j+2] = str('2-подгр) ' + line[j+2])
                
    f = open("Rasp.txt", "w") #after delete unused elements, write new line in txt file
    for i in line:
        f.write(i)
    f.close()

    # # форма таблицы вывода
    # for i in range(len(line)):

    #     if '\d{2}.\d{2}.' in line[i]:
    #         print('A')
    #         line[i] = line[i] + ' Подгруппа 1       Подгруппа 2'

    # print('Schedule on next study day: ') #write in console schedule on next study day
    # f = open("Rasp.txt", 'r')
    # f1 = open("Rasp_next_day.txt", "w")
    # for i in range(19):
    #     strok = f.readline()
    #     f1.write(strok)
    #     print(strok[:-1]) #delete last symbol (/n) from line
    # f.close()
    
    print('All Ready') #write if programm do all work
    #print(settings['rasp_i_101'])
    #print(line)
    
