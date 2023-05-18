### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing? 
   A standard style of laying out an API's various.  Following this standard makes the purpose and use of the routes easier for users and developers to understand.

- What is a resource?
    A resource is the object that the API routes pull. For example, if you are pulling a list of users, the list is the resource. 

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
    The API is only meant to return requested API data in the form of JSON.  Data is only posted through the data included in the route.  If you wanted to post data to an API through a form, you would build a front-end with the form, and then on submit you would take that form data and format it into a proper API request (which could either be done by sending the request directly from the front-end or sending the data to the back-end server to make the request from there)

- What does idempotent mean? Which HTTP verbs are idempotent?
    Idempotent is a request that, no matter how many times that exact same request is made, will always yield the same result.  Idempotent verbs include Get, Put/Patch, and Delete, since if you make requests with those verbs using the same data over and over, the results will always be the same. 

- What is the difference between PUT and PATCH?
    PUT sends and updates all the information on a resource, so PUT request data looks the same as POST request data.  A PATCH request only updates part of the data.  For example, if you have a user with a username, password, and email, and wanted to update the email, a PUT request would still send the username, password, and email, even if the username and password being sent are the same.  A PATCH request would only send the email.

- What is one way encryption?
    It is when you run data through the encryption function and the result cannot be reversed. 

- What is the purpose of a `salt` when hashing a password?
    It adds a random string to the password before hashing, so that if two people are using the same password, the hashed results remain different. 

- What is the purpose of the Bcrypt module?
    It is an effective module for salting and hashing passwords.

- What is the difference between authorization and authentication?
    Authenticating is for confirming who the user is, while authorization confirms what that user has access to. So when a user signs in, they are authenticated, but a user might need special authorization to see certain parts of a another user's data.
