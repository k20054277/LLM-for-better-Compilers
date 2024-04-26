def validate_password(username, password):
    if username == "admin" and password == "secret":
        return True
    else:
        return False