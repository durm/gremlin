# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from domains.models import Zone, Domain
from django.db import IntegrityError, transaction

BULK_SIZE = 1000

class Command(BaseCommand):
    
    args = '<fname> <zone>'

    def set_zone(self, zone):
        self.zone, created = Zone.objects.get_or_create(name=zone.lower())

    def parse_line(self, line):
        parts = line.split()
        return {
            parts[0]: {
                "registrer_date":parts[1], 
                "release_date":parts[2], 
                "registrator":parts[3]
            }
        }
            
    def store(self):
        with transaction.atomic():
            existed_domains = Domain.objects.filter(name__in=self.names.keys())
            for domain in existed_domains:
                cproto = self.names[domain.name]
                domain.update(cproto)
                domain.save()
                self.names.pop(domain.name)
            for key, value in self.names.items():
                self.bulk.append(
                    Domain(
                        name=key, 
                        zone=self.zone, 
                        registrer_date=value["registrer_date"],
                        release_date=value["release_date"],
                        registrator=value["registrator"]
                    )
                )
            if self.bulk:
                Domain.objects.bulk_create(self.bulk)
                del self.bulk[:]
            self.names.clear() 
            
    def handle(self, *args, **options):
        self.set_zone(args[1])
        with open(args[0]) as f:
            self.bulk = []
            self.names = {}
            for i, line in enumerate(f):
                dproto = self.parse_line(line)
                self.names.update(dproto)
                if i % BULK_SIZE == 0 :
                    self.store()
            self.store()