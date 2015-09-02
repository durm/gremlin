# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from domains.models import Zone, Domain, DomainProto
from django.db import connection
import os
import re

class DomainTmp(DomainProto):
    pass

class Command(BaseCommand):
    
    args = '<fname> <zone>'

    def set_zone(self, zone):
        self.zone, created = Zone.objects.get_or_create(name=zone.lower())

    def handle(self, *args, **options):
        self.set_zone(args[1])
        fpath = os.path.abspath(args[0])
        critery = "name"
        tmp_tablename = DomainTmp._meta.db_table
        actual_tablename = Domain._meta.db_table
        with connection.cursor() as c:
            sql = connection.creation.sql_create_model(DomainTmp, self.style)[0][0]
            sql += """BULK INSERT {0} FROM {1} WITH (FIELDTERMINATOR = ' ', ROWTERMINATOR = '\\n') UPDATE {2} SET """
            sql += ", ".join(["{0} = {1}.{0}".format(f.name, tmp_tablename) for f in Domain._meta.fields if f.name != critery])
            sql += """ FROM {0} WHERE  {2}.{3} = {0}.{3};"""
            sql += """DROP TABLE {0};""".format(tmp_tablename)
            sql = sql.format(tmp_tablename, fpath, actual_tablename, critery)
            sql = re.sub(r"\^\[.+m", "", sql)
            self.stdout.write(sql)
            with open("r.sql", "w") as s:
                s.write(sql.decode("utf-8"))
            #c.execute(sql)
            self.stdout.write("Finished")
            
