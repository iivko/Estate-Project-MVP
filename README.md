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

### Google Oauth Login

Google Authorization URL
```http
POST http://localhost:8080/api/v1/auth/o/google-oauth2/

params: 
    redirect_uri: "http://localhost:8080/api/v1/auth/google"
```

Login With Google
```http
POST http://localhost:8080/api/v1/auth/o/google-oauth2/

params: 
    state: ""
    code: ""

Headers: 
    Content-Type: application/x-www-form-urlencoded
```

### Profile Endpoints

My Profile
```http
GET http://localhost:8080/api/v1/profiles/user/my-profile/
```

Update Profile
```http
PATCH http://localhost:8080/api/v1/profiles/user/update/

{
    "first_name": "",
    "last_name": "",
    "username": "",
    "bio": "",
    "occupation": "",
    "phone_number": "+359",
    "country_of_origin": "Bulgaria",
    "city_of_origin": "Kazanluk"
}
```

Upload Avatar
```http
PATCH http://localhost:8080/api/v1/profiles/user/avatar/
```

All Profiles
```http
GET http://localhost:8080/api/v1/profiles/all/
```

All Technician Profiles
```http
GET http://localhost:8080/api/v1/profiles/non-tenant-profiles/
```

### Apartment Endpoints

Add Apartment
```http
POST http://localhost:8080/api/v1/apartments/add/

{
    "unit_number": "",
    "building": "",
    "floor": 1
}
```

Apartment Details
```http
GET http://localhost:8080/api/v1/apartments/my-apartment/
```

### Issue Endpoints

Create Issue
```http
POST http://localhost:8080/api/v1/issues/create/<uuid:apartment_id>/

{
    "title": "",
    "description": "",
    "status": "",
    "priority": ""
}
```

Issue Details
```http
GET http://localhost:8080/api/v1/issues/<uuid:issue_id>/
```

Update Issue
```http
PATCH http://localhost:8080/api/v1/issues/<uuid:issue_id>/

{
    "title": "",
    "description": "",
    "status": "",
    "priority": ""
}
```

Delete Issue
```http
DELETE http://localhost:8080/api/v1/issues/<uuid:issue_id>/
```

All Reported Issues
```http
GET http://localhost:8080/api/v1/issues/
```

My Issues
```http
GET http://localhost:8080/api/v1/issues/me/
```

### Report Endpoints

Create Report
```http
POST http://localhost:8080/api/v1/reports/create/

{
    "title": "",
    "description": "",
    "reported_user_username": ""
}
```

My Reports
```http
GET http://localhost:8080/api/v1/reports/me/
```

### Rating Endpoints

Add User Rating
```http
POST http://localhost:8080/api/v1/ratings/create/

{
    "rated_user_username": "",
    "rating": 3,
    "comment": ""
}
```

### Post Endpoints

Create Post
```http
POST http://localhost:8080/api/v1/posts/create/

{
    "title": "",
    "tags": ["One", "Two", "Three"],
    "body": ""
}
```

My Posts
```http
GET http://localhost:8080/api/v1/posts/my-posts/
```

Update Post
```http
PATCH http://localhost:8080/api/v1/posts/<slug:slug>/update/

{
    "title": "",
    "tags": ["One", "Three"],
    "body": ""
}
```

Get All Posts
```http
GET http://localhost:8080/api/v1/posts/
```

Get Single Post
```http
GET http://localhost:8080/api/v1/posts/<slug:slug>/
```

Upvote Post
```http
POST http://localhost:8080/api/v1/posts/<uuid:post_id>/upvote/
```

Downvote Post
```http
POST http://localhost:8080/api/v1/posts/<uuid:post_id>/downvote/
```

Bookmark Post
```http
POST http://localhost:8080/api/v1/posts/<slug:slug>/bookmark/
```

Un Bookmark Post
```http
POST http://localhost:8080/api/v1/posts/<slug:slug>/unbookmark/
```

All Bookmarked Posts
```http
GET http://localhost:8080/api/v1/posts/bookmarked/
```

Add Reply To Post
```http
POST http://localhost:8080/api/v1/posts/<uuid:post_id>/reply/

{
    "body": ""
}
```

All Replies Of A Post
```http
GET http://localhost:8080/api/v1/posts/<uuid:post_id>/replies/
```

Get Popular Tags
```http
GET http://localhost:8080/api/v1/posts/popular-tags/
```

Get Top Posts
```http
GET http://localhost:8080/api/v1/posts/top-posts/
```

Get Posts By Tag
```http
GET http://localhost:8080/api/v1/posts/tags/<str:tag_slug>/
```

---

