import requests

request_history = []  # Keeps a record of the requests made during the program

##request_history.append("GET post by ID")


# Option 1 - Get a post by ID
def get_post_by_id():
    post_id = input("Enter a post ID between 1 and 100: ")  # Ask the user for a post ID

    if not post_id.isdigit():  # Check that the input is a number
        print("Invalid post ID. Please enter a number.")
        return

    post_id = int(post_id)

    if post_id < 1 or post_id > 100:  # Check that the ID is within the valid range
        print("Invalid post ID. Please enter a number between 1 and 100.")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  # Build the URL using the post ID

    response = requests.get(url)  # Send the GET request
    request_history.append(f"GET /posts/{post_id} - Status {response.status_code}")  # Save the request

    if response.status_code == 200:  # Successful request
        data = response.json()
        print("Post ID:", data["id"])
        print("Title:", data["title"])
        print("Body:", data["body"])

    elif response.status_code == 404:  # Post was not found
        print("Post not found")

    else:  # Any other response
        print("Request failed with status code:", response.status_code)


# Option 2 - Get all posts from a user
def get_posts_by_user():
    user_id = input("Enter a user ID between 1 and 10: ")  # Ask the user for a user ID

    if not user_id.isdigit():  # Check that the input is a number
        print("Invalid user ID. Please enter a number.")
        return

    user_id = int(user_id)

    if user_id < 1 or user_id > 10:  # Check that the ID is within the valid range
        print("Invalid user ID. Please enter a number between 1 and 10.")
        return

    url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint
    params = {"userId": user_id}  # Send the user ID as a query parameter

    response = requests.get(url, params=params)  # Send the GET request

    if response.status_code == 200:  # Successful request
        posts = response.json()

        for post in posts:  # Display each post returned by the API
            print("Post ID:", post["id"])
            print("Title:", post["title"])
            print()

    else:
        print("Request failed with status code:", response.status_code)


# Option 3 - Get comments for a post
def get_comments_for_post():
    post_id = input("Enter a post ID: ")  # Ask the user for a post ID

    if not post_id.isdigit():  # Check that the input is a number
        print("Invalid post ID. Please enter a number.")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"  # Build the comments URL

    response = requests.get(url)  # Send the GET request

    if response.status_code == 200:  # Successful request
        comments = response.json()

        for comment in comments:  # Display the name and email for each comment
            print("Name:", comment["name"])
            print("Email:", comment["email"])
            print()

    else:
        print("Request failed with status code:", response.status_code)


# Option 4 - Create a new post
def create_post():
    title = input("Enter a title: ")  # Ask for the post title
    body = input("Enter the post body: ")  # Ask for the post body
    user_id = input("Enter a user ID: ")  # Ask for the user ID

    if not user_id.isdigit():  # Check that the user ID is a number
        print("Invalid user ID. Please enter a number.")
        return

    data = {
        "title": title,
        "body": body,
        "userId": int(user_id)
    }  # Information sent to the API

    url = "https://jsonplaceholder.typicode.com/posts"  # API endpoint

    response = requests.post(url, json=data, timeout=10)  # Send the POST request

    if response.status_code == 201:  # POST was accepted
        result = response.json()
        print("POST successful")
        print("Post ID:", result["id"])
    else:
        print("Request failed with status code:", response.status_code)


# Option 5 - Update a post
def update_post():
    post_id = input("Enter a post ID: ")  # Ask which post will be updated
    new_title = input("Enter the new title: ")  # Ask for the new title

    if not post_id.isdigit():  # Check that the post ID is a number
        print("Invalid post ID. Please enter a number.")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  # Build the URL

    data = {
        "title": new_title
    }  # Only the title will be changed

    response = requests.patch(url, json=data, timeout=10)  # Send the PATCH request

    if response.status_code == 200:  # Update was accepted
        result = response.json()
        print("Update successful")
        print("Post ID:", result["id"])
        print("New Title:", result["title"])
    else:
        print("Request failed with status code:", response.status_code)


# Option 6 - Delete a post
def delete_post():
    post_id = input("Enter a post ID: ")  # Ask which post will be deleted

    if not post_id.isdigit():  # Check that the post ID is a number
        print("Invalid post ID. Please enter a number.")
        return

    confirm = input("Are you sure you want to delete this post? (Y/N): ")  # Confirm before sending DELETE

    if confirm.upper() != "Y":  # Cancel if the user does not confirm
        print("Delete cancelled")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"  # Build the URL

    response = requests.delete(url, timeout=10)  # Send the DELETE request

    if response.status_code == 200:  # DELETE request was accepted
        print("DELETE request accepted")
        print("The deletion is simulated by the API.")
    else:
        print("Request failed with status code:", response.status_code)


# Option 7 - Get a random programming joke
def get_random_joke():
    url = "https://v2.jokeapi.dev/joke/Programming?safe-mode"  # JokeAPI programming endpoint

    response = requests.get(url, timeout=10)  # Send the GET request

    if response.status_code == 200:  # Successful request
        joke = response.json()

        if joke["type"] == "single":  # Display a single-line joke
            print("Joke:", joke["joke"])

        elif joke["type"] == "twopart":  # Display a setup and delivery joke
            print("Setup:", joke["setup"])
            print("Delivery:", joke["delivery"])

    else:
        print("Could not get a joke. Please try again.")


# Original menu before the repeating menu and request history were added
##print("=====================================")
##print("          HTTP API EXPLORER")
##print("=====================================")
##print("1. Get a post by ID")
##print("2. Get all posts from a user")
##print("3. Get comments for a post")
##print("4. Create a new post")
##print("5. Update a post")
##print("6. Delete a post")
##print("7. Get a random joke")
##print("8. Exit")

# choice = input("Select an option: ")

# if choice == "1":
#     get_post_by_id()

# elif choice == "2":
#     get_posts_by_user()

# elif choice == "3":
#     get_comments_for_post()

# elif choice == "4":
#     create_post()

# elif choice == "5":
#     update_post()

# elif choice == "6":
#     delete_post()

# elif choice == "7":
#     get_random_joke()


# Main menu
while True:
    print("=====================================")
    print("          HTTP API EXPLORER")
    print("=====================================")
    print("1. Get a post by ID")
    print("2. Get all posts from a user")
    print("3. Get comments for a post")
    print("4. Create a new post")
    print("5. Update a post")
    print("6. Delete a post")
    print("7. Get a random joke")

    #print("8. Exit")

    print("8. View request history")
    print("9. Exit")

    choice = input("Select an option: ")  # Ask the user to select a menu option

    if choice == "1":
        get_post_by_id()

    elif choice == "2":
        get_posts_by_user()

    elif choice == "3":
        get_comments_for_post()

    elif choice == "4":
        create_post()

    elif choice == "5":
        update_post()

    elif choice == "6":
        delete_post()

    elif choice == "7":
        get_random_joke()

    # elif choice == "8":
    #     print("Goodbye!")
    #     break

    # else:
    #     print("Invalid option. Please try again.")

    # print()

    # elif choice == "8":
    #     print("Request History:")
    #     for item in request_history:
    #         print(item)

    # elif choice == "9":
    #     print("Goodbye!")
    #     break

    elif choice == "8":  # Display the requests recorded during the session
        print("Request History:")
        for item in request_history:
            print(item)

    elif choice == "9":  # End the program
        print("Goodbye!")
        break

    else:  # Handle an invalid menu option
        print("Invalid option. Please try again.")

    print()  # Add space before displaying the menu again