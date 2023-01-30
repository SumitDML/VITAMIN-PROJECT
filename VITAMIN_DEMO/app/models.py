from django.db import models


class Tabs(models.Model):
    tabId = models.AutoField(primary_key=True, editable=False, name='tab_id')
    name = models.CharField(name='name', max_length=255)
    displayName = models.CharField(name='display_name', max_length=255)
    createdAt = models.DateTimeField(auto_now=True, name='created_at', null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, name='updated_at', null=True)

    class Meta:
        db_table = 'tabs'

    def __str__(self):
        return self.name


class TabChild(models.Model):
    tabChildId = models.AutoField(primary_key=True, editable=False, name='tab_child_id')
    name = models.CharField(name='name', max_length=255)
    displayName = models.CharField(name='display_name', max_length=255)
    tabs = models.ForeignKey(Tabs, on_delete=models.CASCADE, related_name='childs', name='tab', null=True)
    createdAt = models.DateTimeField(auto_now=True, name='created_at', null=True)
    updatedAt = models.DateTimeField(auto_now_add=True, name='updated_at', null=True)

    class Meta:
        db_table = 'tab_childs'

    def __str__(self):
        return self.name


class TabChildMappings(models.Model):
    tabId = models.ForeignKey(Tabs, on_delete=models.CASCADE, related_name='tabs', name='tab', null=True)
    tabChildId = models.ForeignKey(TabChild, on_delete=models.CASCADE, related_name='childs', name='tab_child',
                                   null=True)

    class Meta:
        db_table = 'tab_child_mappings'

    def __str__(self):
        return self.name


class Zones(models.Model):
    ZoneID = models.IntegerField(primary_key=True, editable=False, name='id')
    LatitudeMin = models.FloatField(name='LatitudeMin')
    LatitudeMax = models.FloatField(name='LatitudeMax')
    NorthSouth = models.CharField(max_length=1, name='NorthSouth')

    class Meta:
        db_table = 'zones'

    def __str__(self):
        return self.name


class SunshineAvailability(models.Model):
    sunshine_id = models.AutoField(primary_key=True, editable=False, name='id', null=False)
    Month = models.IntegerField(name='Month')
    Strength = models.IntegerField(name='Strength')
    ZoneID = models.ForeignKey('Zones', on_delete=models.CASCADE, related_name='strengths', name='ZoneID', null=True)

    class Meta:
        db_table = 'sunshine_availability'

    def __str__(self):
        return self.name


class ZipCodes(models.Model):
    zipCode = models.CharField(max_length=5, name='zip_code', primary_key=True, editable=False, null=False)
    latitude = models.FloatField(name='latitude', null=False)
    longitude = models.FloatField(name='longitude', null=False)

    class Meta:
        db_table = 'zip_codes'

    def __str__(self):
        return self.name


class FoodAllergy(models.Model):
    foodAllergyId = models.IntegerField(primary_key=True, editable=False, name='id')
    foodAllergyName = models.CharField(name='Allergy', max_length=255)
    allergyDescription = models.TextField(name='Description', null=True)

    class Meta:
        db_table = 'food_allergy'

    def __str__(self):
        return self.name


class Spices(models.Model):
    spiceId = models.IntegerField(primary_key=True, editable=False, name='id')
    spiceName = models.CharField(name='Name', max_length=255)
    ingredients = models.CharField(name='Ingredients', max_length=255)
    upcCode = models.CharField(name='UPC_Code', max_length=255)
    sizeQuantity = models.FloatField(name='Size_Quantity', null=True)
    sizeMetric = models.CharField(name='Size_Metric', null=True, max_length=255)
    imageUrl = models.TextField(name='Image_URL')
    recipesUrl = models.TextField(name='Recipes_URL', null=True)

    class Meta:
        db_table = 'spices'

    def __str__(self):
        return self.name


class Nutrients(models.Model):
    nutrientId = models.IntegerField(primary_key=True, editable=False, name='id')
    nutrient = models.CharField(name='Nutrient', max_length=255)
    parent = models.IntegerField(name='Parent', null=True)
    supplementName = models.CharField(name='Supplements_Name', max_length=255, null=True)
    foodNutritionName = models.CharField(name='Food_Nutrition_Name', max_length=255, null=True)
    active = models.BooleanField(name='Active', null=True)

    class Meta:
        db_table = 'Nutrients'

    def __str__(self):
        return self.name
