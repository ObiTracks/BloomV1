from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django_countries.fields import CountryField
import calendar
from datetime import date, time, timedelta



class Company(models.Model):
    company_name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    company_email = models.EmailField(max_length=60,null=False, blank=False, unique=True)
    address_line = models.CharField(max_length=200, null=False, blank=False, unique=True)
    city = models.CharField("City", max_length=1024, null=False, blank=False)
    zip_code = models.CharField("ZIP/Postal code", max_length=12, null=True, blank=True)
    country = CountryField(blank_label="Select country", null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    
    class Meta:
        ordering = ["-company_name"]
        verbose_name = "Company"

    def __str__(self):
        return "{}".format(self.company_name)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="customer_set", null=True, on_delete=models.CASCADE)
    lease_owner = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(default='someemail@gmail.com', max_length=200, null=True, unique=True)
    apt = models.IntegerField(default='205', blank=False)
    # phone = models.CharField(default='805.555.3809', max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    # lease_members = models.TextField('Lease Members', blank=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class LeaseMember(models.Model):
    RELATIONSHIP = (
        ('husband','Husband'),
        ('wife','Wife'),
        ('daughter','Daughter'),
        ('son','Son'),
        ('relative','Relative')
    )
    lease_owner = models.ForeignKey(Customer, related_name="lease_member_set", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,null=False, blank=False)
    relation = models.CharField(max_length=100,null=True, choices=RELATIONSHIP)

    def __str__(self):
        return "{}".format(self.full_name)

class Day(models.Model):
    company = models.ForeignKey(Company, related_name="day_set", null=True, on_delete=models.CASCADE)
    today = date.today()
    tomorrow = today + timedelta(days=1)

    # Fields
    day = models.DateField(default=tomorrow, blank=False) 
    date_created = models.DateField(default=today, blank=False, editable=False)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    pool_capacity = models.IntegerField(null=True, blank=False)
    class Meta:
        ordering = ['-day']

    def name_day(self):
        date = self.day
        year = date.year
        month = calendar.month_abbr[date.month]
        day_num = date.day
        dayname = calendar.day_name[date.weekday()]
        # print(dayname)

        return '{}. {}, {}'.format(month, day_num, str(year)[-6:])
    
    def __str__(self):
        return self.name_day()

class TimeSlot(models.Model):
    TIMESLOTS = (
        ('9am-11am','9am-11am'),
        ('12pm-2pm','12pm-2pm'),
        ('3pm-5pm','3pm-5pm'),
    )

    time_slot = models.CharField(max_length=100,null=True, choices=TIMESLOTS, default="Choose a time window")
    day = models.ForeignKey(Day, related_name="timeslot_set", null=True, on_delete= models.CASCADE)
    # day = models.ForeignKey(Day, related_name="timeslot_set", default=Day.objects.first(), null=True, on_delete= models.CASCADE)
    capacity = models.IntegerField(blank=True, default=13, editable=False)
    current_capacity = models.IntegerField(default=0, blank=True, null=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    
    def return_constants(self):
        return self.TIMESLOTS
        
    def __str__(self):
        return "{} {}".format(self.day, self.time_slot)

class Reservation(models.Model):
    # Foreign relations
    customer = models.ForeignKey(Customer, related_name="reservation_set", null=True, on_delete= models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, related_name="reservation_set", null=True, on_delete=models.CASCADE)
    # Details
    no_show = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    notes = models.TextField(max_length=2000, null=True, blank=True)
    # Bring alongs
    party_members = models.CharField(max_length=1000,null=True, blank=True,)
    # lease_members = models.ManyToManyField(LeaseMember)
    # party_members = models.ManyToManyField(LeaseMember, null=True, blank=True,)
    # party_members = models.ForeignKey(LeaseMember, null=True, blank=True, on_delete=models.CASCADE)
    # party_members = models.ManyToManyField(Customer, related_name="party_members", blank=True)

    def __str__(self):
        return "{}".format(self.timeslot)
    
