import pickle

vehicle = {
    'brand': 'BMW',
    'model': '530i',
    'year' : 2015,
    'color': 'Black Sapphire'
}

my_file = open('vehicledetail.bin', 'wb')
pickle.dump(vehicle, my_file)
my_file.close()