# Authentication Application
Its role is to validate and generate ***Json Web Tokens*** known as the  JWTs. This application allows to restrict access to certain functionalities offered by the platform. This documentation contains the most important information about the ***API***.

## Table of contents
1. Endpoints:
    - [Registration Endpoint (GET)](#register_get)
    - [Registration Endpoint (POST)](#register_post)
    - [Login Endpoint (GET)](#login_get)
    - [Login Endpoint (POST)](#login_post)
2. Database Models:
    - [User Model](#user_model)
    - [Token Model](#token_model)
3. User Service:
    - ...
4. Token Service:
    - ...
    
## Registration Endpoint (/auth/register) GET <a name="register_get"></a>
#### Description
- The Registration Endpoint is responsible for returning the HTML page to the user.

#### Status Codes:
- **200**: successfully returned the web page;
- **404**: web page was not found;


## Registration Endpoint (/auth/register) POST <a name="register_post"></a>
#### Description
- The Registration Endpoint is responsible for creating new user accounts.

#### Status Codes:
- **204**: successfully created a user account;
- **400**: bad request, unable to process;
- **409**: could not create a user account;

## Login Endpoint (/auth/login) GET <a name="login_get"></a>
- The Login Endpoint is responsible for returning the HTML page to the user.

#### Status Codes:
- **200**: successfully returned the web page;
- **404**: web page was not found;

## Login Endpoint (/auth/login) POST <a name="login_post"></a>
- The Login Endpoint is responsible for authenticating the user credentials.

#### Status Codes:
- **200**: successfully logged in, fetched a JWT;
- **400**: bad request, unable to process;
- **404**: invalid credentials;