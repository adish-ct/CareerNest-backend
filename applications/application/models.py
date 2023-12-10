from django.db import models
from common.base_models import DateBaseModel
from applications.accounts.models import User
from applications.jobs.models import Jobs


class Application(DateBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=25, null=True, blank=True)
    is_pending = models.BooleanField(default=True, blank=True)
    is_accept = models.BooleanField(default=False, blank=True)
    is_reject = models.BooleanField(default=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.job.job_role}'



