import string
import factory
import factory.fuzzy
from .models import PennUser


class PennUserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PennUser

    username = factory.Sequence(lambda n: "bfrank{0}".format(n))
    email = factory.LazyAttribute(lambda obj: "{0}@seas.upenn.edu".format(obj.username))
    pennid = factory.fuzzy.FuzzyText(length=8, chars=string.digits)


class PennUserStaffFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PennUser
    username = factory.Sequence(lambda n: "tjefferson{0}".format(n))
    email = factory.LazyAttribute(lambda obj: "{0}@seas.upenn.edu".format(obj.username))
    is_staff = True
    is_active = True


class PennUserAdminFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PennUser
    username = factory.Sequence(lambda n: "tjefferson{0}".format(n))
    email = factory.LazyAttribute(lambda obj: "{0}@seas.upenn.edu".format(obj.username))
    is_staff = True
    is_active = True
    is_admin = True

