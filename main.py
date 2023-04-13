import requests
import argparse


def send(account, value):
    url = 'https://eservice.towngas.com/MeterReading/ReportMeterReading'
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15"

    try:
        headers = {'User-Agent': user_agent}
        # print('header %s' % user_agent)
        pload = {'VASID': '',
                 'SelectWay': 'rbAccountAddress',
                 'SelectType': '1',
                 'ChannelID': '1',
                 'NonLoginAccountNo': account,
                 'SelectAddress': '',
                 'AddressStandardaztion_SelectBuildingKey': '',
                 'AddressStandardaztion_AccountNo1': '',
                 'AddressStandardaztion_AccountNo2': '',
                 'AddressStandardaztion_BuildingKey': '',
                 'AddressStandardaztion_work_Zone': '',
                 'FindAddressRegisteredName': '',
                 'Meter_Reading': tg_value,
                 'ValidationStatus': '1'
                 }
        response = requests.post(url, headers=headers, data=pload)
    finally:
        return response.json()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use the command to submit gas meter value to HK Town Gas website')
    parser.add_argument('-a', '--account', type=str)
    parser.add_argument('-v', '--value', type=str)
    args = parser.parse_args()

    tg_account = args.account  # '7163687262'
    tg_value = args.value  # '1041'

    if tg_account is None or tg_value is None:
        print("Not all parameters are provided! \ntype withe -h parameter for help!")
    else:
        ret = send(tg_account, tg_value)
        print(ret)
        print("submit successfully!")
