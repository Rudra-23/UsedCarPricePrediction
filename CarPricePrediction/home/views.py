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
        
        Locations = [0]*10
        if Location =='Bangalore':
            Locations[0] =1
        elif Location =='Chennai':
            Locations[1] =1
        elif Location =='Coimbatore':
            Locations[2] =1    
        elif Location =='Delhi':
            Locations[3] =1   
        elif Location =='Hyderabad':
            Locations[4] = 1
        elif Location =='Jaipur':
            Locations[5] = 1
        elif Location =='Kochi':
            Locations[6] = 1
        elif Location =='Kolkata':
            Locations[7] = 1
        elif Location =='Mumbai':
            Locations[8] = 1
        elif Location =='Pune':
            Locations[9] = 1
        else:
            Locations[0] = 0

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

        final_arr = []
        final_arr += [year,Kilometers_Driven,transmission,owner,Seats,Mileage,Power,Engine]
        final_arr += Locations
        final_arr += [Fuel_Type_Diesel, Fuel_Type_LPG, Fuel_Type_Petrol]

        ans =model.predict([final_arr])
        context ={
            'ans':round(float(ans),2),
            'flag':True
        }

    return render(requests,'index.html',context=context)
