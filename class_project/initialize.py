# initialize the django code
print('Initializing Django...')
import sys, os
mydir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(mydir)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "class_project.settings")
django.setup()

# regular imports
from account import models as amod
from catalog import models as cmod
from event import models as emod
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
import datetime, random, sys

#print("You should not be running this.  No soup for you.")
#sys.exit(0)

#####################################
###   Create Permissions and Groups

print()
print('Creating permissions and groups...')

# delete the existing groups and permissions assigned to them
Group.objects.all().delete()  # this also deletes everything in the association table between groups and permissions

# I'm not creating any permissions because I'm going to use the default ones that Django creates
# They are automatically created for each model class.  For the account.User class, we get:
#    account.add_user
#    account.change_user
#    account.delete_user

# manager group (managers have all permissions)
group_manager = Group()
group_manager.name = 'Manager'
group_manager.save()
for p in Permission.objects.all(): 
  group_manager.permissions.add(p)

# SalesRep group (sales reps can change only catalog items)
group_salesrep = Group()
group_salesrep.name = 'SalesRep'
group_salesrep.save()
for p in Permission.objects.filter(content_type__app_label='catalog'):
  group_salesrep.permissions.add(p)

# customer group (customers have no permissions)
group_customer = Group()
group_customer.name = 'Customer'
group_customer.save()

######################################
###   Users

print()
print('Creating users...')
amod.User.objects.all().delete()
users = []  # to save for use later
for i in range(1, 10):
  u = amod.User()
  u.username = 'user%i' % i
  u.first_name = 'First%i' % i
  u.last_name = 'Last%i' % i
  u.email = 'me%i@me.com' % i
  u.set_password('pass%i' % i)
  u.address = 'Address%i' % i
  u.city = 'City%i' % i
  u.birth = datetime.datetime.now()
  u.phone_number = '555-555-000%i' % i
  u.is_active = True
  if i == 1:
    u.is_staff = True
    u.is_superuser = True
  u.save()
  print(u)
  users.append(u)
  # assign user to some groups/permissions
print('user1, pass1 is the superuser.')

print()
for name in sorted(users[1].get_all_permissions()):
  print('Permission:', name)


#####################################
###   Products

print()
print('Creating products...')

### NO!  Products cannot be created because they don't really exist.  Never do this:
#p = cmod.Product()

# rental items
cmod.RentalProduct.objects.all().delete()
for i in range(1, 5):
  p = cmod.RentalProduct()
  p.name = 'Rental%i' % i
  p.description = 'This rental, #%i, is a really cool rental beacuse it is number %i.' % (i, i)
  p.image = 'rental%i.png' % i
  p.status = cmod.STATUS_CHOICES[0][0]
  p.save()
  print(p)
  
# individual products
cmod.IndividualProduct.objects.all().delete()
for i in range(1, 5):
  p = cmod.IndividualProduct()
  p.name = 'IndividualProduct%i' % i
  p.description = 'This product, #%i, is an individual product.  It is a bit of a loner.' % i
  p.image = 'indprod%i.png' % i
  p.creator = random.choice(users)
  p.save()
  print(p)
 
# bulk products
cmod.BulkProduct.objects.all().delete()
for i in range(1, 5):
  p = cmod.BulkProduct()
  p.name = 'BulkProduct%i' % i
  p.description = 'This product, #%i, is an bulk product. It has lots of quantity.' % i
  p.image = 'bulkprod%i.png' % i
  p.quantity = random.randint(1, 100)
  p.save()
  print(p)


print()
print('Creating Venues...')

# venues
emod.Venue.objects.all().delete()
venues = []
for i in range(1, 5):
  v = emod.Venue()
  v.name = 'Venue%i' % i
  v.address = 'This venue, #%i, is a venue. It is awesome.' % i
  v.city = 'VenueCity%i' % i
  v.state = 'VenueState%i' %i
  v.zip = 'VenueZip%i' %i
  v.save()
  print(v)
  venues.append(v)

print('Creating events...')
for i in range (1, 10):
    o = emod.Event()
    o.name = o.name = 'Event%i' % i
    o.description = 'Description of the event %i' % i
    o.start_date = datetime.datetime.now()
    o.end_date = datetime.datetime.now() 
    o.venue = random.choice(venues)
    o.save()
    print(o)
    print('Creating areas...')
    for j in range(1, 4):
        a = emod.Area()
        a.name = 'Area%i' % j
        a.description = 'Description of the area %i' % j
        a.place_number = i*j
        a.event = o
        a.save()
        print(a)
 
