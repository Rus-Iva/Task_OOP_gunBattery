import math

# Ускорение свободного падения.
FREE_FALL_ACCEL = 9.81


class GunBattery:
    """Создание орудия.

    Ключевые аргументы:
    :param name: наименование орудия, по умолчанию None
    :type name: str
    :param bullet_speed: скорость выпускаемого снаряда, по умолчанию None
    :type bullet_speed: float
    :param shot_records: для логирования выстрелов, по умолчанию пуст.
    :type shot_records: list

    Методы:
    .. method:: calc(distance)
    Подсчет параметров для попадания в цель.
    :param distance: расстояние, точка приземления снаряда
    :type distance: float
    .. method:: add_record(record)
    Добавление записи в список shot_records.
    :param record: добавляемая запись
    :type record: str
    .. method:: show_records()
    Вывод списка shot_records в консоль.
    """

    INCORRECT_VALUE_TEMPLATE = ('{dist} или {speed} - '
                                'некорректные данные. '
                                'Оба числа должны быть положительными.')
    RECORD_TEMPLATE = ('Цель на расстоянии, м: {dist}. '
                       'Угол наводки, град: {angle_degree:.2f}. '
                       'Время полета снаряда (таймер взрыва, с): {time:.2f}.')

    def __init__(self, name=None, bullet_speed=None):
        self.shot_records = []

        if name is None:
            self.name = 'Орудийная батарея'
        else:
            self.name = name

        if bullet_speed is None:
            self.bullet_speed = 1000
        else:
            self.bullet_speed = bullet_speed

    def add_record(self, record):
        """Добавление записи в список shot_records.
        :param str record: добавляемая запись
        :return: none.
        """
        self.shot_records.append(record)

    def show_records(self):
        """Вывод списка shot_records в консоль.

        :return: print(list)
        """
        if not self.shot_records:
            print('В списке нет записей.')
        else:
            print(f'Записи о выстрелах орудия "{self.name}" '
                  f'(скорость снаряда, м/с: {self.bullet_speed}):')
            print('\n'.join(self.shot_records))

    def calc(self, distance):
        """Подсчет параметров для попадания в цель.

        Ключевые аргументы:
        :param float distance: расстояние, точка приземления снаряда

        Создай запись rec, в которой:
        :param distance: расстояние (м),
        angle_degree: угол наводки (град),
        time_fly: время полета снаряда (с).

        Добавь rec в shot_records.

        :return: rec.
        """

        if distance <= 0 or self.bullet_speed <= 0:
            return self.INCORRECT_VALUE_TEMPLATE.format(dist=distance,
                                                        speed=self.bullet_speed
                                                        )

        angle = abs(math.asin(distance / math.pow(self.bullet_speed, 2) *
                    FREE_FALL_ACCEL) / 2)
        angle_degree = math.degrees(angle)

        time_fly = abs(2 * self.bullet_speed * math.sin(angle) /
                       FREE_FALL_ACCEL)
        rec = self.RECORD_TEMPLATE.format(dist=distance,
                                          angle_degree=angle_degree,
                                          time=time_fly)

        self.add_record(rec)

        return rec
