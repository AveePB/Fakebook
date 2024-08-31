# Authentication Application
Its role is to validate and generate ***Json Web Tokens*** known as the  JWTs. This application allows to restrict access to certain functionalities offered by the platform. This documentation contains the most important information about the ***API***.

## Table of contents
1. Endpoints:
    - [Signup Endpoint (GET)](#signup_get)
    - [Signup Endpoint (POST)](#signup_post)
    - [Login Endpoint (GET)](#login_get)
    - [Login Endpoint (POST)](#login_post)
    
## Signup Endpoint (/auth/signup) GET <a name="signup_get"></a>
#### Description
- The Signup Endpoint is responsible for returning the HTML page to the user.

#### Status Codes:
- **200**: successfully returned the web page;
- **404**: web page was not found;


## Signup Endpoint (/auth/signup) POST <a name="signup_post"></a>
#### Description
- The Signup Endpoint is responsible for creating new user accounts.

#### Status Codes:
- **204**: successfully created a user account;
- **400**: bad request, unable to process;
- **409**: username is already taken;

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

## User Model <a name="user_model"></a>
- Stores basic information used to authenticate a client.

#### Fields
- **username**: unique account name;
- **password**: secret sequence of chars; 