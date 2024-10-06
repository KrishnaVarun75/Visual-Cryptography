#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import random
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class crypto:

    def __init__(self):
        img = Image.new('1', (150, 150), color=255)  
        self.txt = ''
        for i in range(6):
            self.txt += chr(random.randint(97, 122))
        ImageDraw.Draw(img).text(xy=(0, 50), text=self.txt,
                                 font=ImageFont.truetype('C:\WINDOWS\Fonts\ARLRDBD.TTF'
                                 , 37))
        img.save('source_image.jpg')

        image = Image.open("C:\\Users\\DELL\\Downloads\\hii.jpg")
        image = image.convert('1') 
      
        out1 = Image.new('1', [dimension * 2 for dimension in
                                image.size])  
        out2 = Image.new('1', [dimension * 2 for dimension in
                                image.size])

        lists=[[255,0,255,0], [0,255,0,255]]
        for x in range(0, image.size[0]):
           for y in range(0, image.size[1]): 
                pixel=image.getpixel((x,y)) 
                pattern=random.choice(lists) 
                if pixel==0: 
                     out1.putpixel((x * 2, y * 2), pattern[0])
                     out1.putpixel((x * 2 + 1, y * 2), pattern[1])
                     out1.putpixel((x * 2, y * 2 + 1), pattern[2])
                     out1.putpixel((x * 2 + 1, y * 2 + 1), pattern[3])
                     
                     out2.putpixel((x * 2, y * 2), 255-pattern[0])
                     out2.putpixel((x * 2 + 1, y * 2), 255-pattern[1])
                     out2.putpixel((x * 2, y * 2 + 1), 255-pattern[2])
                     out2.putpixel((x * 2 + 1, y * 2 + 1), 255-pattern[3])
                else: 
                     out1.putpixel((x * 2, y * 2), pattern[0])
                     out1.putpixel((x * 2 + 1, y * 2), pattern[1])
                     out1.putpixel((x * 2, y * 2 + 1), pattern[2])
                     out1.putpixel((x * 2 + 1, y * 2 + 1), pattern[3])
                     
                     out2.putpixel((x * 2, y * 2), pattern[0])
                     out2.putpixel((x * 2 + 1, y * 2), pattern[1])
                     out2.putpixel((x * 2, y * 2 + 1), pattern[2])
                     out2.putpixel((x * 2 + 1, y * 2 + 1), pattern[3])


        out1.save(r'out1.jpg')
        out2.save('out2.jpg')


    def GetPassword(self):
        return self.txt


    def GetPicture(self):
        with open(r'out1.jpg', 'rb') as infile1:
            infile_read = infile1.read()
        infile1.close()
        return infile_read


    def Send_Out2_By_Email(self, email_addr):
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587
        content = MIMEMultipart()
        content['From'] = 'himamshg@gmail.com'
        content['To'] = 'cb.en.u4aie21014@cb.students.amrita.edu'
        content['Subject'] = 'Password First Picture'
        content.attach(MIMEText('Here is the first picture of the password:'
                       , 'plain'))
        filename = "C:\\Users\\DELL\\Downloads\\hii.jpg"
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= '
                        + filename)

        content.attach(part)
        content = content.as_string()
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        mail.starttls()
        mail.login('varunias2004@gmail.com', 'cpmf ahfq ghnp ysya')
        try:
            mail.sendmail('himamshg@gmail.com', [email_addr], content)
        except:
            print ("Unexpected Client Error 1.")
