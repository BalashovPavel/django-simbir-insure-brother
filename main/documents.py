from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from main.models import Insurance, Category
from user.models import CompanyProfile


@registry.register_document
class InsuranceDocument(Document):
    # company = fields.ObjectField(properties={
    #     'company_name': fields.TextField()
    # })
    # category = fields.ObjectField(properties={
    #     'category_name': fields.TextField()
    # })

    class Index:
        name = 'insurance'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Insurance

        fields = [
            'description',
            # 'interest_rate',
            # 'insurance_amount',
        ]
        # related_models = [CompanyProfile, Category]

    # def get_queryset(self):
    #     return super(InsuranceDocument, self).get_queryset().select_related(
    #         'company', 'category'
    #     )
    #
    # def get_instances_from_related(self, related_instance):
    #     if isinstance(related_instance, CompanyProfile):
    #         return related_instance.insurance
    #     if isinstance(related_instance, Category):
    #         return related_instance.insurance_set.all()
