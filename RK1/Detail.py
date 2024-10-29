from operator import itemgetter


class Detail:
    def __init__(self, id, name, weight, price, id_prov):
        self.id = id
        self.name = name
        self.weight = weight
        self.price = price
        self.id_prov = id_prov


class Provider:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DetProv:
   def __init__(self, det_id, prov_id):
        self.det_id = det_id
        self.prov_id = prov_id

providers = [
    Provider(1, 'АртАвто'),
    Provider(2, 'РусТрейдСервис'),
    Provider(3, 'Кетекс'),
    Provider(4, 'Партгрейд'),
    Provider(5, 'Комтранс')
]

details = [
    Detail(1, 'Катушка', 2000, 12000, 3),
    Detail(2, 'Свеча зажигания', 1400, 7000, 1),
    Detail(3, 'Фара', 430, 9600, 1),
    Detail(4, 'Термостат', 1150, 13500, 4),
    Detail(5, 'Аккумулятор', 1330, 8750, 5)
]

dets_provs = [
    DetProv(1, 1),
    DetProv(2, 2),
    DetProv(3, 3),
    DetProv(3, 4),
    DetProv(3, 5),
    DetProv(4, 1),
    DetProv(4, 2),
    DetProv(5, 3),
    DetProv(5, 4),
    DetProv(5, 5),
]


def main():
    one_to_many = [(d.name, d.price, p.name)
                   for d in details
                   for p in providers
                   if d.id_prov == p.id]

    many_to_many_temp = [(p.name, dp.prov_id, dp.det_id)
                         for p in providers
                         for dp in dets_provs
                         if p.id == dp.prov_id]

    many_to_many = [(d.name, d.price, prov_name)
                    for prov_name, prov_id, det_id in many_to_many_temp
                    for d in details if d.id == det_id]

    print('Задание 1')
    res_1 = [el for el in one_to_many if 'Авто' in el[2]]
    print(res_1)

    print('\nЗадание 2')
    res_2_unsorted = []
    for prov in providers:

        prov_det = [(el[0], el[1]) for el in one_to_many if prov.name in el]
        print("prov_det=", prov_det)
        if len(prov_det) > 0:
            sred_price = sum([el[1] for el in prov_det])/len(prov_det)
            print(sred_price)
            res_2_unsorted.append((prov.name, sred_price))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание 3')
    res_3 = []
    for el in many_to_many:
        if el[0][0] == 'Т':
            res_3.append((el[0], el[2]))
    print(res_3)


if __name__ == '__main__':
    main()
