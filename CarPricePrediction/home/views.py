from django.shortcuts import render,HttpResponse
import pickle

model  =pickle.load(open('model.pkl','rb'))

# Create your views here.
def index(requests):
    ans =0
    context ={
            'ans':ans,
            'flag':False
        }
    if requests.method =='POST':
        year = requests.POST['year']
        Kilometers_Driven =requests.POST['Kilometers_Driven']

        transmission =requests.POST['transmission']
        if transmission == 'manual':
            transmission =0
        else:
            transmission =1

        owner =requests.POST['owner']
        if owner == 'First':
            owner =0
        elif owner =='Second':
            owner =1
        elif owner =='Third':
            owner =2
        else:
            owner =3

        Seats =requests.POST['Seats']
        Mileage  =requests.POST['Mileage']
        Power =requests.POST['Power']
        Engine =requests.POST['Engine']

        Location =requests.POST['Location']
        

        if Location =='Bangalore':
            Location_Bangalore =1
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif Location =='Chennai':
            Location_Bangalore =0
            Location_Chennai =1
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif Location =='Coimbatore':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=1
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0    
        elif Location =='Delhi':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=1
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0   
        elif Location =='Hyderabad':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=1
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif Location =='Jaipur':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=1
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif Location =='Kochi':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=1
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0
        elif Location =='Kolkata':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=1
            Location_Mumbai=0
            Location_Pune=0
        elif Location =='Mumbai':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=1
            Location_Pune=0
        elif Location =='Pune':
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=1 
        else:
            Location_Bangalore =0
            Location_Chennai =0
            Location_Coimbatore=0
            Location_Delhi=0
            Location_Hyderabad=0
            Location_Jaipur=0
            Location_Kochi=0
            Location_Kolkata=0
            Location_Mumbai=0
            Location_Pune=0

        fuel_type =requests.POST['fuel_type']
        if fuel_type =='Petrol':
            Fuel_Type_Diesel =0
            Fuel_Type_LPG =0
            Fuel_Type_Petrol =1
        elif fuel_type =='Diesel':
            Fuel_Type_Diesel =1
            Fuel_Type_LPG =0
            Fuel_Type_Petrol =0
        elif fuel_type =='LPG':
            Fuel_Type_Diesel =0
            Fuel_Type_LPG =0
            Fuel_Type_Petrol =0
        else:
            Fuel_Type_Diesel =0
            Fuel_Type_LPG =0
            Fuel_Type_Petrol =0


        ans =model.predict([[year,Kilometers_Driven,transmission,owner,Seats,Mileage,Power,Engine,Location_Bangalore,Location_Chennai,Location_Coimbatore,Location_Delhi,Location_Hyderabad,Location_Jaipur,Location_Kochi,Location_Kolkata,Location_Mumbai,Location_Pune,Fuel_Type_Diesel,Fuel_Type_LPG,Fuel_Type_Petrol]])
        context ={
            'ans':round(float(ans),2),
            'flag':True
        }

    return render(requests,'index.html',context=context)
