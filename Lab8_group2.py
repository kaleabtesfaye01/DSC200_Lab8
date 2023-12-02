"""
Group 2 Lab8
Kaleab Alemu
Manogya Aryal

This program takes data from 2 API's and returns the result in a csv file. One of the API requires authentication
(The cat API) to access the data while the other (The dog API) does not.

It has three functions: catAPI, dogAPI and the main. The catAPI is used to access the cat API and return the data in
a csv file. The dogAPI is used to do the same as catAPI but getting the result from dog API. Finally, the main function
is used to take inout from user about which API they would like to get the dataset from. It calls the respective
function based on user's input.
"""

# Importing necessary libraries
import requests
import pandas as pd


# Defining a function called catAPI
def catAPI():

    """
    Retrieves cat images using TheCatAPI and stores the data in a CSV file.

    Data Source:
    TheCatAPI (https://thecatapi.com/) provides access to a vast collection of cat images.

    API Used:
    TheCatAPI provides various endpoints to fetch cat images. In this function, the '/images/search' endpoint is used.

    Login Credentials:
    The API_KEY variable stores the access key required to authenticate requests to TheCatAPI.

    Testing Information:
    To test this code, ensure the API_KEY variable is valid.
    """

    # Assigning the API key to a variable
    API_KEY = 'live_vLF8rPRIuD6DZwo3CgsZuxvS6EDJjsu6HjpnJ1LvoJs3nmEIqq6V8HXb7lmxC5w7'

    # Constructing the URL to fetch cat images with a limit of 10 using the Cat API
    url = f'https://api.thecatapi.com/v1/images/search?limit=10&API_KEY={API_KEY}'

    # Sending a GET request to the Cat API using the constructed URL
    data = requests.get(url)

    # Creating a Pandas DataFrame from the JSON response received from the API
    df = pd.DataFrame(data.json())

    # Setting the index of the DataFrame to the 'id' column and modifying the DataFrame in place
    df.set_index('id', inplace=True)

    # Saving the DataFrame to a CSV file named 'cat_group2.csv'
    df.to_csv('cat_group2.csv')
"""
This function extracts data (which is dog images) from Dog API we found in a public API repository in git, and outputs
the result in  a csv file. This API does not require authentication. 
"""
def dogAPI():
    api_url = 'https://dog.ceo/api/breeds/image/random/10' # this is the url for the api we are accessing.Here
    # The "/api/breeds/image/random/10" endpoint is used, and the 10 specifies the limit of dog images to retrieve.

    # Sending a GET request to the Dog API using the constructed URL
    response = requests.get(api_url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Creating a Pandas DataFrame from the JSON response received from the API
        data = response.json()
        df = pd.DataFrame(data['message'], columns=['url'])

        # Adding an 'id' column to the DataFrame
        df['id'] = df.index + 1

        # Setting the 'id' column as the index of the DataFrame
        df.set_index('id', inplace=True)

        # Saving the DataFrame to a CSV file named 'dog_group2.csv'
        df.to_csv('dog_group2.csv')
    else: # printing an error message if the url is not accessible
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")

# this is the main function that prompts user for input and returns the dataset of user's choice.
def main():
    user_choice = input("Enter what dataset you would like to access \n 1. Cat \n 2. Dogs \n: ")
    if user_choice == "1":# Calling the catAPI function to execute the code if the user chooses to get dataset from
        # CAT API
        catAPI()
    elif user_choice == "2": # Calling the dogAPI function to execute the code if the user chooses to get dataset from
        # dog API
        dogAPI()
    else: # printing an error message if a user types invalid option and calling the main function again.
        print("Invalid answer")
        main()
# Call the main function
main()






