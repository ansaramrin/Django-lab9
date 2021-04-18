from django.db import models

'''
# create table core_product(
#     id INTEGER,
#     name VARCHAR(300),
#     price NUMBER DEFAULT 0
# );
'''

# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#
# class ProductTag(models.Model):
#     tag = models.ForeignKey(Tag)
#     product = models.ForeignKey(Product)

class Company (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=100)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.id}: {self.name}|{self.description}| {self.city}: {self.address}'

class Vacancy (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='company')

    # tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary
        }

    def __str__(self):
        return f'{self.id}: {self.name}|{self.description}| {self.salary}------{self.company}'


