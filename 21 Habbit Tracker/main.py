import requests
import datetime as dt


#------------- Set up the user account -------------#
USERNAME = # Replace with your username
TOKEN = # Replace with your token

user_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(user_endpoint, json=user_params)
# print(response.text)


#------------- Create Graph -------------#
graph_endpoint = f"{user_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Walking",
    "unit": "Steps",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


#------------- Post the value to the graph -------------#
today_date = dt.datetime.now()
today_date = today_date.strftime("%Y%m%d")

put_endpoint = f"{user_endpoint}/{USERNAME}/graphs/graph1"

put_params = {
    'date': today_date,
    'quantity': str(input("How many steps did you walk today? ")),
}

# response = requests.post(put_endpoint, json=put_params, headers=headers)
# print(response.text)


#------------- Update graph -------------#
update_endpoint = f"{user_endpoint}/{USERNAME}/graphs/graph1/{today_date}"

updated_data = {
    'quantity': str(input("How many steps did you walk today? ")),
}

# response = requests.post(update_endpoint, json=updated_data, headers=headers)
# print(response.text)

#------------- Delete pixel -------------#
pixel_date = "20230710"
delete_endpoint = f"{user_endpoint}/{USERNAME}/graphs/graph1/{pixel_date}"

response = requests.delete(delete_endpoint, headers=headers)
