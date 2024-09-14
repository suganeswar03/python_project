import psutil
import smtplib
import ssl
from email.message import EmailMessage

sender_email = 'suganeswar2000@gmail.com'
receiver_email = 'suganeswar2000@gmail.com'
password = 'rvqc kgbr xreb wkii'

def get_running_services():
    running_services = set()
    for service in psutil.win_service_iter():
        if service.status()=='running':
            running_services.add(service.name())
    return running_services
#new service aler
def send_warning_email(new_service):
    subject = 'NEW SERVICE ALERT!!! from SUGANESWAR SAVADAMUTHU'
    body = f'New services detected: {new_service}'
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(sender_email, password)
            smtp.sendmail(sender_email, receiver_email, em.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    existing_services = get_running_services()

    while True:
        current_services = get_running_services()
        new_services = current_services - existing_services

        if new_services:
            print("New services detected:")
            for service in new_services:
                print(f"- {service}")
                send_warning_email(service)

        existing_services = current_services

if __name__ == "__main__":
    main()

