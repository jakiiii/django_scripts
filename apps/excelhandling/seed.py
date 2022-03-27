from excelhandling.models import UserInformation

from faker import Faker
fake = Faker()


def seed_db(n):
    for i in range(0, n):
        UserInformation.objects.create(
            start='20190321145115',
            provider_name='Banglalink',
            a_party='8801909592609',
            b_party='8801994492756',
            call_duration='30',
            usage_type='MOC',
            network_type='2G',
            mcc_start_a='470',
            mnc_start_a='3',
            lac_start_a='416',
            ci_start_a='65202',
            imei='352572100624530',
            imsia='470039402902542',
            address='Tetul baria bazar,Morrelganj,Bagerhat'
        )


'''
start
provider_name
a_party
b_party
call_duration
usage_type
network_type
mcc_start_a
mnc_start_a
lac_start_a
ci_start_a
imei
imsia
address
'''
