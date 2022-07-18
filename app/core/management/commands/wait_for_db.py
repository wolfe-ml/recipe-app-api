"""
Django command to wait for bd to be available
"""
import time
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for db."""

    def handle(self, *args, **options):
        """Entrypoint for command."""

        self.stdout.write('Waiting for DB...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('DB unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
