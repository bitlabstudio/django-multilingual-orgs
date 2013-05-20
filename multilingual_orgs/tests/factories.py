"""Factories for the ``multilingual_orgs`` app."""
import factory

from django_libs.tests.factories import SimpleTranslationMixin

from ..models import (
    Organization,
    OrganizationPluginModel,
    OrganizationTranslation,
)


class OrganizationFactory(SimpleTranslationMixin, factory.Factory):
    """Factory for the ``Organization`` model."""
    FACTORY_FOR = Organization

    @staticmethod
    def _get_translation_factory_and_field():
        return (OrganizationTranslationFactory, 'organization')


class OrganizationPluginModelFactory(factory.Factory):
    """Factory for ``OrganizationPluginModel`` objects."""
    FACTORY_FOR = OrganizationPluginModel

    display_type = 'small'
    organization = factory.SubFactory(OrganizationFactory)


class OrganizationTranslationFactory(factory.Factory):
    """Factory for ``OrganizationTranslation`` objects."""
    FACTORY_FOR = OrganizationTranslation

    title = factory.Sequence(lambda n: 'my org title {0}'.format(n))
    organization = factory.SubFactory(OrganizationFactory)
    language = 'en'
