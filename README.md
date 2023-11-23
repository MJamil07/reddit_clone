# reddit_clone

- NOTE : Some Endpoints Don't added in docs update laterly
-  Below Information is Basic Endpoint Details and more features are updated upcoming commits...

### 1. Authenticator 

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

___

### 2. Subreddit


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


____

### 3. Post


### Endpoints:

#### `POST /api/create_post/`
- **Description:** Creates a new post.
- **Payload:** 
  - `title`: Title of the post
  - `content`: Content of the post
  - `link`: Optional link associated with the post
  - `image`: Image file (if applicable)
  - `video`: Video file (if applicable)
  - `subreddit`: ID of the subreddit the post belongs to (optional)
  - `interest`: Interest related to the post (optional)
- **Returns:** 
  - Success: Status Code `201 Created`, Success message
  - Failure: Status Code `403 Forbidden`, `404 Not Found`, `500 Internal Server Error`, Error message details

#### `DELETE /api/delete_post/<post_id>/`
- **Description:** Deletes a post by its ID.
- **Returns:** 
  - Success: Status Code `204 No Content`
  - Failure: Status Code `403 Forbidden`, `404 Not Found`, `500 Internal Server Error`, Error message details

#### `GET /api/list_post/`
- **Description:** Lists recent posts from user followers, followed users, and subscribed communities.
- **Returns:** 
  - Success: Status Code `200 OK`, List of recent posts
  - Failure: Status Code `500 Internal Server Error`, Error message details

#### `POST /api/create_upvote/`
- **Description:** Creates an upvote for a post.
- **Payload:** `post`: ID of the post to upvote
- **Returns:** 
  - Success: Status Code `201 Created`, Success message
  - Failure: Status Code `500 Internal Server Error`, Error message details

#### `POST /api/create_downvote/`
- **Description:** Creates a downvote for a post.
- **Payload:** `post`: ID of the post to downvote
- **Returns:** 
  - Success: Status Code `201 Created`, Success message
  - Failure: Status Code `400 Bad Request`, `500 Internal Server Error`, Error message details

The endpoints facilitate post creation, deletion, listing recent posts, and managing upvotes/downvotes for posts. Adjust descriptions based on specific requirements or additional functionality.

___

### 4. Comments


### Endpoints:

#### `POST /api/create_comment/`
- **Description:** Creates a new comment.
- **Payload:** 
  - `post`: ID of the post the comment belongs to
  - `parent_comment`: ID of the parent comment (if it's a reply to another comment)
  - `content`: Text content of the comment
- **Returns:** 
  - Success: Status Code `201 Created`, Newly created comment data
  - Failure: Status Code `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`, Error message details

#### `DELETE /api/delete_comment/<comment_id>/`
- **Description:** Deletes a comment by its ID.
- **Returns:** 
  - Success: Status Code `204 No Content`
  - Failure: Status Code `500 Internal Server Error`, Error message details

#### `PATCH /api/update_comment/<comment_id>/`
- **Description:** Updates a comment by its ID.
- **Payload:** New data for the comment
- **Returns:** 
  - Success: Status Code `200 OK`, Updated comment data
  - Failure: Status Code `500 Internal Server Error`, Error message details

#### `POST /api/upvote_comment/`
- **Description:** Upvotes a comment.
- **Payload:** `comment`: ID of the comment to upvote
- **Returns:** 
  - Success: Status Code `200 OK`, Success message
  - Failure: Status Code `404 Not Found`, `500 Internal Server Error`, Error message details

#### `POST /api/downvote_comment/`
- **Description:** Downvotes a comment.
- **Payload:** `comment`: ID of the comment to downvote
- **Returns:** 
  - Success: Status Code `200 OK`, Success message
  - Failure: Status Code `404 Not Found`, `500 Internal Server Error`, Error message details

The endpoints manage the creation, deletion, updating of comments, and handling upvotes/downvotes for comments.

___

### 5. Saved

### Endpoints:

1. **Create Saved**
   - **URL:** `/create/` [POST]
   - **Description:** Creates a Saved instance for a User, either for a Post or a Comment.
   - **Parameters:** 
     - `post` (optional): ID of the Post to save.
     - `comment` (optional): ID of the Comment to save.
   - **Behavior:**
     - Checks if either a Post ID or a Comment ID is provided.
     - Creates a Saved instance linked to the specified Post or Comment for the authenticated User.

2. **Unsaved**
   - **URL:** `/unsaved/<int:pk>/` [DELETE]
   - **Description:** Deletes a specific Saved instance by its primary key.
   - **Behavior:**
     - Deletes the Saved instance associated with the provided primary key (`pk`) if it belongs to the authenticated User.

3. **List Saved**
   - **URL:** `/list/` [GET]
   - **Description:** Retrieves a list of Saved instances for the authenticated User.
   - **Behavior:**
     - Fetches all Saved instances associated with the authenticated User.


___

### 6. My Profile


### Endpoints :

#### 1. **`follow/`**
- **Method:** POST
- **Functionality:** Creates a connection between a user and the user they want to follow.
- **Input Data:** JSON payload containing the `following_user` ID.
- **Actions:**
  - Checks if the user is trying to follow themselves.
  - Verifies if the `following_user` exists.
  - Creates a connection between the authenticated user and the specified `following_user`.
- **Response Codes:**
  - 201 Created: Connection successfully established.
  - 400 Bad Request: Unwanted connections or invalid user ID.
  - 500 Internal Server Error: Server-side errors.

#### 2. **`retrieve_followers/`**
- **Method:** GET
- **Functionality:** Retrieves a list of users who are following the authenticated user.
- **Actions:**
  - Fetches and returns a list of users following the authenticated user.
- **Response Codes:**
  - 200 OK: Successful retrieval of followers.
  - 401 Unauthorized: Authentication failure.
  - 500 Internal Server Error: Server-side errors.

#### 3. **`retrieve_followings/`**
- **Method:** GET
- **Functionality:** Retrieves a list of users whom the authenticated user is following.
- **Actions:**
  - Fetches and returns a list of users the authenticated user is following.
- **Response Codes:**
  - 200 OK: Successful retrieval of followings.
  - 401 Unauthorized: Authentication failure.
  - 500 Internal Server Error: Server-side errors.

#### 4. **`unfollow/`**
- **Method:** POST
- **Functionality:** Removes the connection between the authenticated user and a specified user they followed.
- **Input Data:** JSON payload containing the `following_user` ID.
- **Actions:**
  - Checks if the `following_user` exists.
  - Deletes the connection between the authenticated user and the specified `following_user`.
- **Response Codes:**
  - 200 OK: Successfully unfollowed the user.
  - 400 Bad Request: Invalid or missing `following_user` ID.
  - 500 Internal Server Error: Server-side errors.


The users to follow/unfollow each other, retrieve followers and following users , facilitating social network-like interactions.

