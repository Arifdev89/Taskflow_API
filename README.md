# ✅ TaskFlow API

A RESTful Task Management API built with Django REST Framework. It works as a backend for any task manager application where users can register, login, and manage their tasks with full CRUD operations, JWT authentication, and role-based access control.

## What It Does

Users can register and login to get a JWT token. Using that token they can create, view, update, and delete their own tasks. Each task has a title, description, priority, status, and due date. Admin users can view all users and all tasks.

## Features

- User registration and login with JWT authentication
- Create, read, update, delete tasks
- Update task status — To Do, In Progress, Completed, Cancelled
- Filter tasks by status and priority
- Search tasks by title or description
- Pagination and sorting support
- Role-based permissions — Admin and Normal User
- Task summary — total, pending, completed count
- All endpoints tested with Postman

## Tech Used

- **Backend:** Python, Django, Django REST Framework
- **Auth:** JWT (djangorestframework-simplejwt)
- **Database:** SQLite
- **Testing:** Postman


