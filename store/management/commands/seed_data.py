import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Seeds the database with categories and products.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Creating categories...')
        fake = Faker('pt_BR')
        categories = ['Ração', 'Brinquedos', 'Higiene', 'Acessórios', 'Farmácia']
        created_categories = []
        for category_name in categories:
            category, created = Category.objects.get_or_create(
                name=category_name,
                slug=slugify(category_name)
            )
            created_categories.append(category)

        self.stdout.write('Creating products...')
        for _ in range(25):
            product_name = fake.unique.word().capitalize() + ' ' + random.choice(categories)
            Product.objects.create(
                category=random.choice(created_categories),
                name=product_name,
                slug=slugify(product_name),
                description=fake.paragraph(nb_sentences=5),
                price=round(random.uniform(15.00, 350.00), 2),
                stock=random.randint(10, 100),
                is_featured=random.random() < 0.2, # 20% chance
                image='products/placeholder.png'
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))
