import subprocess
profile = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

names = [line.split(":")[1].strip()
         for line in profile
         if "All User Profile" in line]
for i, n in enumerate(names, start=1):
    print(f"{i}. {n}")
ch = input("Enter the number of the Wi-Fi profile to view the password: ")
wifi = names[int(ch) - 1]
results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
print("\n" + "\n".join(results))

