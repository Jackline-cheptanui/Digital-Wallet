from email import message
from django.shortcuts import render
from .forms import AccountRegistrationForm, CardRegistrationForm, CustomerRegisterationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RegisterTransactionForm, RewardRegistrationForm,ThirdPartyRegistrationForm, WalletRegistrationForm
from .models import Account, Card, Customer, Loan, Notifcation, Receipt, Reward, ThirdParty, Transaction, Walletb
from django.shortcuts import redirect
from django.views.generic.base import View
from rest_framework import views
from rest_framework.response import Response


def home_page(request):
    return render(request,"wallet/index.html")



def register_customer(request):
    if request.method=='POST':
        form=CustomerRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CustomerRegisterationForm()
    return render(request,"wallet/register_customer.html",
        {"formi":form
    })
    

def customer_profile(request,id):
   customers=Customer.objects.get(id=id)
   return render(request,"wallet/customer_profile.html",{"customers":customers })

def edit_customer(request,id):
   customer=Customer.objects.get(id=id)
   if request.method =='POST':
       form=CustomerRegisterationForm(request.POST,instance=customer)
       if form.is_valid():
           form.save()
           return redirect("customerProfile",id=customer.id)
   else:
       form=CustomerRegisterationForm(instance=customer)
   return render(request,"wallet/edit_customer.html",{"forms":form})




class SearchCustomer(View):
    model = Customer
    template_name = 'wallet/customer_list.html'

    def get(self,request):
        customers=Customer.objects.all()
        customer_found=request.GET.get('customer_found',None)     #request takes form as customer_found 
        if customer_found:
            result=Customer.objects.filter(first_name__contains=customer_found)    #filter from database and assign it tothe request 
            context={'Customers':result}
            return render(request, self.template_name,context)   #return result
        context={'Customers':customers}
        return render(request, self.template_name,context)                                  
    


def register_account(request):
    if request.method=="POST":
            form_account=AccountRegistrationForm(request.POST)
            if form_account.is_valid():
                form_account.save()
    else:
        form_account=AccountRegistrationForm()
    return render(request,'wallet/register_account.html',{"form":form_account} )



def list_accounts(request):
    accounts=Account.objects.all()
    return render(request,'wallet/account_list.html',{
        "accounts":accounts})

def account_profile(request,id):
    account=Account.objects.get(id=id)
    return render(request,"wallet/account_profile.html",{"accounts":account})

def edit_account(request,id):
    account=Account.objects.get(id=id)
    if request.method == "POST":
        form=AccountRegistrationForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect("accountProfile",id=account.id)

    else:
        form=AccountRegistrationForm(instance=account)
    return render(request,"wallet/edit_account.html",{"forms":form})

def register_wallet(request):
    if request.method=="POST":
            form_wallet=WalletRegistrationForm(request.POST)
            if form_wallet.is_valid():
                form_wallet.save()
    else:
        form_wallet=WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html", {"wallet":form_wallet} )

def wallet_profile(request,id):
    wallet=Walletb.objects.get(id=id)
    return render(request,"wallet/account_profile.html",{"wallets":wallet})

def edit_wallet(request,id):
    wallet=Walletb.objects.get(id=id)
    if request.method=="POST":
        form=WalletRegistrationForm(request.POST,instance=wallet)
        if form.is_valid():
            form.save()
            return redirect("walletProfile",id=wallet.id)
    else:
        form=WalletRegistrationForm(instance=wallet)
        return render(request,"wallet/edit_wallet.html",{"forms":form})

def list_wallet(request):
    wallet=Walletb.objects.all()
    return render(request,"wallet/wallet_list.html",{"wallet":wallet})


def register_transaction(request):
    if request.method=="POST":
            form_transact=RegisterTransactionForm(request.POST)
            if form_transact.is_valid():
                form_transact.save()
    else:
        form_transact=RegisterTransactionForm()
    return render(request,"wallet/register_transaction.html", {"transact":form_transact})

def list_transaction(request):
    transactions=Transaction.objects.all()
    return render(request,"wallet/transaction_list.html",{"transactions":transactions})


def register_card(request):
    card_form=CardRegistrationForm()
    if request.method=="POST":
        card_form=CardRegistrationForm(request.POST)
        if card_form.is_valid():
            card_form.save()
    else:
        card_form=CardRegistrationForm()
    return render(request,"wallet/card_register.html",{"card":card_form})

def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render(request,"wallet/transaction_profile.html",{"transactions":transaction})


def edit_transaction(request,id):
    transaction=Transaction.objects.get(id=id)
    if request.method=="POST":
        form=RegisterTransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transactionProfile",id=transaction.id)
    else:
        form=RegisterTransactionForm(instance=transaction)
        return render(request,"wallet/edit_transaction.html",{"forms":form})


def list_card(request):
    card=Card.objects.all()
    return render(request,"wallet/list_card.html",{"cards":card})

def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render(request,"wallet/card_profile.html",{"cards":card})

def edit_card(request,id):
    card=Card.objects.get(id=id)
    if request.method=="POST":
        form=CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
            return redirect("cardProfile",id=card.id)
    else:
        return render(request,"wallet/edit_card.html",{"forms":form})
        

def register_thirdparty(request):
    if request.method=="POST":
       thirdparty_form=ThirdPartyRegistrationForm(request.POST)
       if thirdparty_form.is_valid():
           thirdparty_form.save()
    else:
        thirdparty_form=ThirdPartyRegistrationForm()
    return render(request,"wallet/register_thirdp.html",{"third":thirdparty_form})

def list_thirdparty(request):
    thirds=ThirdParty.objects.all()
    return render (request,'wallet/thirdparty_list.html',{"thirdpartys":thirds})


def register_notification(request):
    if request.method=="POST":
       form_notify=NotificationRegistrationForm(request.POST)
       if form_notify.is_valid():
           form_notify.save()
    else:
        form_notify=NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",{"notify":form_notify})

def notification_list(request):
    notification=Notifcation.objects.all()
    return render (request,'wallet/notification_list.html',{"notifications":notification})



def register_loan(request):
    if request.method=="POST":
       loan_form=LoanRegistrationForm(request.POST)
       if loan_form.is_valid():
           loan_form.save()
    else:
           loan_form=LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",{"loan":loan_form} )

def list_loan(request):
    loan=Loan.objects.all()
    return render(request,'wallet/loan_list.html',{"loans":loan})


def register_reward(request):
    if request.method=="POST":
       reward_form=RewardRegistrationForm(request.POST)
       if reward_form.is_valid():
           reward_form.save()
    else:
        reward_form=RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",{"reward":reward_form}
    )

def list_reward(request):
    reward=Reward.objects.all()
    return render(request,"wallet/reward_list.html",{"rewards":reward})


def register_receipt(request):
    if request.method=="POST":
       receipt_form=ReceiptRegistrationForm(request.POST)
       if receipt_form.is_valid():
           receipt_form.save()
       else:
            receipt_form=ReceiptRegistrationForm()
       return render(request,"wallet/register_receipt.html", {"receipt":receipt_form})

def list_receipts(request):
    receipt=Receipt.objects.all()
    return render(request,"wallet/receipt_list.html",{"receipts":receipt})

def receipt_profile(request,id):
     receipt=Receipt.objects.get(id=id)
     return render(request,"wallet/receipt_profile.html",{"receipts":receipt})

     
def edit_receipts(request,id):
     receipt=Receipt.objects.get(id=id)
     if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST,instance=receipt)
        if form.is_valid():
            form.save()
            return redirect("receiptProfile",id=receipt.id)
     else:
        form=ReceiptRegistrationForm(instance=receipt)
        return render(request,"wallet/edit_receipt.html",{"forms":form})



                           
    



