from math import sin, asin, cos, acos

latitude = -22.170811
longitude = -47.393904
curr_hour = 18
curr_day = 364

def sun_declination_angle(day: int):
    return -23.45 * cos(360/365*(day + 10))

def local_hour_angle(hour: float):
    return 15 * (hour - 12)

# def sun_azimuth(lat: float, day: int, hour: float):
#     decl_angle = sun_declination_angle(day)
#     hour_angle = local_hour_angle(hour)
#     h = asin(
#         sin(decl_angle) * sin(lat) + cos(decl_angle) * cos(lat) * cos(hour_angle)
#     )
#     return h#asin(cos(lat) * sin(hour_angle) / cos(h))

# def sun_zenith(lat: float, day: int, hour: float):
#     hour_angle = local_hour_angle(hour)
#     decl_angle = sun_declination_angle(day)
#     azimuth = sun_azimuth(lat, day, hour)

#     sun_zenith = acos(
#         (sin(decl_angle) * cos(lat) - cos(decl_angle) * sin(lat) * cos(hour_angle)) 
#         / cos(azimuth) 
#     )

#     return sun_zenith if hour_angle < 0 else 360 - sun_zenith

def sun_elevation_angle(lat: float, day: int, hour: float):
    decl_angle = sun_declination_angle(day)
    hour_angle = local_hour_angle(hour)
    return asin(sin(decl_angle) * sin(lat) + cos(decl_angle) * cos(lat) * cos(hour_angle))

print('declination angle:', sun_declination_angle(curr_day))
print('hour ang:', local_hour_angle(curr_hour))
# print('azimuth:', 90 - sun_azimuth(latitude, curr_day, curr_hour))
print('elevation:', sun_elevation_angle(latitude, curr_day, curr_hour))