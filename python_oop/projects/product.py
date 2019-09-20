class Product:
  def __init__(self, price, item_name, weight, brand, status='For Sale'):
    self.price = price
    self.item_name = item_name
    self.weight = weight
    self.brand = brand
    self.status = status

  
  def sell(self):
    self.status = "Sold"
    return self
  
  def add_tax(self, tax):
    
    return "Price after sales tax: ${}".format(self.price * (1+tax))
  
  def return_item(self,reason_for_return):
    if reason_for_return.lower() == 'defective':
      self.status = 'defective'
      self.price = 0
    elif reason_for_return.lower() == 'like_new':
      self.status = 'for sale'
    elif reason_for_return.lower() == 'opened':
      self.status = 'used'
      self.price = self.price * 0.80
    
    return self
  
  def display_info(self):
    print (f"Price: {self.price}")
    print (f"Item Name: {self.item_name}")
    print (f"Weight: {self.weight}")
    print (f"Brand: {self.brand}")
    print (f"Status: {self.status}")

    return self

chocolate = Product(5, 'chocolate', 100, 'Dairy Milk')
chocolate.return_item('opened')
chocolate.display_info()

