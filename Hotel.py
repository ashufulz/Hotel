# Hotel Name

from selenium import webdriver
import time, smtplib
import datetime

now = datetime.datetime.now()
today = now.strftime("%d%b-%H%M")

start = input("Check-in(dd-mm-yyyy): ")             # Getting checkin & checkout dates as per user
end = input("Check-out(dd-mm-yyyy): ")

checkin = start.replace('-', '%2F')                 # Replacing string elements according to URL conventions
checkout = end.replace('-', '%2F')

driver = webdriver.Chrome()

# Properly check the URL; you can directly change no. of guests/rooms as you need!
URL = 'https://www.oyorooms.com/79954-oyo-rooms-oyo-49759-hotel-qubic-mumbai/?checkin='+checkin+'&checkout='+checkout+'&rooms=1&guests=2&rooms_config=1-2_0&selected_rcid=11'
driver.get(URL)
time.sleep(5)                       # Gives some time to load the page completely, value varies on your internet connection
driver.minimize_window()            # Comment this line if you want to keep the window open


def final():
    cost = driver.find_element_by_class_name('listingPrice__finalPrice--black').text
    price = int(cost[1:5])              # Excluding the currency symbol, hence getting exact value we need

    if price <= 3500:                   # Value depends on your overall stay's budget
        mail()
    else:
        print(today + " - Hotel's price isn't coming down!")


def mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    if now == datetime.datetime(2020, 2, 10):               # (yyyy-mm-dd) format date; code will keep running till this date
        server.quit()

    else:
        server.login('mail-id', 'password')

        subject = "Hotel - Oyo"
        body = 'Price fell down at. Book soon!\n' \
               'Check the following link:\n' \
               + URL
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'from_mail_id',
            'to_mail_id',
            msg
        )

        print("Email Sent!")


while True:
    final()
    driver.close()
    time.sleep(3600)                        # Will run the code every hour


