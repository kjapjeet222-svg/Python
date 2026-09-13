print("Welcome to ride builder!")
print()


print("Step 1: Pick your vehicle")
print(" 1 - bike")
print(" 2- car")


choice = int(input("Enter 1 or 2: "))

if choice == 1:
   print("Step 2: Pick your bike type")
   print("  1 - scooty")
   print("  2 - Mountine bike")
   print()


   bike_type = int(input("Enter 1 or 2:"))
   print()

   if bike_type == 1:

      print("You picked  : scooty")
      print("Top speed : 80 km/h")
      print("Best for : city roads")
   else:
      print("You picked  : Mountain Bike")
      print("Top speed  : 40 km/h")
      print("Best for : off-road trails")
      
      

elif choice == 2:
   print("Step 2  : Pick your car type")
   print(" 1 - sedan")
   print(" 2 - SUV")
   print()


   car_type = int(input("Enter 1 or 2: "))
   print()


   if car_type == 1:
       print("You picked  : Sedan")
       print("Seats  : 5 passengers")
       print("Best for  : Family trips")
   else:
       print("You picked  : SUV")
       print("Seats  : 7 passengers")
       print("Best for : off-road adventures")


else:
   print("That was not a valid choice.")
   print("Please enter 1 for bike or 2 for car.")
   print()

print("Your custom ride is ready!")
print("Enjoy the journey!")
