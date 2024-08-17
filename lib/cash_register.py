#!/usr/bin/env python3

class CashRegister:
  
  def __init__(self, discount = 0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.last_transation_amount = 0.0

  def add_item(self, name, price=0, quantity = 1):
  
    self.name = name
    self.price = price
    self.total += price * quantity
    for _ in range(quantity):
      self.items.append(name)
      self.last_transaction_amount = price * quantity


  #discount price variable by 20%
  #return the new value
  def apply_discount(self):
    if isinstance(self.total, (int, float)) and self.total > 0:
      self.total = self.total - (self.total * .20)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
    
  
  def void_last_transaction(self):
      self.total -= self.last_transaction_amount
      if self.items:
        self.items.pop()
      self.last_transaction_amount = 0
      # minus last item price from total
     
      
      #last transaction amount reset
      self.last_transaction_amount = 0
      if not self.items:
        self.total = 0.0

  