
# Using True
is_student_allowed = True
if is_student_allowed:
    print("Student is allowed to attend the class.")
else:
    print("Student is not allowed to attend the class.")

# Using bytes
message = b"Hello, World!"
print(type(message))
print(message)
print(len(message))

# Converting True to bytes and appending it to message
is_allowed_access = True
message_with_permission = b"\x01" + bytearray([int(i) for i in [int(str(x)[0]) for x in list(str(bool(is_allowed_access)))][::-1]) if i else b'\x00' ] 
print("Message with permission: ", message_with_permission)
