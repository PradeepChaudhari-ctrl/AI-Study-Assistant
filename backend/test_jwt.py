from app.auth.jwt import create_access_token, decode_token

token = create_access_token(
    {
        "sub": "pradeep@example.com"
    }
)

print("JWT Token:\n")
print(token)

print("\nDecoded:\n")

print(
    decode_token(token)
)