# Authentication Application

## Table of Contents
- [Login Endpoint (`/authz/login/`)](#authzlogin)
  - [GET Request](#get-request)
  - [POST Request](#post-request)
- [Register Endpoint (`/authz/register/`)](#authzregister)
  - [GET Request](#get-request-1)
  - [POST Request](#post-request-1)

## `/authz/login/`

### GET Request
**Description**: Renders the login page.

**Response**:
- **Status Code**: `200 OK`
- **Content**: The login HTML page.

### POST Request
**Description**: Authenticates a user and returns authentication tokens.

**Request Body** (Form data):
- `username`: The user's username.
- `password`: The user's password.

**Response**:
- **Success**:
  - **Status Code**: `200 OK`
  - **Content**:
    ```json
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```
  - **Meaning**: Provides `refresh` and `access` tokens for authenticated access.

- **Failure**:
  - **Status Code**: `400 Bad Request`
    - **Content**:
      ```json
      {
        "error": "Form is invalid"
      }
      ```
    - **Meaning**: Missing `username` or `password`, or invalid format.

    - **Content**:
      ```json
      {
        "error": "Username doesn't meet the criteria"
      }
      ```
    - **Meaning**: `username` must be alphanumeric and between 6 and 32 characters.

    - **Content**:
      ```json
      {
        "error": "Password doesn't meet the criteria"
      }
      ```
    - **Meaning**: `password` must be between 6 and 32 characters.

  - **Status Code**: `401 Unauthorized`
    - **Content**:
      ```json
      {
        "error": "Invalid credentials"
      }
      ```
    - **Meaning**: Authentication failed due to incorrect `username` or `password`.

## `/authz/register/`

### GET Request
**Description**: Renders the registration page.

**Response**:
- **Status Code**: `200 OK`
- **Content**: The registration HTML page.

### POST Request
**Description**: Registers a new user and returns authentication tokens.

**Request Body** (Form data):
- `username`: The desired username for the new user.
- `password`: The desired password for the new user.

**Response**:
- **Success**:
  - **Status Code**: `200 OK`
  - **Content**:
    ```json
    {
      "refresh": "<refresh_token>",
      "access": "<access_token>"
    }
    ```
  - **Meaning**: User successfully registered; provides `refresh` and `access` tokens.

- **Failure**:
  - **Status Code**: `400 Bad Request`
    - **Content**:
      ```json
      {
        "error": "Form is invalid"
      }
      ```
    - **Meaning**: Missing `username` or `password`, or invalid format.

    - **Content**:
      ```json
      {
        "error": "Username doesn't meet the criteria"
      }
      ```
    - **Meaning**: `username` must be alphanumeric and between 6 and 32 characters.

    - **Content**:
      ```json
      {
        "error": "Password doesn't meet the criteria"
      }
      ```
    - **Meaning**: `password` must be between 6 and 32 characters.

  - **Status Code**: `409 Conflict`
    - **Content**:
      ```json
      {
        "error": "User already exists"
      }
      ```
    - **Meaning**: Username already taken; cannot register the user.
