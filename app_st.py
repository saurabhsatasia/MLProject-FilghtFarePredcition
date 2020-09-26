import numpy as np
import pandas as pd
import pickle
import streamlit as st
import datetime

from PIL import Image

pickle_input = open('flight_rf.pkl', 'rb')
classifier = pickle.load(pickle_input)

def price_pred(Total_Stops,Journey_day,Journey_month,Dep_hour,Dep_minute,Arrival_hour,Arrival_minute,
               dur_hour,dur_min,Air_India,GoAir,IndiGo,Multiple_carriers,Multiple_carriers_Premium_economy,
               SpiceJet,Trujet,Vistara,Vistara_Premium_economy,Source_Chennai,Source_Delhi,Source_Kolkata,
               Source_Mumbai,Destination_Cochin,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata,
               Destination_New_Delhi):
    prediction = classifier.predict([[Total_Stops,Journey_day,Journey_month,Dep_hour,Dep_minute,Arrival_hour,Arrival_minute,
               dur_hour,dur_min,Air_India,GoAir,IndiGo,Multiple_carriers,Multiple_carriers_Premium_economy,
               SpiceJet,Trujet,Vistara,Vistara_Premium_economy,Source_Chennai,Source_Delhi,Source_Kolkata,
               Source_Mumbai,Destination_Cochin,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata,
               Destination_New_Delhi]])
    print(prediction)
    return prediction



def main():
    st.title("Fight Fare Prediction")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Fight Price Prediction ML App </h2>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    Source = st.selectbox("Source", ('Select Here','Delhi', 'Kolkata', 'Mumbai', 'Chennai', 'Bangalore'), key=None)
    Destination = st.selectbox("Destination", ('New Delhi', 'Bangalore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad'), key=None)
    Airline = st.selectbox("Airline", ('IndiGo', 'Air India', 'SpiceJet', 'Vistara',
                           'Multiple carriers Premium economy', 'Multiple carriers', 'GoAir',
                           'Air Asia', 'Trujet', 'Vistara Premium economy'), key=None)

    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    Departure_date = st.date_input('Deptarture date')
    Journey_day = int(pd.to_datetime(Departure_date, format="%Y/%m/%d").day)
    Journey_month = int(pd.to_datetime(Departure_date, format="%Y/%m/%d").month)

    Departure_time = st.time_input('Departure time')
    Dep_hour = Departure_time.hour
    Dep_minute = Departure_time.minute

    Arrival_time = st.time_input('Arrival time')
    Arrival_hour = Arrival_time.hour
    Arrival_minute = Arrival_time.minute

    # Duration
    dur_hour = abs(Arrival_hour - Dep_hour)
    dur_min = abs(Arrival_minute - Dep_minute)
    Duration = st.write("Duration", str(dur_hour)+":"+str(dur_min))

    # Total_Stops
    Total_Stops = st.selectbox('Total stops', (0,1,2,3,4))


    if (Source == 'Delhi'):
        Source_Delhi = 1
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0

    elif (Source == 'Kolkata'):
        Source_Delhi = 0
        Source_Kolkata = 1
        Source_Mumbai = 0
        Source_Chennai = 0

    elif (Source == 'Mumbai'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 1
        Source_Chennai = 0

    elif (Source == 'Chennai'):
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 1

    else:
        Source_Delhi = 0
        Source_Kolkata = 0
        Source_Mumbai = 0
        Source_Chennai = 0


    if (Source == 'Cochin'):
        Destination_Cochin = 1
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0

    elif (Source == 'Delhi'):
        Destination_Cochin = 0
        Destination_Delhi = 1
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0

    elif (Source == 'New_Delhi'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 1
        Destination_Hyderabad = 0
        Destination_Kolkata = 0

    elif (Source == 'Hyderabad'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 1
        Destination_Kolkata = 0

    elif (Source == 'Kolkata'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 1

    else:
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_New_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0


    if (Airline == 'IndiGo'):
        IndiGo = 1
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'Air India'):
        IndiGo = 0
        Air_India = 1
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'Multiple carriers'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 1
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'SpiceJet'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 1
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'Vistara'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 1
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'GoAir'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 1
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'Multiple carriers Premium economy'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 1
        Vistara_Premium_economy = 0
        Trujet = 0

    elif (Airline == 'Vistara Premium economy'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 1
        Trujet = 0

    elif (Airline == 'Trujet'):
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 1

    else:
        IndiGo = 0
        Air_India = 0
        Multiple_carriers = 0
        SpiceJet = 0
        Vistara = 0
        GoAir = 0
        Multiple_carriers_Premium_economy = 0
        Vistara_Premium_economy = 0
        Trujet = 0

    rounded_result = ""
    if st.button("Predict"):
        result=price_pred(Total_Stops,Journey_day,Journey_month,Dep_hour,Dep_minute,Arrival_hour,Arrival_minute,
               dur_hour,dur_min,Air_India,GoAir,IndiGo,Multiple_carriers,Multiple_carriers_Premium_economy,
               SpiceJet,Trujet,Vistara,Vistara_Premium_economy,Source_Chennai,Source_Delhi,Source_Kolkata,
               Source_Mumbai,Destination_Cochin,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata,
               Destination_New_Delhi)
        rounded_result = round(result[0], 2)

    st.success("The Flight Fare Prediction is : Rs.{}".format(rounded_result))


if __name__ == '__main__':
    main()




