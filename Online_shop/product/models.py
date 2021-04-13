from django.db import models


'''
# create table store_product(
#     id INTEGER,
#     name VARCHAR(300),
#     price NUMBER DEFAULT 0,
#     description TEXT,
#     count INTEGER DEFAULT 0,
#     is_active BOOLEAN
# );
'''

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
        }
