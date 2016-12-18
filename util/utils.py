from random import randint, choice
import datetime

names = ['Eglis', 'Liaena', 'Mirelys', 'Vionaika', 'Danayasi', 'Arais', 'Trifina', 'Misleydi', 'Ermela', 'Pedra',
         'Anielka', 'Yipsi', 'Yodelkis', 'Yuneislys', 'Yoslaine', 'Rubiseida', 'Surina', 'Merlín', 'Gudelis',
         'Onelys', 'Mailer', 'Yilián', 'Danae', 'Yailén', 'Yamila', 'Imillas', 'Yamilet', 'Yenielys', 'Vindenay',
         'Tatiel', 'Dergán', 'Inaudis', 'Dennos', 'Randy', 'Freddy', 'Génesis', 'Yemel', 'Yordanys', 'Dioscórides',
         'Yusmaikel', 'Leovanny', 'Yoerky', 'Abdel', 'Adiel', 'Alain', 'Alden', 'Aleidis', 'Alexander', 'Alexos',
         'Alien', 'Amauri', 'Antino', 'Arleys', 'Asniel', 'Ayalen', 'Calmiche', 'Cosmar', 'Dabiel', 'Damichel',
         'Danel', 'Danger', 'Danny', 'Dany', 'Darién', 'Darwin', 'Deinis', 'Delvis', 'Denis', 'Dermis', 'Dimitri',
         'Dioel', 'Dirien', 'Doelsis', 'Donal', 'Doval', 'Dublas', 'Dunieki', 'Duniel', 'Edilbel', 'Edisbel',
         'Eglys', 'Eliecer', 'Elier', 'Eliovel', 'Eliu', 'Enoyder', 'Eriel', 'Francisley', 'Frederich', 'Genier',
         'Geosvanni', 'Gionni', 'Giorvis', 'Hassan', 'Hermes', 'Idel', 'Ifreidi', 'Irandy', 'Islet', 'Ixis',
         'Jairo', 'Jeichel', 'Jeison', 'Jenny', 'Joan', 'Johan', 'Jokel', 'Jonder', 'Junior', 'Karel', 'Kenen',
         'Kenny', 'Lemay', 'Leodanis', 'Leovel', 'Lerys', 'Leslie', 'Leyán', 'Liobel', 'Lisdey', 'Lisnel', 'Loidel',
         'Maicel', 'Maidier', 'Maikel', 'Marcio', 'Michel', 'Mijail', 'Minoel', 'Miralis', 'Misael', 'Neury',
         'Nivaldo', 'Noelvis', 'Norge', 'Norlis', 'Odelmis', 'Onel', 'Ordanys', 'Orelvis', 'Orlis', 'Ormari',
         'Osbeck', 'Osbiel', 'Osdelvis', 'Osmani', 'Osmel', 'Pavel', 'Raidel', 'Raudel', 'Reinier', 'Renier',
         'Robelio', 'Roberquis', 'Robeysi', 'Roger', 'Roidel', 'Roinier', 'Rolexis', 'Ronnier', 'Rudy', 'Sandy',
         'Selme', 'Serguei', 'Stanley', 'Ubisney', 'Valeri', 'Vicyhondri', 'Vidalmer', 'Waldo', 'Wilber', 'Wilmer',
         'Yadel', 'Yadiel', 'Yadier', 'Yagencys', 'Yaibel', 'Yaimel', 'Yamel', 'Yandri', 'Yasel', 'Yasiel',
         'Yasmani', 'Yassel', 'Yasser', 'Yenier', 'Yisnei', 'Yoandry', 'Yoandy', 'Yoandy', 'Yoanis', 'Yoanny',
         'Yoelkis', 'Yoelmis', 'Yoelvis', 'Yoenis', 'Yoenis', 'Yoenny', 'Yoice', 'Yoirani', 'Yoisnel', 'Yolber',
         'Yolexis', 'Yonelky', 'Yonger', 'Yorbis', 'Yordan', 'Yordanis', 'Yorelvis', 'Yorley', 'Yormani', 'Yorquis',
         'Yosbel', 'Yosley', 'Yosvani', 'Yovani', 'Yudiel', 'Yulexis', 'Yulieski', 'Yuliet', 'Yunel', 'Yunier',
         'Yunieski', 'Yuniesky', 'Yunior', 'Yusded', 'Yusisley', 'Yuslán', 'Yusmani', 'Yusmel', 'Yusnel', 'Yusniel',
         'Yusquiel']

last_names = ['CAMPOS', 'VEGA', 'FUENTES', 'DIEZ', 'CARRASCO', 'CABALLERO', 'NIETO', 'REYES', 'AGUILAR', 'PASCUAL',
              'HERRERO', 'SANTANA', 'LORENZO', 'MONTERO', 'HIDALGO', 'GIMENEZ', 'IBAÑEZ', 'FERRER', 'DURAN',
              'SANTIAGO', 'VICENTE', 'BENITEZ', 'MORA']

other = ['mamá', 'papá', 'tío', 'prima', 'abuelo', 'abuela']


def random_string(available_choices=None):
    return choice(available_choices)


def get_random_first_name():
    return random_string(names)


def get_random_last_name():
    return random_string(last_names).title()


def get_random_user_name():
    """
        Returns an string that can be used as a user name.
        Examples:
            Misleydi Caballero
            Carlos
            mamá
    :return:
    """
    kind = randint(0, 2)
    if kind == 0:
        return '{0} {1}'.format(get_random_first_name(), get_random_last_name())
    elif kind == 1:
        return get_random_first_name()
    else:
        return random_string(other)


def get_random_date(before=datetime.date(1999, 1, 1), after=datetime.date(1920, 1, 1)):
    if not (isinstance(after, datetime.date) and isinstance(before, datetime.date)):
        raise ValueError
    delta_days = (before - after).days
    return after + datetime.timedelta(days=randint(0, delta_days))


def get_random_id_number():
    rand_date = get_random_date()
    year = str(rand_date.year)[2:]
    month = str(rand_date.month) if rand_date.month > 9 else "0{0}".format(rand_date.month)
    day = str(rand_date.day) if rand_date.day > 9 else "0{0}".format(rand_date.day)

    last_numbers = randint(10000, 99999)
    return "{0}{1}{2}{3}".format(year, month, day, last_numbers)


def get_random_license_number():
    number = randint(1000000000, 9999999999)
    kind = random_string(['A', 'B', 'C', 'D', 'E', 'D'])
    return "{0}{1}".format(kind, number)
