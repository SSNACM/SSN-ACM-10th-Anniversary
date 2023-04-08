from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
from fpdf import FPDF

pdf = FPDF()

cer = {
  "type": "service_account",
  "project_id": "nourishnow-ef98a",
  "private_key_id": "73483b9adde161163fb9a7dc22586b4880d564c4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDcZ6vpblbxpxqp\nZp8gOLZ+N8L2K9zN+TxdD2DmsnmOZozZ0tfS1b0xkFwZE7esgZzLvo4WxI39/ubt\n1PcibuAPz/X8ELSfO329kupgMS5HctDe5nQSMBfKY8xOp2KLgg/LRonXkKlCiVb8\nNUS/8A0fCZfb9mQmnWzdm4Ae/iziTdi2qgqGxt4EBrNM2J/o0jSgDjAFrUh6h7zi\nj5iGab2uK19lDnMAW5eWYSwZLHsqzvxWIOys+WeTToztuCIzL3VAD6/pYPLVS29G\nTpCkXvCWX3c+TQsz6KuQ0xYN5qEPDU7D6MtEAsZY6T6eCAIxQH2QP1Umw7cvca3P\npjfKr1TBAgMBAAECggEAAnDUdsiNxm3NDgiwpOzz2mh4LH02XAKRUE+CCXP7BCBv\nGV9sG+3Zg0G/v1hYTZz+1UPGM4rYLrKisIoN9Y/oQ8yQAwtVULkaLp4AofGRe2GS\nXhGLwgLN1KQvyEQyw2w8jAn7L0uvEClQsQjO+tgn8QrMZ3duSv4tzTNyYwV6DkR8\nqaKMV0F8avjaXC2XOVhocuFF6Y0YusLCCTv1ut3UvipMGs+TxNEnnL83X+hAtL4C\nC4J2R3xaBcBgokTYav9Gxhf3yGDSTAWA/n6hxCIVK45epd5iSOsxNdYgptCXOCm6\nb0d4HLW26+5ZSZuV1+2EzS+TXrtvfK2V3GHDhESAAQKBgQDxijeCskYKYYu/vP4j\nHzBfXgjqDPRcm2sYyhEhPevHW9N/S8aW2+GXY8QNuqsOLDETIn6ualAAvetN1Gjs\n16/MPafvqSosutwzyWOUSaacapy92ImNdzaa19LDY1wQ11/1fgTTuWA/XWmWeAOH\nHD83HG060Q9x2H1llkSZzIj4AQKBgQDpmYur93xEnS6N9ldkNOgDME4v5jNPkgr8\nz+ti+UfdzsH0V9PeePwChnMZkEjymJmTqAj27/yOkYVTgY0MUaQ/2dfglKh4YTqU\npKUNMT0HIwQsZPVwDMZ6iLu4L+EPd3P+h0Trks8aMww79hcESu80Y/2leEDChZQP\nF5AJvkxcwQKBgQCSUPwXfA7ZswWI/N+mPvp6iugzf+13O97AgYem72+osIOKFUkT\nkdcycgkNmAqO505DHR5IYbZc/K9R0l5NOssPmjnlAEDAH+HMrS5ZYdQ/5IVWq5mH\nzLOTUTInkkTvHsjOWaxq5VzchaW0tLbOXdoddGbmvkXw3Qf5RfIAiNpgAQKBgQC1\n/pWN1hPwFRG3Moxlmr6D9XeE4/Fn9d0vmAHIq3QtQC9l4aNEebfFc+BqsznSH8fO\n/SR21wRKQt+/7nfoeBbiVCNXahpTJ1UPh7K7s3fbfpF60PFTafCceLjfyBWtCiDJ\n1bOBYXCO9eR7NsA57POuOpTb/PNfWdi/ZVkn7iXqQQKBgQDnWF1i/ef7Y/wJM8t3\n2zLhbzR+RTwmdeH9TKaseNLyjChkPjitQp8hISMJQagPUNbY0ANoDBiG3oRNkwbW\ndxcXCB0aOKchp0Omozcw937WYZdNZg56H+wBatMcDwKh9nK1HdU0bTkP6ENC+5R6\nVDH81TocmGnJgHR1gO/3bOgHbg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-s8a3e@nourishnow-ef98a.iam.gserviceaccount.com",
  "client_id": "118010188229147225993",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-s8a3e%40nourishnow-ef98a.iam.gserviceaccount.com"
}


cred = credentials.Certificate(cer)

fb = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://nourishnow-ef98a-default-rtdb.firebaseio.com'
})

def indexPage(request):
    return render(request, "indexPage.html")

def signinPage(request):
    return render(request, "signinPage.html")

def signupDonorPage(request):
    return render(request, "signupDonorPage.html")

def signupVolunteerPage(request):
    return render(request, "signupVolunteerPage.html")

def signupAcceptorPage(request):
    return render(request, "signupAcceptorPage.html")

def gotoForm(request):
    return render(request, "https://docs.google.com/forms/d/e/1FAIpQLSebzesIElJiX6zEfCmyIFYtZiffyKErMbJrLQcQBbpt_UYvAA/viewform?usp=sharing")

def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    try:
        refAcc = db.reference('acceptors')
        refDo = db.reference('donors')
        refVo = db.reference('volunteers')

        d = {}
        for val in refAcc.get().values():
            for value in val.values():
                if (value['email'] == email):
                    d = value
        for val in refDo.get().values():
            for value in val.values():
                if (value['email'] == email):
                    d = value
        for val in refVo.get().values():
            for value in val.values():
                if (value['email'] == email):
                    d = value
        if d['password'] != password:
            raise ConnectionError
        else:
            if 'income' in d:
                return render(request, "dashboardAcceptorPage.html")
            elif 'fssai' in d:
                return render(request, "dashboardDonorPage.html")
            else:
                return render(request, "indexPage.html")
    except:
        return render(request, "signinPage.html", {"error": "Invalid Credentials"})

def acceptor(request):
    name = request.POST.get('nameAcc')
    phone = request.POST.get('phoneAcc')
    address = request.POST.get('addressAcc')
    income = request.POST.get('incomeAcc')
    email = request.POST.get('emailAcc')
    user = request.POST.get('userAcc')
    password = request.POST.get('passwordAcc')
    passwordCon = request.POST.get('passwordConAcc')
    gender = request.POST.get('genderAcc')

    try:
        if (password == passwordCon):
            data = {phone: {"name":name, "address":address, "income":income,
                        "email":email, "username":user, "password":password,
                        "gender":gender}}
            ref = db.reference('acceptors')
            ref.push(data)
            user = auth.create_user(email=email, password=password)
        else:
            raise ConnectionAbortedError
    except:
        return render(request, "signupAcceptorPage.html", {"error": "Invalid Credentials"})
    return render(request, "dashboardAcceptorPage.html")

def donor(request):
    name = request.POST.get('nameDo')
    phone = request.POST.get('phoneDo')
    typeof = request.POST.get('typeDo')
    fssai = request.POST.get('fssaiDo')
    email = request.POST.get('emailDo')
    user = request.POST.get('userDo')
    password = request.POST.get('passwordDo')
    passwordCon = request.POST.get('passwordConDo')
    gender = request.POST.get('genderDo')

    try:
        if (password == passwordCon):
            data = {phone: {"name":name, "type":typeof, "fssai":fssai,
                        "email":email, "username":user, "password":password,
                        "gender":gender}}
            ref = db.reference('donors')
            ref.push(data)
            user = auth.create_user(email=email, password=password)
        else:
            raise ConnectionAbortedError
    except:
        return render(request, "signupDonorPage.html", {"error": "Invalid Credentials"})
    return render(request, "dashboardDonorPage.html")

def contactSubmit(request):
    name = request.POST.get('nameIn')
    email = request.POST.get('emailIn')
    phone = request.POST.get('phoneIn')
    msg = request.POST.get('messageIn')

    try:
        data = {phone:{"email":email, "name":name, "query":msg}}
        ref = db.reference('queries')
        ref.push(data)
    
    except:
        return render(request, "indexPage.html")
    return render(request, "indexPage.html")

def volunteer(request):
    name = request.POST.get('nameVo')
    phone = request.POST.get('phoneVo')
    email = request.POST.get('emailVo')
    user = request.POST.get('userVo')
    password = request.POST.get('passwordVo')
    passwordCon = request.POST.get('passwordConVo')
    gender = request.POST.get('genderVo')

    try:
        if (password == passwordCon):
            data = {phone: {"name":name,"email":email, "username":user, 
                        "password":password,
                        "gender":gender}}
            ref = db.reference('volunteers')
            ref.push(data)
            user = auth.create_user(email=email, password=password)
        else:
            raise ConnectionAbortedError
    except:
        return render(request, "signupVolunteerPage.html", {"error": "Invalid Credentials"})
    return render(request, "indexPage.html")

def food(request):
    item = request.POST.get('item')
    type = request.POST.get('type')
    add = request.POST.get('add')
    city = request.POST.get('city')
    phn = request.POST.get('phn')
    nop = request.POST.get('nop')
    date = request.POST.get('date')
    time = request.POST.get('time')
    ref = db.reference('donors')
    d = {}
    for val in ref.get().values():
        for value in val.keys():
            if (value == phn):
                d = val
    d = d[str(phn)]
    print(d)
    data = {phn: {"item":item,"type":type, "address":add, 
                        "city":city, "email":d["email"], "FSSAI No":d["fssai"], "name":d["name"],
                        "noofplates":nop, "date":date, "time":time}}
    ref = db.reference('food')
    ref.push(data)
    return render(request, "dashboardDonorPage.html", {"error": "Details Submitted successfully"})

def acceptorFood(request):
    item = request.POST.get('fitem')
    type = request.POST.get('ftype')
    add = request.POST.get('fadd')
    city = request.POST.get('fcity')
    phn = request.POST.get('fphn')
    nop = request.POST.get('fnop')
    date = request.POST.get('fdate')
    time = request.POST.get('ftime')
    email = request.POST.get('femail')

    ref = db.reference('food')
    for val in ref.get().values():  
        for k,v in val.items():
            pdf.add_page()
            pdf.set_font("Arial", size=20)
            pdf.cell(200, 10, txt="Name: " + v['name'], ln=2, align='L')
            pdf.cell(200, 10, txt="Phone Number: " + k, ln=2, align='L')
            pdf.cell(200, 10, txt="Email Id: " + v['email'], ln=2, align='L')
            pdf.cell(200, 10, txt="FSSAI Number: " + v['FSSAI No'], ln=2, align='L')
            pdf.cell(200, 10, txt="Address: " + v['address'], ln=2, align='L')
            pdf.cell(200, 10, txt="City: " + v['email'], ln=2, align='L')
            pdf.cell(200, 10, txt="Food Item: " + v['item'], ln=2, align='L')
            pdf.cell(200, 10, txt="Food Type: " + v['type'], ln=2, align='L')
            pdf.cell(200, 10, txt="No of Plates: " + v['noofplates'], ln=2, align='L')
            pdf.cell(200, 10, txt="Date: " + v['date'], ln=2, align='L')
            pdf.cell(200, 10, txt="time: " + v['time'], ln=2, align='L')
            
    pdf.output("C:\\Users\\Raghul\\Desktop\\NourishNow\\nourishnowapp\\nourishnowapp\\static\\pdf\\list.pdf")
    
    return render(request, "dashboardAcceptorPage.html")

def pdfview(request):
    return render(request, "pdfViewer.html")