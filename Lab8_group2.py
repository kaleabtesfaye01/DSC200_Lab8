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


# Calling the catAPI function to execute the code
catAPI()
