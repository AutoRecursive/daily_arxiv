from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
from smtplib import SMTP

def send_email(title, content):

    #发送者邮箱
    sender = ''#'dailyarxiv@163.com'
    #发送者的登陆用户名和密码
    user = ''#'dailyarxiv@163.com'
    password = 'aaaaaaaa'#dailyarxiv123
    #发送者邮箱的SMTP服务器地址
    smtpserver = 'smtp.163.com'
    #接收者的邮箱地址
    receiver = 'youremail@qq.com' #receiver 可以是一个list


    msg = MIMEMultipart('alternative')  

    part1 = MIMEText(content, 'plain', 'utf-8')  
    #html = open('subject_file.html','r')
    #part2 = MIMEText(html.read(), 'html')

    msg.attach(part1)  
    #msg.attach(part2)

    #发送邮箱地址
    msg['From'] = sender
    #收件箱地址
    msg['To'] = receiver
    #主题
    msg['Subject'] = title

    smtp = smtplib.SMTP() #实例化SMTP对象
    smtp.connect(smtpserver, 25) #（缺省）默认端口是25 也可以根据服务器进行设定
    smtp.login(user, password) #登陆smtp服务器
    smtp.sendmail(sender, receiver, msg.as_string()) #发送邮件 ，这里有三个参数
    '''
    login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文
    是一个str，as_string()把MIMEText对象变成str。
    '''
    smtp.quit()




    # '''send email'''
    # #selected_papers.to_html('email.html')
    # content = 'Today arxiv has {} new papers in CS area, and {} of them is about CV, {}/{} of them contain your keywords.\n\n'.format(len(list_title), subject_cnt['Computer Vision and Pattern Recognition (cs.CV)'], len(selected_papers), len(selected_papers2))
    # content += 'Ensure your keywords is ' + str(key_words) + ' and ' + str(Key_words) + '(case=True). \n\n'
    # content += 'This is your paperlist.Enjoy! \n\n'
    # for i, selected_paper in enumerate(zip(selected_papers['id'], selected_papers['title'], selected_papers['authors'], selected_papers['subject_split'])):
    #     #print(content1)
    #     content1, content2, content3, content4 = selected_paper
    #     content += '------------' + str(i+1) + '------------\n' + content1 + content2 + str(content4) + '\n'
    #     content1 = content1.split(':', maxsplit=1)[1]
    #     content += 'https://arxiv.org/abs/' + content1 + '\n\n'

    # content += 'Ensure your keywords2 is ' + str(key_words2) + ' and ' + str(Key_words2) + '(case=True). \n\n'
    # content += 'This is your paperlist.Enjoy! \n\n'
    # for i, selected_paper2 in enumerate(zip(selected_papers2['id'], selected_papers2['title'], selected_papers2['authors'], selected_papers2['subject_split'])):

    #     #print(content1)
    #     content1, content2, content3, content4 = selected_paper2
    #     content += '------------' + str(i+1) + '------------\n' + content1 + content2 + str(content4) + '\n'
    #     content1 = content1.split(':', maxsplit=1)[1]
    #     content += 'https://arxiv.org/abs/' + content1 + '\n\n'


    # content += 'Here is the Research Direction Distribution Report. \n\n'
    # for subject_name, times in subject_items:
    #     content += subject_name + '   ' + str(times) +'\n'
    # title = time.strftime("%Y-%m-%d") + ' you have {}+{} papers'.format(len(selected_papers), len(selected_papers2))
    # # send_email(title, content)
    # freport = open('/home/zzh/Code/Spider/paperspider/arxiv/report/'+title+'.txt', 'w')
    # freport.write(content)
    # freport.close()


    # '''dowdload key_word selected papers'''
    # list_subject_split = []
    # if not os.path.exists('/home/zzh/Code/Spider/paperspider/arxiv/selected/'+time.strftime("%Y-%m-%d")):
    #     os.makedirs('/home/zzh/Code/Spider/paperspider/arxiv/selected/'+time.strftime("%Y-%m-%d"))
    # for selected_paper_id, selected_paper_title in zip(selected_papers['id'], selected_papers['title']):
    #     selected_paper_id = selected_paper_id.split(':', maxsplit=1)[1]
    #     selected_paper_title = selected_paper_title.split(':', maxsplit=1)[1]
    #     r = requests.get('https://arxiv.org/pdf/' + selected_paper_id) 
    #     while r.status_code == 403:
    #         time.sleep(500 + random.uniform(0, 500))
    #         r = requests.get('https://arxiv.org/pdf/' + selected_paper_id)
    #     selected_paper_id = selected_paper_id.replace(".", "_")
    #     pdfname = selected_paper_title.replace("/", "_")   #pdf名中不能出现/和：
    #     pdfname = pdfname.replace("?", "_")
    #     pdfname = pdfname.replace("\"", "_")
    #     pdfname = pdfname.replace("*","_")
    #     pdfname = pdfname.replace(":","_")
    #     pdfname = pdfname.replace("\n","")
    #     pdfname = pdfname.replace("\r","")
    #     print('/home/zzh/Code/Spider/paperspider/arxiv/selected/'+time.strftime("%Y-%m-%d")+'/%s %s.pdf'%(selected_paper_id, selected_paper_title))
    #     with open('/home/zzh/Code/Spider/paperspider/arxiv/selected/'+time.strftime("%Y-%m-%d")+'/%s %s.pdf'%(selected_paper_id,pdfname), "wb") as code:    
    #        code.write(r.content)

