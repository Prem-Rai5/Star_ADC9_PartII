from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField()
    author = models.CharField(max_length = 30)
    email = models.EmailField(blank = True)

    def __str__(self):
        return self.name

    def is_valid_book(self):
        return self.name!=None
    def authorname(self):
        return self.author
    def validemail(self):
        return self.email!=None



class member(models.Model):
    member_name = models.CharField(max_length=50)
    member_phone = models.IntegerField()
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.member_id


class Bill(models.Model):
    bill_no = models.IntegerField()

    def is_valid_bill(self):
        return self.bill_no
        


class Transaction(models.Model):
    name = models.CharField(max_length=20)
    amount= models.IntegerField()
    member= models.ForeignKey(member, on_delete = models.CASCADE, related_name = "Members")

    def is_minvalue1000(self):
        return self.amount<=1000
