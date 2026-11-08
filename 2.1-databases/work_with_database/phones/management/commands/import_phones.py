import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

from django.utils.text import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = csv.DictReader(file, delimiter=';')

            for phone in phones:
                phone_name = phone["name"]
                phone_slug = slugify(phone_name)

                phone = Phone(
                    id = phone["id"],
                    name = phone_name,
                    price = phone["price"],
                    image = phone["image"],
                    release_date = phone["release_date"],
                    lte_exists = phone["lte_exists"],
                    slug = phone_slug
                )
                phone.save()
        
        self.stdout.write(self.style.SUCCESS("Данные успешно загружены"))