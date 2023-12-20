from product.models import product

SESSION_KEY = 'Cart'


class MyCart:
    def __init__(self,request):
        self.session=request.session
        mycart = self.session.get(SESSION_KEY)
        if not mycart:
            mycart=self.session[SESSION_KEY]={}
        self.mycart=mycart

    def __iter__(self):
        ccart=self.mycart.copy()
        for key,item in ccart.items():
            item['product']=product.objects.get(slug=item['productid'])
            item['total']=int(item['price'])*int(item['quantity'])
            item['pk']=key
            yield item

    def unicode_generate_id(self,productid,color,size):
            unic=f"{productid}-{color}-{size}"
            return unic

    def Cart_Add(self,productid,color,size,quantity):
        unicid=self.unicode_generate_id(productid,color,size)
        object=product.objects.get(slug=productid)
        if unicid not in self.mycart:
            self.mycart[unicid]={'color':color,'size':size,'quantity':0,'productid':str(productid),'price':str(object.price)}
        self.mycart[unicid]['quantity']+=int(quantity)
        self.save()

    def save(self):
        self.session.modified=True

    def deletecart(self,id):
        if id in self.mycart:
            del self.mycart[id]
            self.save()

    def total(self):
        cart=self.mycart
        m=list( int(item['price'])*int(item['quantity']) for item in cart.values())
        sumprice = sum(m)
        return sumprice

    def remove(self):
        del self.session[SESSION_KEY]


