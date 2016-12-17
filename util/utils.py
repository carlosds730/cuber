def get_random_name():
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
    from random import randint
    kind = randint(0, 2)
    return '{0} {1}'.format(names[randint(0, len(names) - 1)], last_names[randint(0, len(last_names) - 1)].title()) \
        if kind == 0 else '{0}'.format(names[randint(0, len(names) - 1)]) if kind == 1 else '{0}'.format(
        other[randint(0, len(other) - 1)])
