from django.db import models
from django.db.models.fields import CharField, IntegerField,DateField,TextField

class FundingBoard(models.Model):

    board_id = IntegerField(primary_key=True)
    user_id = CharField(max_length=30, null=True)
    title = CharField(max_length=30, null=True)
    content = TextField(null=True)
    fund_goal_price = IntegerField()
    fund_total_price = IntegerField()
    regi_date = DateField()

    
    class Meta:
        db_table = 'FundingBoard'
        app_label = 'fundingapp'
        managed = False