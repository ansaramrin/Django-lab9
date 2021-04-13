from django.db import models


'''
# create table store_category(
#     id INTEGER,
#     name VARCHAR(300)
# );
'''

class Category(models.Model):
    name = models.CharField(max_length=300)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name

        }
