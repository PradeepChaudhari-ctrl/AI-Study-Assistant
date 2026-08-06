from app.auth.security import hash_password, verify_password

password = "OpenAI@123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print("Verify :", verify_password(password, hashed))
