
CART_SESSION_ID='cart'


class Cart:
    def __init__(self,request):
        self.session=request.session
        cart = self.session.get(CART_SESSION_ID)

        if not cart:
            cart = self.session[CART_SESSION_ID]={}
        self.cart=cart

    def __iter__(self):
        cart=self.cart.copy()
        for item in cart.values():
            item['total']=int(item['quantity'] * item['price'])
            yield item



    def unicode_generate_id(self,id,color,size):
        unic=f"{id}-{color}-{size}"
        return unic

    def add(self,product,color,size,quantity):
          unicid=self.unicode_generate_id(product.slug,color,size)
          if unicid not in self.cart:
              self.cart[unicid]={'quantity':0,'price':str(product.price),'color':color,'size':size,'id':product.slug}
          self.cart[unicid]['quantity'] += int(quantity)
          self.save()

    def save(self):
        self.session.modified=True


