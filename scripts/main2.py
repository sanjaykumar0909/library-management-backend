from mainapp.models import Admins
def run():
    Admins(uname="sanjay", pwd=1234).save()
    Admins(uname="John", pwd=1234).save()