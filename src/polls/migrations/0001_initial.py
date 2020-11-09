from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    
    initial = True
    
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    
    operations = [
        migrations.CreateModel(
            name="Choice",
            fields=[(
                "id",
                models.AutoField(
                    auto_created = True,
                    primary_key = True,
                    serialize = True,
                    verbose_name = "ID"
                    ),
                ),
                (
                "choice_text",
                models.CharField(max_length = 250)),
                ],
            ),
        migrations.CreateModel(
            name = "Poll",
            fields = [(
                "id",
                models.AutoField(
                    auto_created = True,
                    primary_key = True,
                    serialize = True,
                    verbose_name = "ID"
                    ),
                ),
                ("question",models.CharField(max_length = 250)),
                ("publication_date", models.DateTimeField(auto_now = True))
                ],
            ),
        migrations.CreateModel(
            name = "Vote",
            fields = [(
                "id",
                models.AutoField(
                    auto_created = True,
                    primary_key = True,
                    serialize = True,
                    versbose_name = "ID"
                        ),
                    ),
                (
                "choice",
                models.ForeignKey(
                    on_delete = django.db.models.deletion.CASCADE,
                    related_name = "votes",
                    to = "polls.Choice"
                        ),
                    ),
                (
                "poll",
                models.ForeignKey(
                    on_delete = django.db.models.deletion.CASCADE,
                    to = "polls.Poll"
                        ),
                    ),
                (
                "voted_by",
                models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                        ),    
                    ),
                ],
            ),
        
        migrations.AddField(
            model_name= "choice",
            name = "poll",
            field = models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="choices",
                to="polls.Poll",
                ),
            ),
        
        migrations.AlterUniqueTogether(
            name="vote", unique_together={("poll", "voted_by")}
        ),
        ]