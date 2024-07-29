import smtplib
import dotenv
import os

class Mail:
    def __init__(self) -> None:
        dotenv.load_dotenv(os.path.join(os.getcwd(),".env"))
        self.email = os.environ["email"]
        self.password =  os.environ["password"]
    def sendmail(self,sendto: str = None) -> None:
        if sendto:
            print(f"Sending To {sendto}")
        else:
            print(f"Sending To {self.email}")

if __name__ == '__main__':
    pass