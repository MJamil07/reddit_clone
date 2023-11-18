# reddit_cloone


### Authenticator 

### Endpoints:

#### `POST /api/register/`
- **Description:** Registers a new user and creates a CustomUser profile for the registered user.
- **Parameters:** `username`, `email`, `password`, `phone_number`, `profile_photo`, `karma`, `interests`, `social_links`
- **Returns:** 
  - Success:
    - Status Code: `201 Created`
    - Response: `{ "success": true, "message": "Successfully Registered" }`
  - Failure:
    - Status Code: `400 Bad Request` or `500 Internal Server Error`
    - Response: `{ "success": false, "message": "Error message details" }`

#### `POST /api/login/`
- **Description:** Allows a registered user to log in and returns an authentication token for the user.
- **Parameters:** `username`, `password`
- **Returns:** 
  - Success:
    - Status Code: `202 Accepted`
    - Response: `{ "success": true, "token": "authentication_token" }`
  - Failure:
    - Status Code: `400 Bad Request`, `401 Unauthorized`, or `500 Internal Server Error`
    - Response: `{ "success": false, "message": "Error message details" }`

### Documents:

#### `RegisterAPIView`:
- **Description:** Allows users to register by providing necessary details and creates a new User and CustomUser profile.
- **Usage:** `POST /api/register/`
- **Payload:**
  - `username`: User's username
  - `email`: User's email address
  - `password`: User's password
  - `phone_number`: Optional user phone number
  - `profile_photo`: Optional profile photo
  - `karma`: Optional user karma
  - `interests`: Optional user interests
  - `social_links`: Optional social links
- **Response:** 
  - Successful Registration: Status Code `201 Created`, Success message
  - Registration Failure: Status Code `400 Bad Request` or `500 Internal Server Error`, Error message details

#### `LoginAPIView`:
- **Description:** Logs in an existing user and generates an authentication token for further authenticated requests.
- **Usage:** `POST /api/login/`
- **Payload:**
  - `username`: User's username
  - `password`: User's password
- **Response:** 
  - Successful Login: Status Code `202 Accepted`, Authentication token
  - Login Failure: Status Code `400 Bad Request`, `401 Unauthorized`, or `500 Internal Server Error`, Error message details

___

### Subreddit


### Endpoints:

#### `POST /api/create/`
- **Description:** Creates a new subreddit/community.
- **Payload:** 
  - `name`: Name of the subreddit
  - `about`: Description of the subreddit
  - `links`: Associated links
  - `rules`: Subreddit rules
  - `avatar`: Avatar or image for the subreddit
  - `interest`: Interests related to the subreddit
- **Returns:** 
  - Success: Status Code `201 Created`, Success message
  - Failure: Status Code `400 Bad Request` or `500 Internal Server Error`, Error message details

#### `DELETE /api/destroy/<subreddit_id>/`
- **Description:** Deletes a subreddit by its ID, allowed only for the subreddit admin.
- **Returns:** 
  - Success: Status Code `204 No Content`
  - Failure: Status Code `403 Forbidden`, `404 Not Found`, or `500 Internal Server Error`, Error message details

#### `GET /api/get_community/<subreddit_id>/`
- **Description:** Retrieves community information, including recent posts, details, and members' info (private community access is restricted).
- **Returns:** 
  - Success: Status Code `200 OK`, Subreddit details with posts and members
  - Failure: Status Code `403 Forbidden`, `404 Not Found`, or `500 Internal Server Error`, Error message details

#### `GET /api/list/`
- **Description:** Lists all communities based on the number of members.
- **Returns:** 
  - Success: Status Code `200 OK`, List of subreddits sorted by member count
  - Failure: Status Code `403 Forbidden`, `500 Internal Server Error`, Error message details

#### `POST /api/request_member/`
- **Description:** Requests to join a subreddit as a member.
- **Payload:** `subreddit_id`: ID of the subreddit to join
- **Returns:** 
  - Success: Status Code `201 Created`, Success message or if already a member, Status Code `200 OK`
  - Failure: Status Code `400 Bad Request`, `403 Forbidden`, `404 Not Found`, or `500 Internal Server Error`, Error message details

#### `POST /api/remove_member/`
- **Description:** Removes a user from a subreddit's members.
- **Payload:** `subreddit_id`: ID of the subreddit to leave
- **Returns:** 
  - Success: Status Code `201 Created`, Success message
  - Failure: Status Code `400 Bad Request`, `404 Not Found`, or `500 Internal Server Error`, Error message details

#### `GET /api/get_members/<subreddit_id>/`
- **Description:** Retrieves members of a subreddit.
- **Returns:** 
  - Success: Status Code `200 OK`, List of subreddit members
  - Failure: Status Code `404 Not Found`, `500 Internal Server Error`, Error message details

#### `GET /api/search/`
- **Description:** Searches for subreddits by name or interest.
- **Parameters:** `name`: Subreddit name or `interest`: Interest related to the subreddit
- **Returns:** 
  - Success: Status Code `200 OK`, List of subreddits matching the search criteria
  - Failure: Status Code `500 Internal Server Error`, Error message details

These endpoints enable subreddit creation, deletion, member management, and information retrieval based on various criteria.

Adjust the descriptions as per additional functionality or specific requirements.

____

### Post
