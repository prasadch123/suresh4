from django.db import models

class LearnAI(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    whatsup=models.BigIntegerField()
    occupation = models.CharField(max_length=50)
    Looking=models.CharField(max_length=50)
    department1= models.CharField(max_length=15)
    department2 = models.CharField(max_length=50)
    department3 = models.CharField(max_length=50)
    department4 = models.CharField(max_length=50)
    department5 = models.CharField(max_length=50)
    department6 = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class LearnAI_2(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    whatsup=models.BigIntegerField()
    occupation = models.CharField(max_length=50)
    Looking=models.CharField(max_length=50)
    project= models.CharField(max_length=15)
    type1 = models.CharField(max_length=50)
    projects = models.CharField(max_length=50)
    student = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class LearnAI_3(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    whatsup=models.BigIntegerField()
    occupation = models.CharField(max_length=50)
    Looking=models.CharField(max_length=50)
    intern1= models.CharField(max_length=15)
    internship = models.CharField(max_length=50)
    time= models.CharField(max_length=50)

    def __str__(self):
        return self.email



class LearnAI_4(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    whatsup=models.BigIntegerField()
    occupation = models.CharField(max_length=50)
    Looking=models.CharField(max_length=50)
    job= models.CharField(max_length=15)
    job1= models.CharField(max_length=50)

    def __str__(self):
        return self.email

class LearnAI_5(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    whatsup=models.BigIntegerField()
    occupation = models.CharField(max_length=50)
    Looking=models.CharField(max_length=50)
    visa= models.CharField(max_length=15)
    visa1= models.CharField(max_length=50)
    country= models.CharField(max_length=50)

    def __str__(self):
        return self.email


class LearnAI_6(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    whatsup=models.BigIntegerField()
    occupation = models.CharField(max_length=50)
    Looking=models.CharField(max_length=50)
    job_assi= models.CharField(max_length=15)
    job_assi1= models.CharField(max_length=50)

    def __str__(self):
        return self.email
