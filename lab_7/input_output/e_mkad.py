# lambda function to calculate road sign based on distance traveled

road_sign = lambda speed, time: (speed * time) % 109

# example usage
if __name__ == "__main__":
    print("Calculate road sign based on distance traveled")
    speed = int(input("Enter the speed (km/h): "))
    time = int(input("Enter the time (h): "))
    print(f"The road sign is {road_sign(speed, time)} km")