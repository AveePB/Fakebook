# Authentication Application

## `/authz/login/`

### GET Request

- **Description**: Returns the login page for the user.
- **Response**: Renders the `login.html` template.

### POST Request

- **Description**: Authenticates a user with the provided username and password.
- **Request Body**: 
  - `username` (string): The username of the user.
  - `password` (string): The password of the user.
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "token": "access_token_here"
    }
    ```
    - **Description**: Returns a JWT token if credentials are valid.
  - **Client Error (400 Bad Request)**:
    ```json
    {
      "error": "Form is invalid"
    }
    ```
    - **Description**: Returned if either username or password is missing.
    ```json
    {
      "error": "Username doesn't meet the criteria"
    }
    ```
    - **Description**: Returned if the username is not alphanumeric or exceeds 32 characters.
    ```json
    {
      "error": "Password doesn't meet the criteria"
    }
    ```
    - **Description**: Returned if the password is shorter than 6 characters or longer than 32 characters.
  - **Unauthorized (401 Unauthorized)**:
    ```json
    {
      "error": "Invalid credentials"
    }
    ```
    - **Description**: Returned if the credentials are incorrect.

## `/authz/register/`

### GET Request

- **Description**: Returns the registration page for the user.
- **Response**: Renders the `register.html` template.

### POST Request

- **Description**: Registers a new user with the provided username and password.
- **Request Body**:
  - `username` (string): The username of the new user.
  - `password` (string): The password of the new user.
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
      "message": "User successfully created"
    }
    ```
    - **Description**: Returned when a new user is successfully created.
  - **Client Error (400 Bad Request)**:
    ```json
    {
      "error": "Form is invalid"
    }
    ```
    - **Description**: Returned if either username or password is missing.
    ```json
    {
      "error": "Username doesn't meet the criteria"
    }
    ```
    - **Description**: Returned if the username is not alphanumeric or exceeds 32 characters.
    ```json
    {
      "error": "Password doesn't meet the criteria"
    }
    ```
    - **Description**: Returned if the password is shorter than 6 characters or longer than 32 characters.
  - **Conflict (409 Conflict)**:
    ```json
    {
      "error": "User already exists"
    }
    ```
    - **Description**: Returned if the username is already taken.
