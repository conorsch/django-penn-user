#!/usr/bin/env python
from django.test import TestCase
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .factories import PennUserFactory, PennUserStaffFactory, PennUserAdminFactory
from .validators import validate_pennname, validate_pennid


class TestPennUserAttributes(TestCase):

    def setUp(self):
        self.user = PennUserFactory()

    def test_default_user_permissions(self):
        """User should NOT be staff or admin by default."""
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_admin)

    def test_pennkey_is_valid(self):
        """Ensure username field is 2-8 alphanumeric characters."""
        try:
            validate_pennname(self.user.username)
        except ValidationError:
            msg = "Unexpectedly failed to validate PennKey '{}'."
            self.fail(msg)

    def test_pennkey_is_invalid(self):
        self.assertRaises(ValidationError, validate_pennname, '1kjlakd')
        self.assertRaises(ValidationError, validate_pennname, 'abcdefghi')

    def test_pennid_is_valid(self):
        """Ensure PennID is 8 digits."""
        try:
            validate_pennid(self.user.pennid)
        except ValidationError:
            msg = "Unexpectedly failed to validate PennID '{}'."
            self.fail(msg)

    def test_pennid_is_invalid(self):
        # Can't have letters
        self.assertRaises(ValidationError, validate_pennid, 'abc')
        # Can't be less than 8 characters
        self.assertRaises(ValidationError, validate_pennid, '837291')
        # Can't be more than 8 characters
        self.assertRaises(ValidationError, validate_pennid, '820392992')

    def test_email_is_valid(self):
        """Ensure email address looks right."""
        # Django's core validator will raise an exception on failure; let's make sure.
        from django.core.exceptions import ValidationError
        self.assertRaises(ValidationError, validate_email, ["xxx"])
        # Email address should be valid.
        validate_email(self.user.email)


class TestPennUserStaffAttributes(TestCase):

    def setUp(self):
        self.user = PennUserStaffFactory()

    def test_user_is_staff(self):
        self.assertTrue(self.user.username)
        self.assertTrue(self.user.is_staff)
        self.assertFalse(self.user.is_admin)


class TestPennUserAdminAttributes(TestCase):

    def setUp(self):
        self.user = PennUserAdminFactory()

    def test_user_is_admin(self):
        self.assertTrue(self.user.username)
        self.assertTrue(self.user.is_admin)
        self.assertTrue(self.user.is_staff)
