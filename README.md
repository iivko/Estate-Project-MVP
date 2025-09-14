# 🚀 Estate Project

This project is focused on building a full-stack estate management system using Django and React.

The reason for this project is to explore new techologies and build a MVP.

---

## ⚙️ Tech Stack
- Backend: Django
- Frontend: React


---

## 📜 API Documentation

### Auth Endpoints

Register User
```http
POST http://localhost:8080/api/v1/auth/users/

{
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "password": "",
    "re_password": ""
}
```

Activate User
```http
POST http://localhost:8080/api/v1/auth/users/activation/

{
    "uid": "",
    "token": ""
}
```

Login User
```http
POST http://localhost:8080/api/v1/auth/login/

{
    "email": "",
    "password": ""
}
```

Currently Logged User
```http
GET http://localhost:8080/api/v1/auth/users/me/
```

Refresh JWT
```http
POST http://localhost:8080/api/v1/auth/refresh/
```

Reset User Password
```http
POST http://localhost:8080/api/v1/auth/users/reset_password/

{
    "email": ""
}
```

Reset User Password Confirmation
```http
POST http://localhost:8080/api/v1/auth/users/reset_password_confirm/

{
    "uid": "",
    "token": "",
    "new_password": "",
    "re_new_password": ""
}
```

Logout User
```http
POST http://localhost:8080/api/v1/auth/logout/
```
---

