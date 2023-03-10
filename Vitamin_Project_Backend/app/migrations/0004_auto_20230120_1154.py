# Generated by Django 4.1.5 on 2023-01-12 04:22

from django.db import migrations


class Migration(migrations.Migration):
    def initiateData(self, schema_editor):

        import pandas as pd
        from app.models import SunshineAvailability, Zones, Spices, FoodAllergy
        xls = pd.ExcelFile('app/data/Vitamin D (1).xlsx')
        xls1 = pd.ExcelFile('app/data/Spices.xlsx')
        xls2 = pd.ExcelFile('app/data/Common Food Allergies.xlsx')

        df1 = pd.read_excel(xls, 'Vitamin D Strength')
        df2 = pd.read_excel(xls, 'Zones')

        df3 = pd.read_excel(xls1, 'Sheet1')
        df4 = pd.read_excel(xls2, 'Allergies')
        df3 = df3.astype(object).where(df3.notna(), None)
        df4 = df4.astype(object).where(df4.notna(), None)

        for df2 in df2.itertuples():
            obj1 = Zones.objects.create(id=df2.ZoneID, LatitudeMin=df2.LatitudeMin, LatitudeMax=df2.LatitudeMax,
                                        NorthSouth=df2.NorthSouth)
            obj1.save()

        for df1 in df1.itertuples():
            zones = Zones.objects.get(id=df1.ZoneID)
            obj = SunshineAvailability(ZoneID=zones, Month=df1.Month, Strength=df1.Strength)
            obj.save()

        for df3 in df3.itertuples():
            obj1 = Spices.objects.create(id=df3.ID, spice_name=df3.Name, ingredients=df3.Ingredients,
                                         upc_code=df3.UPC_Code, size_quantity=df3.Size_Quantity,
                                         size_metric=df3.Size_Metric)
            obj1.save()

        for df4 in df4.itertuples():
            obj1 = FoodAllergy.objects.create(id=df4.ID, food_allergy_name=df4.Allergy,
                                              food_allergy_description=df4.Description)
            obj1.save()

    dependencies = [
        ('app', '0003_auto_20230120_1154'),
    ]

    operations = [
        migrations.RunPython(initiateData)
    ]
