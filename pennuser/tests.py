#!/usr/bin/env python
from django.test import TestCase
from .factories import PennUserFactory, PennUserStaffFactory, PennUserAdminFactory
from django.core.validators import validate_email
import re


class TestPennUserAttributes(TestCase):

    def setUp(self):
        self.user = PennUserFactory()

    def test_default_user_permissions(self):
        """User should NOT be staff or admin by default."""
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_admin)

    def test_pennkey_is_valid(self):
        """Ensure username field is 3-8 alphanumeric characters."""
        # There should be NO capital letters.
        self.assertFalse(re.match(r'[A-Z]', self.user.username))
        self.assertTrue(re.match(r'[a-z0-9]{3,8}', self.user.username))

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
        self.assertTrue(self.user.is_staff)
        self.assertFalse(self.user.is_admin)


class TestPennUserAdminAttributes(TestCase):

    def setUp(self):
        self.user = PennUserAdminFactory()

    def test_user_is_admin(self):
        self.assertTrue(self.user.is_admin)
        self.assertTrue(self.user.is_staff)
