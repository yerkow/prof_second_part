from django.db import models

# Create your models here.
class Vizit(models.Model):
    id = models.AutoField(primary_key=True)
    vizit = models.BigIntegerField()
    date = models.DateField(auto_now_add=True)

class Prof(models.Model):
    id = models.AutoField(primary_key = True)
    bin = models.CharField(max_length = 12)
    industry = models.CharField(max_length = 255)
    higher_union_org = models.CharField(max_length = 255)
    union_name = models.CharField(max_length = 255)
    union_type = models.CharField(max_length = 255)
    addres = models.TextField()
    phone = models.CharField(max_length=20)
    website = models.TextField()
    email = models.CharField(max_length = 255)
    chairman_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.id

class Report(models.Model):
    id = models.AutoField(primary_key = True)
    prof_id = models.ForeignKey(Prof, on_delete = models.CASCADE)
    report_type = models.CharField(max_length = 255)
    creator = models.CharField(max_length = 255)
    document = models.TextField()
    status = models.CharField(max_length = 50)
    creation_date = models.DateField(auto_now_add = True)
    submission_date = models.DateField()
    acceptance_date = models.DateField()

class ProfCollegianBodies(models.Model):
    id = models.AutoField(primary_key = True)
    prof_id = models.ForeignKey(Prof, on_delete = models.CASCADE)
    body_type = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    union_ticket_number = models.CharField(max_length = 50)
    position = models.CharField(max_length = 255)
    role = models.CharField(max_length = 255)

class ProfMember(models.Model):
    id = models.AutoField(primary_key = True)
    prof_id = models.ForeignKey(Prof, on_delete = models.CASCADE)
    photo = models.TextField()
    name = models.CharField(max_length = 255)
    union_ticket_number = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 10)
    birth_date = models.DateField()
    position = models.CharField(max_length = 255)
    role = models.CharField(max_length = 255)
    education = models.CharField(max_length = 50)
    total_work_experience = models.DateField()
    org_work_experience = models.DateField()
    union_membership_date = models.DateField()
    awards_list = models.TextField()
    vacation_list = models.TextField()
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 255)

    def __str__(self):
        return self.id

class Awards(models.Model):
    id = models.AutoField(primary_key = True)
    prof_memeber_id = models.ForeignKey(ProfMember, on_delete = models.CASCADE)
    award_type = models.CharField(max_length = 255)
    award_date = models.DateField()

class Vacation(models.Model):
    id = models.AutoField(primary_key = True)
    prof_memeber_id = models.ForeignKey(ProfMember, on_delete = models.CASCADE)
    sanatorium = models.CharField(max_length = 255)
    vacation_date = models.DateField()

class SocialPartnershipAgreements(models.Model):
    id = models.AutoField(primary_key = True)
    prof_id = models.ForeignKey(Prof, on_delete = models.CASCADE)
    agreement_type = models.CharField(max_length = 255)
    start_date = models.DateField()
    end_date = models.DateField()