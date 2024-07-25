from req.TradeReq import TradeReq


class TradePayoutReq(TradeReq):
    def __init__(self, paymentMethod, payer, receiver, cashAccount, orderNo, purpose, productDetail, additionalParam,
                 itemDetailList, billingAddress, shippingAddress, money, merchant, callbackUrl, redirectUrl):
        super().__init__(orderNo, purpose, productDetail, additionalParam, itemDetailList, billingAddress,
                         shippingAddress, money, merchant, callbackUrl, redirectUrl)
        if paymentMethod is not None:
            self.paymentMethod = paymentMethod
        if payer is not None:
            self.payer = payer
        if receiver is not None:
            self.receiver = receiver
        if cashAccount is not None:
            self.cashAccount = cashAccount
