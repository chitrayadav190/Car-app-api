from django.db import models

# Create your models here.

#docker-compose run app sh -c ""
class Car(models.Model):
    make_id=models.IntegerField(max_length=24, unique=False)
    make_name=models.CharField(max_length=100, unique=False)
    model_id=models.IntegerField(max_length=25,unique=True,primary_key=True)
    model_name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.model_name
class Rating(models.Model):
    # rating=(
    #     ('1', 'Poor'),
        #         ('2', 'Below Average'),
        #         ('3', 'Average'),
        #         ('4', 'Good'),
        #         ('5', 'Excellent'),
        #             )
    POOR=1
    BELOWAVERAGE=2
    AVERAGE=3
    GOOD=4
    EXCELLENT=5
    rating=(
        (POOR, 'Poor'),
        (BELOWAVERAGE, 'Below Average'),
        (AVERAGE, 'Average'),
        (GOOD, 'Good'),
        (EXCELLENT, 'Excellent'),
    )

    car=models.ForeignKey('Car',on_delete=models.CASCADE)
    car_rating=models.IntegerField(
        choices=rating,
        default=EXCELLENT,
    )

    def __str__(self):
        return "hello"
#
# class AccessRecord(models.Model):
#     car_record=models.ForeignKey('Rating',on_delete=models.CASCADE)
#     date=models.DateField()
#
#     def __str__(self):
#         return str(self.date)
#     'Categorie',
    # on_delete=models.CASCADE,
#
