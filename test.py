import math

FREE_FALL = 9.81

ang = math.radians(30)
ang_degree = math.degrees(ang)
sin_ang = math.sin(ang)
sin_ang_deg = math.sin(ang_degree)

# print('Радианы', ang)
print('Градусы', ang_degree)
# print('Синус радиан', sin_ang)
# print('Синус градусов', sin_ang_deg)


def calc(speed, angle):
    angle_rad = math.radians(angle)
    # полное время полета снаряда
    time = 2 * speed * math.sin(angle_rad) / FREE_FALL

    # высота подъема
    height = (math.pow(
        speed, 2) * math.pow(math.sin(angle_rad), 2)) / (2 * FREE_FALL)

    # Дальность полета
    distance = math.pow(
        speed, 2) * math.sin(2 * angle_rad) / FREE_FALL

    return (f'Время полета (с) - {time:.2f}, '
            f'высота подъема (м) - {height:.2f}, '
            f'дальность полета (м) - {distance:.2f}.')


def what_angle(speed, distance):
    angle = math.asin((distance / math.pow(speed, 2) * FREE_FALL))
    # angle = math.degrees(angle / 2)
    return f'Угол равен {angle:.2f}.'


print(calc(490, 30))
print(what_angle(490, 21195.99))
