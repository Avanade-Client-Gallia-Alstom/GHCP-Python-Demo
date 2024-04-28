import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")

def monitor_memory_usage():
    while True:
        memory_usage = psutil.virtual_memory().percent
        print(f"Memory Usage: {memory_usage}%")

#create a function for sending an email
def send_email(subject, message, from_email, to_email, password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    # Create a SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        print("Email sent successfully")

# Example usage
subject = "CPU and Memory Usage Report"
message = "This is a report on the CPU and memory usage."
from_email = "your_email@gmail.com"
to_email = "recipient_email@gmail.com"
password = "your_password"

def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU Usage: {cpu_usage}%")
        if cpu_usage > 80:
            send_email(subject, message, from_email, to_email, password)

if __name__ == '__main__':
    monitor_cpu_usage()
    monitor_memory_usage()

