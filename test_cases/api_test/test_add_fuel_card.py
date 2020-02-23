import pytest


def test_add_fuel_card_normal(api, db, data):
    """测试添加新的加油卡"""
    card_number = data.get('NEW_CARD_01')
    # 数据准备
    db.delete_card(card_number)
    # 发送请求
    res_dict = api.add_fuel_card(card_number)
    # 断言
    assert res_dict.get('code') == 200
    assert res_dict.get('msg') == '添加卡成功'
    assert res_dict.get('success') is False

    assert db.check_card(card_number) is True  # 数据库断言

    # 环境清理
    db.delete_card(card_number)


def test_add_fuel_card_exists(api, db, data):
    """测试添加已存在的加油卡"""
    card_number = data.get('EXIST_CARD_01')
    # 数据检查
    if db.check_card(card_number) is False:
        # db.change_db(f'-- insert into cardinfo (cardNumber) values ("{card_number}")')
        pytest.skip()

    # 发送请求
    res_dict = api.add_fuel_card(card_number)
    # 断言
    assert res_dict.get('code') == 5000
    assert res_dict.get('msg') == '该卡已添加'
    assert res_dict.get('success') is False


def test_add_fuel_card_twice(api, db, data):
    card_number1 = data.get('NEW_CARD_01')
    card_number2 = data.get('NEW_CARD_02')

    # 数据准备
    db.delete_card(card_number1)
    db.delete_card(card_number2)
    # 发送请求
    api.add_fuel_card(card_number1)
    res_dict = api.add_fuel_card(card_number2)
    # 断言
    assert res_dict.get('code') == 200
    assert res_dict.get('msg') == '添加卡成功'
    assert res_dict.get('success') is False

    assert db.check_card(card_number2) is True  # 数据库断言

    # 环境清理
    db.delete_card(card_number1)
    db.delete_card(card_number2)