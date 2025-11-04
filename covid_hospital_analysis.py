import pandas as pd
import matplotlib.pyplot as plt
import requests

#make an http get requests to fetch data from the covid-19 statistics
api_url ="https://api.rootnet.in/covid19-in/hospitals/beds"
response = requests.get(api_url)

#check if the request was successful (status code 200)
if response.status_code ==200:
 #parse the jason response code to extract the required data
    data = response.json()
    if 'data' in data and 'regional' in data ['data']:
        regional_data= data['data']['regional']
        
        #create a dataframe from the summary data
        df= pd.DataFrame(regional_data)
        
        #bar plot with total total beds available in states
        plt.figure(figsize=(12, 6))
        plt.plot(df['state'], df['urbanHospitals'], color='skyblue',marker = "o")
        plt.xticks(rotation=90)  #rotate x-axis labels for better readability
        
        #adding title to theplot
        plt.title("Available urbanHospitals by state in India")
        
        
        #setting the x and y labels
        plt.xlabel('available urbanHospitals')
        plt.ylabel('state')
        
        #plt.tight_layout()
        plt.show()
    else:
        print("Data structure is not as expected in the API response.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
