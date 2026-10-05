def login(email: str, password: str) -> dict:
    if email and password:
        return {"token": "jwt-token-sample", "status": 200}
    return {"error": "Unauthorized", "status": 401}
