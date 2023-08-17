import json
from django.core.management.base import BaseCommand
from countries.models import Country


class Command(BaseCommand):
    help = "Populate gas pricing data in the database"

    def handle(self, *args, **options):
        json_file_path = (
            "/home/phelps/Desktop/projects/gasPrices-api/website/output.json"
        )
        try:
            with open(json_file_path, "r") as json_file:
                gas_pricing_data = json.load(json_file)

            for country_data in gas_pricing_data["result"]:
                Country.objects.create(
                    name=country_data["country"],
                    lpg_locale=country_data["lpg"]["locale"],
                    lpg_euro=country_data["lpg"]["euro"],
                    diesel_locale=country_data["diesel"]["locale"],
                    diesel_euro=country_data["diesel"]["euro"],
                )
            self.stdout.write(
                self.style.SUCCESS("Successfully populated gas pricing data")
            )
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("Gas pricing data file not found"))
