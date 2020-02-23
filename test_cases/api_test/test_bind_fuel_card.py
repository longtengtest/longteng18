import pytest


def test_bind_fuel_card_normal(api, db, data):
    card_number = data.get('FREE_CARD_01')
    user = data.get('EXIST_USER_01')
    username = user.get('username')
    id_number = user.get('id_number')

    # 数据检查
    result = db.query_db(f'select userId from cardinfo where cardNumber="{card_number}";')
    if len(result) == 0 or result[0].get('userId') is not None:
        pytest.skip(f'卡号{card_number}不存在或卡已经绑定用户')

    result = db.query_db(f'select userId from carduser where userName="{username}" and idNumber="{id_number}";')
    if len(result) == 0:
        pytest.skip(f'用户{username} {id_number}不存在')

    user_id = result[0].get('userId')
    # 发送请求
    res_dict = api.bind_fuel_card(card_number, username, id_number)
    # {'code': 5010, 'msg': '绑定成功', 'result': {'UserId': 10143}, 'success': True}
    print(res_dict)
    assert res_dict.get('code') == 5010
    assert res_dict.get('msg') == '绑定成功'
    assert res_dict.get('result').get('UserId') == user_id
    assert res_dict.get('success') is True

    # 数据库断言
    result = db.query_db(f'select userId from cardinfo where cardNumber="{card_number}";')
    assert result and result[0].get('userId') == user_id

    # 数据清理
    db.change_db(f'UPDATE cardinfo SET userId=NULL,cardstatus=0 WHERE cardNumber="{card_number}";')


if __name__ == '__main__':
    pytest.main(['test_bind_fuel_card.py::test_bind_fuel_card_normal', '-rs', '--base-url=http://115.28.108.130:8080'])