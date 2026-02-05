import time

password = "admin123"
attempts = ["1234", "password", "admin", "admin123"]

for attempt in attempts:
    print(f"Trying: {attempt}")
    time.sleep(1)

    if attempt == password:
        print("Password Cracked!")
        break
else:
    print("Bruteforce Failed")
