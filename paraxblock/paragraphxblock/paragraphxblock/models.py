from django.db import models

class Course(models.Model):

    course_name = models.TextField(max_length=100,default="")

    # def __repr__(self):
    #     return u"<Dict1XBlock_Course id={self.id} " \
    #         "course id={self.course_id} " \
    #         "course name={self.course_name}>".format(self=self)

    class Meta: 
        verbose_name = "course"
        verbose_name_plural = "course"
        ordering = ['course_name']

class Lessons(models.Model):
    course = models.ForeignKey(Course)
    lesson_name = models.TextField(max_length=100,default="")
    paragraph = models.TextField(max_length=1000,default="")
    
    def __repr__(self):
        return u"<Lessons id={self.id} " \
            "lesson name={self.lesson_name} " \
            "paragraph={self.paragraph}>".format(self=self)

    class Meta: 
        verbose_name = "lesson"
        verbose_name_plural = "lesson"
        ordering = ['course','lesson_name','paragraph']

class KeyDefinition(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    # key_id = models.CharField(max_length=100,unique=True)
    keyword = models.TextField(max_length=100,default="")
    defination = models.TextField(max_length=1000,default="")
    
    # def __repr__(self):
    #     return u"<Dict1XBlock_Key id={self.id} " \
    #         "keyword ={self.keyword} " \
    #         "defination={self.defination}>".format(self=self)

    class Meta: 
        verbose_name = "keyword"
        verbose_name_plural = "keyword"
        ordering = ['lesson','keyword','defination']