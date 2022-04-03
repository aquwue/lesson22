# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def move(self, field, feld_1_param, field_2_param, direction, fly, crawl, points_per_action = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param feld_1_param: x-координата юнита
        :param field_2_param: у- координата юнита
        :param direction: направление перемещения
        :param fly: летит ли юнит
        :param crawl: крадется ли юнит
        :param points_per_action: базовый параметр скорости
        """
        # Для начала проверим не установлены ли у нас два флага полета и подкрадывания в истину,
        # т.к. одновременно эти события не должны происходить
        if fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if fly:
            points_per_action *= 1.2 # раз мы летим то сцепления наших тапочек с землей нет, и следовательно трение меньше, и поэтому скорость выше
            if direction == 'UP':
                new_y = field_2_param + points_per_action   # увеличим нашу координату Y на нашу текущую скорость
                new_x = feld_1_param  # оставим нашу координату Х без изменений
            elif direction == 'DOWN':
                new_y = field_2_param - points_per_action   # уменьшим нашу координату Y на нашу текущую скорость
                new_x = feld_1_param  # оставим нашу координату Х без изменений
            elif direction == 'LEFT':
                new_y = field_2_param  # оставим нашу координату Y без изменений
                new_x = feld_1_param - points_per_action # уменьшим нашу координату Х на нашу текущую скорость
            elif direction == 'RIGHT':
                new_y = field_2_param  # оставим нашу координату Y без изменений
                new_x = feld_1_param + points_per_action # увеличим нашу координату Х на нашу текущую скорость
        if crawl:
            points_per_action *= 0.5
            if direction == 'UP':
                new_y = field_2_param + points_per_action  # увеличим нашу координату Y на нашу текущую скорость
                new_x = feld_1_param  # оставим нашу координату Х без изменений
            elif direction == 'DOWN':
                new_y = field_2_param - points_per_action  # уменьшим нашу координату Y на нашу текущую скорость
                new_x = feld_1_param  # оставим нашу координату Х без изменений
            elif direction == 'LEFT':
                new_y = field_2_param  # оставим нашу координату Y без изменений
                new_x = feld_1_param - points_per_action  # уменьшим нашу координату Х на нашу текущую скорость
            elif direction == 'RIGHT':
                new_y = field_2_param  # оставим нашу координату Y без изменений
                new_x = feld_1_param + points_per_action  # увеличим нашу координату Х на нашу текущую скорость

            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
