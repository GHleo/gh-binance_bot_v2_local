"""
 This code is a part of Bablofil project, 
 and is confidential and proprietary. 
 Contacts: email: orders@bablofil.ru
           telegram: @BotsForCrypt, @Bablofil
"""

class BaseTrade(object):
    def __init__(self, trade_id, trade_rate, trade_amount, trade_type,
                 trade_total=None, trade_fee=None, fee_type=None, **kwargs):

        self.trade_id = trade_id
        self.trade_rate = trade_rate
        self.trade_amount = trade_amount
        self.trade_type = trade_type
        self.trade_fee = trade_fee
        self.fee_type = fee_type
        if not trade_total:
            self.trade_total = trade_rate * trade_amount
        else:
            self.trade_total = trade_total

        # Устанавливаем прочие свойства для представления класса
        for key, value in kwargs.items():
            setattr(self, key, value)

