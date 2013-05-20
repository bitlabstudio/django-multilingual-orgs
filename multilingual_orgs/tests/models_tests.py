"""Tests for the models of the ``multilingual_orgs`` app."""
from django.test import TestCase

from .factories import (
    OrganizationFactory,
    OrganizationPluginFactory,
    OrganizationTranslationFactory,
)


class OrganizationTestCase(TestCase):
    """Tests for the ``Organization`` model."""
    longMessage = True

    def test_model(self):
        obj = OrganizationFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
        self.assertTrue(obj.get_translation(), msg=(
            'The factory should also create a translation'))


class OrganizationPluginTestCase(TestCase):
    """Tests for the ``OrganizationPlugin`` model."""
    longMessage = True

    def test_model(self):
        obj = OrganizationPluginFactory()
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))


class OrganizationTranslationTestCase(TestCase):
    """Tests for the ``OrganizationTranslation`` model."""
    longMessage = True

    def test_model(self):
        """Test instantiation of the ``OrganizationTranslation`` model."""
        obj = OrganizationTranslationFactory(title='my org')
        self.assertTrue(obj.pk, msg=(
            'Should be able to instantiate and save the model.'))
