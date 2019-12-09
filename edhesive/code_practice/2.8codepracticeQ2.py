lat = input("Enter lats: ")
lon = input("Enter lons: ")

lat_list = [float(s) for s in lat.split(',')]
lon_list = [float(s) for s in lon.split(',')]

print("Furthest north: " + str(max(lat_list)))
print("Furthest west: " + str(max(lon_list)))
print("Furthest south: " + str(min(lat_list)))
print("Furthest east: " + str(min(lon_list)))
