# Fakebook Project

Fakebook is a social media platform that mimics a mix of Facebook and Messenger. It provides users with various functionalities, including a messaging system, friend system, notification system, profile customization, and robust authorization and authentication mechanisms.

## Features

### 1. Messaging System
- **Real-Time Chat**: Users can engage in real-time conversations with friends.
- **Message History**: Access to previous messages for ongoing chats.
- **Message Notifications**: Users receive notifications for new messages.

### 2. Friend System
- **Send Friend Requests**: Users can send and receive friend requests.
- **Friend Management**: Users can view their friends list and manage friend relationships.
- **Friend Suggestions**: Recommendations for potential friends based on mutual connections.

### 3. Notification System
- **Activity Alerts**: Users receive notifications for various activities (e.g., friend requests, messages).
- **Centralized Notification Feed**: All notifications can be viewed in a single feed.

### 4. Profile Customization
- **Profile Information**: Users can update their avatar, background image, bio, and other personal details.
- **Privacy Settings**: Options to control who can see specific parts of their profile.

### 5. Authorization and Authentication
- **Secure Login**: Users can log in securely using email and password.
- **User Registration**: New users can create an account with email verification.
- **Session Management**: Users remain logged in across sessions with secure cookies.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (with frameworks as needed)
- **Backend**: Django for server-side logic
- **Database**: PostgreSQL (or any other suitable database)
- **Real-Time Communication**: WebSockets (for messaging)

## Usage
1. **Creating an Account**:
   - Click on the "Sign Up" button on the homepage.
   - Fill in the required fields, including your email, username, and password.
   - Confirm your email through the verification link sent to your inbox.

2. **Logging In**:
   - Click on the "Log In" button.
   - Enter your registered email and password.
   - Click "Submit" to access your dashboard.

3. **Navigating the Dashboard**:
   - View your friend list on the left column.
   - Click on a friend's name to open a chat in the right column.
   - Use the input box at the bottom of the chat to send messages.

4. **Sending Friend Requests**:
   - Browse through potential friends in the friend suggestions section.
   - Click the "Add Friend" button next to a user's profile.

5. **Managing Notifications**:
   - Access notifications from the bell icon in the top navigation bar.
   - Click on notifications to view details and take actions (e.g., accept friend requests).

6. **Customizing Your Profile**:
   - Go to your profile settings from the top navigation menu.
   - Update your avatar, background image, and bio to personalize your profile.
   - 
### Prerequisites
- Python 3.x
- Django
- MySQL

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/AveePB/fakebook.git
   cd fakebook

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### MIT License Summary
The MIT License is a permissive free software license that allows for software reuse within proprietary software under certain conditions. It is a simple and easy-to-understand license that is widely used in open-source projects. It permits users to:
- Use the software for any purpose.
- Modify the software and distribute modified versions.
- Distribute copies of the original software.

However, the original license must be included in all copies or substantial portions of the software, and there is no warranty provided for the software.


