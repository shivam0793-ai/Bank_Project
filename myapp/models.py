from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class CreateAccount(models.Model):
    gender_type=[('male','male'),('female','female'),('other','other')]
    account_types=[('saving','saving'),('current','current')]

    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    account_number=models.CharField(
        max_length=12,
        unique=True,
        editable=False,
        blank=True
    )

    name=models.CharField(
        max_length=50,
        unique=False,
        error_messages={'blank':'name cannot be empty','required':'please enter user_name'}
    )

    date_of_birth=models.DateField()

    gender=models.CharField(max_length=20,choices=gender_type)

    account_type=models.CharField(max_length=20,choices=account_types,error_messages={'blank':'This field cannot be empty'})

    phone_number=models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='phone number must contain excatly 10 digits'
            )
        ],
        error_messages={'unique':'Phone number already exits'}

    )

    email_address=models.EmailField(
        unique=True,
        error_messages={'unique':'email must be unique'}
    )


    aadhar_card=models.CharField(
        unique=True,
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\d{12}$',
                message='Aadhaar number must contain exactly 12 digits.'
            )
        ]
        ,error_messages={'unique':'This Aadhaar number is already registered.','blank':'name cannot be empty',
    'required':'please enter user_name'}
    )

    pan_number=models.CharField(
        unique=True,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$',
                message='Invalid PAN number format. Example: ABCDE1234F'
            )
        ],
        error_messages={'unique':'pan number already exit.'}
    )


    balance=models.DecimalField(default=0,decimal_places=2,max_digits=12)

    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-->{self.account_number}'
    
