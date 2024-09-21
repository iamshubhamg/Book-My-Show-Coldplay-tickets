from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EVENT_URL = "https://in.bookmyshow.com/events/coldplay-music-of-the-spheres-world-tour/ET00412466"

ticket_info = {
    "Standing (Floor)": 6450,
    "Level 1 - E & L": 3500,
    "Level 1 - A & P": 4000,
    "Level 1 - B, C, D, M, N & O": 4500,
    "Level 2 - E & L": 9000,
    "Level 2 - A & P": 9500,
    "Level 2 - B, C, D, M, N & O": 12500,
    "Level 3 - E & L": 2500,
    "Level 3 - A & P": 3000,
    "Level 3 - B, C, D, M, N & O": 3500,
    "Lounge": 35000
}

payment_modes = {
    "1": "Credit/Debit Card",
    "2": "Net Banking",
    "3": "Gift Voucher",
    "4": "UPI",
    "5": "LazyPay"
}

def get_user_input():
    print("Welcome to the ticket booking system for Coldplay's 'Music of the Spheres' concert!")
    print("We will help you book your tickets for the event at D Y Patil Stadium, Mumbai on 18 & 19 January 2025.")
    print("\nAvailable ticket levels: ")
    for key in ticket_info.keys():
        print(f"{key}: ₹{ticket_info[key]}")
    level = input("Enter the ticket level you want: ")
    num_tickets = int(input("Enter the number of tickets: "))
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    print("\nAvailable Payment Methods:")
    for key, method in payment_modes.items():
        print(f"{key}: {method}")
    payment_mode_choice = input("Enter the number corresponding to your preferred payment method: ")
    payment_mode = payment_modes.get(payment_mode_choice)
    return level, num_tickets, name, email, payment_mode

def automate_ticket_booking(level, num_tickets, name, email, payment_mode):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')
    driver.get(EVENT_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "some_selector_for_tickets_section")))
    ticket_selector = driver.find_element(By.XPATH, f"//button[contains(text(), '{level}')]")
    ticket_selector.click()
    time.sleep(1)
    ticket_input = driver.find_element(By.ID, "ticket_quantity_input_id")
    ticket_input.clear()
    ticket_input.send_keys(str(num_tickets))
    name_input = driver.find_element(By.ID, "name_input_id")
    name_input.send_keys(name)
    email_input = driver.find_element(By.ID, "email_input_id")
    email_input.send_keys(email)
    if payment_mode == "Credit/Debit Card":
        card_selector = driver.find_element(By.ID, "payment_credit_debit_id")
        card_selector.click()
    elif payment_mode == "Net Banking":
        netbanking_selector = driver.find_element(By.ID, "payment_netbanking_id")
        netbanking_selector.click()
    elif payment_mode == "Gift Voucher":
        giftvoucher_selector = driver.find_element(By.ID, "payment_giftvoucher_id")
        giftvoucher_selector.click()
    elif payment_mode == "UPI":
        upi_selector = driver.find_element(By.ID, "payment_upi_id")
        upi_selector.click()
    elif payment_mode == "LazyPay":
        lazypay_selector = driver.find_element(By.ID, "payment_lazypay_id")
        lazypay_selector.click()
    submit_button = driver.find_element(By.ID, "submit_button_id")
    submit_button.click()
    print(f"Thank you {name}, you are now being redirected to the {payment_mode} payment gateway for Coldplay's concert ticket booking.")
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    level, num_tickets, name, email, payment_mode = get_user_input()
    automate_ticket_booking(level, num_tickets, name, email, payment_mode)
