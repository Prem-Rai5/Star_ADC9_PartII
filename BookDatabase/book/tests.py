from django.test import TestCase
from .models import Book,member,Bill,Transaction

class Setup_class(TestCase):


    def setUp(self):
        book1 = Book.objects.create(name="ciscobook",author = "rohit")
        p1 = member.objects.create(member_name="Ram", member_phone= 986423578)
        bill1 = Bill.objects.create(bill_no=123)
        trans1 = Transaction.objects.create(name = "T1", amount = 1000, member = p1)
    
    def test_is_valid_book(self):
        book1 = Book.objects.get(name = "ciscobook")
        booleanvalue = book1.is_valid_book()
        self.assertTrue(booleanvalue,True)

    


    def test_is_valid_bill(self):
        billNo = Bill.objects.get(bill_no=123)
        self.assertTrue(billNo.is_valid_bill(),True)

    def test_minimum_1000(self):
        price = Transaction.objects.get(name = "T1")
        value = price.is_minvalue1000()
        self.assertTrue(value,True)
        
    def test_author(self):
        book1 = Book.objects.get(name = "ciscobook")
        authorname = book1.authorname()
        self.assertEqual(authorname,"rohit")

    def test_validemail(self):
        book1 = Book.objects.get(name = "ciscobook")
        emailvalue = book1.validemail()
        self.assertTrue(emailvalue,True)
