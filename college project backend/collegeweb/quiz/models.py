from django.db import models
class catagory(models.Model):
    catagoty_name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.catagoty_name


class question(models.Model):
    topic_name=models.ForeignKey(catagory,on_delete=models.CASCADE,related_name='Catagory')
    name=models.CharField(max_length=200,null=True)

    number=models.IntegerField(null=True)
    def __str__(self):
        return self.name
class answer(models.Model):
    Question=models.ForeignKey(question,on_delete=models.CASCADE,related_name='Question')
    name=models.CharField(max_length=100)
    isCorrect=models.BooleanField(default=False)
    def __str__(self):
        return self.name
