import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'cdemo.settings'
# print(os.environ)

if __name__ == '__main__':   

    send_mail(
        'test django send mail',
        '您好，您的offer请查收',
        '18779177418@163.com',
        ['bobo.chen@weride.ai'],
    )


