import requests


class Api(object):
    def __init__(self, base_url):
        self.url = f'{base_url}/gasStation/process'
        self.data_source_id = 'bHRz'
        self.session = requests.session()
        self.session.timeout = 60

    def add_fuel_card(self, card_number):
        data = {
                "dataSourceId": self.data_source_id,
                "methodId": "00A",
                "CardInfo": {
                    "cardNumber": card_number
                }
            }
        res = self.session.post(self.url, json=data)
        print(f'添加加油卡 请求数据: {data} 响应数据：{res.text}')
        return res.json()

    def bind_fuel_card(self, card_number, username, id_number, id_type="1"):
        data = {
                "dataSourceId": self.data_source_id,
                "methodId": "01A",
                "CardUser": {
                    "userName": username,
                    "idType": id_type,
                    "idNumber": id_number
                },
                "CardInfo": {
                    "cardNumber": card_number
                }
            }
        res = self.session.post(self.url, json=data)
        print(f'绑定加油卡 请求数据: {data} 响应数据：{res.text}')
        return res.json()

    def query_fuel_card(self, card_number, user_id):
        data = {
            'dataSourceId': self.data_source_id,
            'methodId': '02A',
            'userId': user_id,
            'cardNumber': card_number
        }
        res = self.session.get(self.url, params=data)
        print(f'查询加油卡 请求参数: {data} 响应数据：{res.text}')
        return res.json()

    def deposit_fuel_card(self, card_number, card_balance):
        data = {
                "dataSourceId": self.data_source_id,
                "methodId": "03A",
                    "CardInfo": {
                        "cardNumber": card_number,
                        "cardBalance": card_balance
                    }
                }
        res = self.session.post(self.url, json=data)
        print(f'充值加油卡 请求数据: {data} 响应数据：{res.text}')
        return res.json()

    def consume_fuel_card(self, card_number, user_id, card_balance):
        data = {
                    "dataSourceId": self.data_source_id,
                    "methodId": "04A",
                    "CardUser": {
                        "userId": user_id
                    },
                    "CardInfo": {
                        "cardNumber": card_number,
                        "cardBalance": card_balance
                    }
                }
        res = self.session.post(self.url, json=data)
        print(f'消费加油卡 请求数据: {data} 响应数据：{res.text}')
        return res.json()


if __name__ == '__main__':
    api = Api('http://115.28.108.130:8080')
    api.add_fuel_card('123456')

