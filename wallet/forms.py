

from django import forms
from .models import Card, Customer, Loan, Notifcation, Receipt, Reward, ThirdParty, Transaction, Walletb
from .models import Account

class CustomerRegisterationForm(forms.ModelForm):
    class Meta:   
        model=Customer
        fields=("first_name","last_name","address","email","phone_number","nationality","gender","age","profile_picture")
        widgets={
             "first_name":forms.TextInput(attrs={ 'class': "form-control"}),
             "last_name": forms.TextInput(attrs={ 'class': "form-control"}),
             "address": forms.TextInput(attrs={ 'class': "form-control"}),
             "email": forms.TextInput(attrs={ 'class': "form-control"}),
             "phone_number": forms.TextInput(attrs={ 'class': "form-control"}),
             "gender": forms.Select(attrs={ 'class': "form-control"}),
             "nationality": forms.TextInput(attrs={ 'class': "form-control"}),
             "age": forms.TextInput(attrs={ 'class': "form-control"}),
             "profile_picture":forms.ClearableFileInput(attrs={ 'class': "form-control"}),

}
class AccountRegistrationForm(forms.ModelForm):
    class Meta:
        model=Account
        fields=("customer","account_balance","pin","account_number")
        widgets={
            "customer":forms.Select(attrs={'class':"form-control"}),
            "balance":forms.TextInput(attrs={'class':"form-control"}),
            "pin":forms.TextInput(attrs={'class':"form-control"}),
            "account_number":forms.TextInput(attrs={'class':"form-control"}),

   }
class WalletRegistrationForm(forms.ModelForm):
    class Meta:
        model=Walletb
        fields=("customer","wallet_id","currency_supported")
        widgets={
             "customer":forms.Select(attrs={'class':"form-control"}),
             "wallet_id":forms.TextInput(attrs={'class':"form-control"}),
             "currency_supported":forms.NumberInput(attrs={'class':"form-control"}),

        }

class RegisterTransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=("walletb","origin_account","destination_account","transaction_code","transaction_amount","transaction_charge","transaction_date")
        widgets={
            "walletb":forms.Select(attrs={'class':"form-control"}),
            "origin_account":forms.TextInput(attrs={'class':"form-control"}),
            "destination_account":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_code":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_amount":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_charge":forms.TextInput(attrs={'class':"form-control"}),
            "transaction_date":forms.TextInput(attrs={'class':"form-control"}),
            
             }
    

class CardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Card
        fields=('card_number','card','card_security_code','issuer','walletb')
        widgets={
            'card_number':forms.NumberInput(attrs={'class':"form-control"}),
            'card':forms.Select(attrs={'class':"form-control"}),
            "card_security_code":forms.TextInput(attrs={'class':"form-control"}),
            "issuer":forms.TextInput(attrs={'class':"form-control"}),
            "walletb":forms.Select(attrs={'class':"form-control"}),

        }

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:
        model=ThirdParty
        fields=('account_a','walletb','date_of_issue','amount')
        widgets={
            'account_a':forms.Select(attrs={'class':"form-control"}),
            "walletb":forms.Select(attrs={'class':"form-control"}),
            "date_of_issue":forms.DateTimeInput(attrs={'class':"form-control"}),
            "amount":forms.NumberInput(attrs={'class':"form-control"})
        }

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:
        model=Notifcation
        fields=('message','title','date','status','customer')
        widgets={
            "message":forms.Textarea(attrs={'class':"form-control"}),
            "title":forms.TextInput(attrs={'class':"form-control"}),
            "date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "status":forms.Select(attrs={'class':"form-control"}),
            "customer":forms.Select(attrs={'class':"form-control"}),
        }
class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:
        model=Receipt
        fields=("receipt_date","receipt_number","receipt_file","transaction")
        widgets={
            "receipt_date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "receipt_number":forms.NumberInput(attrs={'class':"form-control"}),
            "receipt_file":forms.ClearableFileInput(attrs={'class':"form-control"}),
            "transaction":forms.NumberInput(attrs={'class':"form-control"})
        }
class LoanRegistrationForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields=("loan_amount","loan_type","interest_rate","date")
      
        widgets={
            "loan_amount":forms.NumberInput(attrs={'class':"form-control"}),
            "loan_type":forms.Select(attrs={'class':"form-control"}),
            "interest_rate":forms.NumberInput(attrs={'class':"form-control"}),
            "date":forms.DateTimeInput(attrs={'class':"form-control"}),
          

        }
class RewardRegistrationForm(forms.ModelForm):
    class Meta:
        model=Reward
        fields=("date","recepient","points")
        widgets={
            "date":forms.DateTimeInput(attrs={'class':"form-control"}),
            "recepient":forms.Select(attrs={'class':"form-control"}),
            "points":forms.NumberInput(attrs={'class':"form-control"})
        }


