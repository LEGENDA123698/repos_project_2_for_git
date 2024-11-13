from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)

    def str(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price_info = models.IntegerField()

    def __str__(self):
        return self.title


class Hall(models.Model):
    number_hall = models.IntegerField()
    all_number_rows = models.IntegerField()
    all_number_armchairs = models.IntegerField()

    def __str__(self):
        return f"{self.number_hall}"


class ArmChair(models.Model):
    hall_connection = models.ForeignKey(Hall, on_delete=models.CASCADE)
    number_row = models.IntegerField()
    number_armchair = models.IntegerField()

    def __str__(self):
        return f"Row {self.number_row}, Armchair {self.number_armchair}"


class Seance(models.Model):
    film_connection = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall_connection = models.ForeignKey(Hall, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.film_connection.title} at {self.time} on {self.date} in {self.hall_connection}"


class Ticket(models.Model):
    seance_connection = models.ForeignKey(Seance, on_delete=models.CASCADE)
    user_connection = models.ForeignKey(User, on_delete=models.CASCADE)
    armchair_connection = models.ForeignKey(ArmChair, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket for {self.seance_connection.film_connection.title} by {self.user_connection.name}"
