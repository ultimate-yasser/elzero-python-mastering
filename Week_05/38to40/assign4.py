username, domain = input("What's ur email? ").strip().lower().split("@")
website, main = domain.split(".")
print(f"Your name is {username.title()}")
print(f"Email Service Provider is {website}")
print(f"Top Level Domain Is {main}")