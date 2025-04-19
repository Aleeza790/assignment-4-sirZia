import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
   
    if email in stored_logins:  
        stored_hash = stored_logins[email]  
        return stored_hash == hash_password(password_to_check)  
    return False  

def main():
    stored_logins = {
        "user@example.com": hash_password("securepassword123"),
        "Tooba@dev.com": hash_password("mypassword"),
    }

 
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful! ✅")
    else:
        print("Login failed! ❌ Incorrect email or password.")

if __name__ == '__main__':
    main()