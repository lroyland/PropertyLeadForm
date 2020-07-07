from django.db import models

"""
REASON_FOR_SELLING_CHOICES = (
    ('FINANCIALHARDSHIP','Financial Hardship'),
    ('INHERITED','Inherited'),
    ('RELOCATION','Relocation'),
    ('LOOKINGFORREALTOR','Looking for Realtor'),
    ('DOWNSIZING','Downsizing'),
    ('DIVORCE','Divorce'),
    ('REPAIRSDAMAGE','Repairs or Damage'),
    ('TIREDLANDLORD','Tired Landlord'),
    ('NOTREADYTOSELL','Not Ready to Sell Yet'),
)

PROPERTY_TYPE_CHOICES = (
    ('SINGLEFAMILY','Single Family'),
    ('CONDODUPLEXTOWNHOME','Condo, Duplex, or Town-Home'),
    ('MOBILEHOME','Mobile Home'),
)

HOW_SOON_CHOICES = (
    ('ASAP','ASAP'),
    ('3MONTHS','Within 3 Months'),
    ('6MONTHS','Within 6 Months'),
    ('NORUSH','No Rush'),
)

OCCUPANCY_CHOICES = (
    ('OWNEROCCUPIED','Occupied by Owner'),
    ('TENANTOCCUPIED','Occupied by Tenant'),
    ('VACANT','Vacant'),
)

BEHIND_ON_MORTGRAGE_CHOICES = (
    ('NO','No'),
    ('YES1MONTH','Yes 1 Month'),
    ('YES2MONTH','Yes 2 Months'),
    ('YES3PLUSMONTHS','Yes 3 or More Months'),
)

HOME_VALUE_CHOICES = (
    ('LESSTHAN50K','< $50,000'),
    ('100KTO150K','$100,000 - $150,000'),
    ('150KTO200K','$150,000 - $200,000'),
    ('200KTO250K','$200,000 - $250,000'),
    ('250KTO300K','$250,000 - $300,000'),
    ('300KTO350K','$300,000 - $350,000'),
    ('350KTO400K','$350,000 - $400,000'),
    ('400KTO450K','$400,000 - $450,000'),
    ('450KTO500K','$450,000 - $500,000'),
    ('500KTO600k','$500,000 - $600,000'),
    ('600KTO700K','$600,000 - $700,000'),
    ('700KTO800K','$700,000 - $800,000'),
    ('800KTO900K','$800,000 - $900,000'),
    ('900KTO1MILLION','$900,000 - $1,000,000'),
    ('1MILLIONTO2MILLION','$1,000,000 - $2,000,000'),
    ('2MILLIONTO3MILLION','$2,000,000 - $3,000,000'),
    ('3MILLIONPLUS','$3,000,000+'),
)

CURRENTLY_LISTED_AS_REALTOR_CHOICES = (
    ('1'),
    ('0'),

)
"""

class Lead(models.Model):
    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    email_address = models.EmailField(max_length=254)

    phone_number = models.CharField(max_length=200)

    reason_for_selling = models.CharField(max_length=100)
    """
    REASON_FOR_SELLING_CHOICES = (
        ('FINANCIALHARDSHIP','Financial Hardship'),
        ('INHERITED','Inherited'),
        ('RELOCATION','Relocation'),
        ('LOOKINGFORREALTOR','Looking for Realtor'),
        ('DOWNSIZING','Downsizing'),
        ('DIVORCE','Divorce'),
        ('REPAIRSDAMAGE','Repairs or Damage'),
        ('TIREDLANDLORD','Tired Landlord'),
        ('NOTREADYTOSELL','Not Ready to Sell Yet'),
    )
    """
    property_type = models.CharField(max_length=100)
    """
    PROPERTY_TYPE_CHOICES = (
        ('SINGLEFAMILY','Single Family'),
        ('CONDODUPLEXTOWNHOME','Condo, Duplex, or Town-Home'),
        ('MOBILEHOME','Mobile Home'),
    )
    """

    how_soon_to_sell = models.CharField(max_length=20)
    """
    HOW_SOON_CHOICES = (
        ('ASAP','ASAP'),
        ('3MONTHS','Within 3 Months'),
        ('6MONTHS','Within 6 Months'),
        ('NORUSH','No Rush'),
    )
    """

    occupancy = models.CharField(max_length=20)
    """
    OCCUPANCY_CHOICES = (
        ('OWNEROCCUPIED','Occupied by Owner'),
        ('TENANTOCCUPIED','Occupied by Tenant'),
        ('VACANT','Vacant'),
    )
    """

    behind_mortgage_payment = models.CharField(max_length=50)
    """
    BEHIND_ON_MORTGRAGE_CHOICES = (
        ('NO','No'),
        ('YES1MONTH','Yes 1 Month'),
        ('YES2MONTH','Yes 2 Months'),
        ('YES3PLUSMONTHS','Yes 3 or More Months'),
    )
    """
    estimated_home_value = models.CharField(max_length=100)
    """
    HOME_VALUE_CHOICES = (
        ('LESSTHAN50K','< $50,000'),
        ('100KTO150K','$100,000 - $150,000'),
        ('150KTO200K','$150,000 - $200,000'),
        ('200KTO250K','$200,000 - $250,000'),
        ('250KTO300K','$250,000 - $300,000'),
        ('300KTO350K','$300,000 - $350,000'),
        ('350KTO400K','$350,000 - $400,000'),
        ('400KTO450K','$400,000 - $450,000'),
        ('450KTO500K','$450,000 - $500,000'),
        ('500KTO600k','$500,000 - $600,000'),
        ('600KTO700K','$600,000 - $700,000'),
        ('700KTO800K','$700,000 - $800,000'),
        ('800KTO900K','$800,000 - $900,000'),
        ('900KTO1MILLION','$900,000 - $1,000,000'),
        ('1MILLIONTO2MILLION','$1,000,000 - $2,000,000'),
        ('2MILLIONTO3MILLION','$2,000,000 - $3,000,000'),
        ('3MILLIONPLUS','$3,000,000+'),
    )
    """

    listed_as_realtor = models.IntegerField()
    """
    REALTOR_CHOICES = (
        (1,'Yes'),
        (0,'No'),
    )
    """
    pub_date = models.DateTimeField('date published')
# Create your models here.
