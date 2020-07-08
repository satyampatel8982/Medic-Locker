from django.db import models

# Create your models here.

class DocterInfo(models.Model) :
    docid           = models.AutoField(primary_key=True)
    phone           = models.CharField(max_length = 10 , verbose_name = "Phone Number")
    address         = models.CharField(max_length = 255 , verbose_name = "Enter you Address ")
    qualification   = models.CharField(max_length = 50 , verbose_name = "| All Degree Qualification |")
    Specifiaction   = models.CharField(max_length = 100 , blank = True , null = True )
    WorkingHosp     = models.CharField(max_length = 200 , verbose_name = "Current Working Hospital / Clinic Address " )
    WorkExp         = models.CharField(max_length = 200 , verbose_name = "Working Experience ")
        # this is work Experience of the Doctor
    def __str__(self):
        return str(self.docid)

    class Meta:
        ordering = ['docid']

class PatInfo(models.Model):
    patid        = models.AutoField(primary_key=True)
    Email        = models.EmailField(blank = True , null = True )
    phone        = models.CharField(max_length = 10 , verbose_name ="Phone Number")
    altphone     = models.CharField(max_length = 10 , verbose_name = "Alternative Phone Number")
    addharNumber = models.CharField(max_length = 16 , verbose_name = "Enter Addhar Number ")
    city         = models.CharField(max_length = 255 , verbose_name = "Current Living City ")
    state        = models.CharField(max_length = 255 , verbose_name = "Current living State ")
    country      = models.CharField(max_length = 255 , verbose_name = "Enter Your Country")
    address      = models.CharField(max_length = 255 , verbose_name = "Enter you Address ")
    # ## ## ## _____________  other human related information _____________  ## ## ## #
    fingerPrint  = models.CharField(max_length = 155)
    eyeScan      = models.CharField(max_length = 155)
    altergy      = models.CharField(max_length = 155 , blank = True, null = True )
    area = (
          ('Dump','Dump Area'),
          ('Indus','Industrial Area'),
          ('N','Fress / Normal'),
          )
    surrounding  = models.CharField(max_length=5,choices=area , default='2')
    level = (
          ('1','Low'),
          ('2','Normal'),
          ('3','High'),
          )
    sugarlevel   = models.CharField(max_length=1 , choices= level , default='2')
    bp           = models.CharField(max_length = 155)
    bloodgroup   = models.CharField(max_length = 155)

    def __str__(self):
         return str(self.patid)

    class Meta :
         ordering = ['patid']
