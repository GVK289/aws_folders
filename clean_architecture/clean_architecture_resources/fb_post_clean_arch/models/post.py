from django.db import models

from fb_post_clean_arch.models.user import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts')
    pub_date_time = models.DateTimeField(auto_now=True)
    post_content = models.CharField(max_length=250)

    def __str__(self):
        return "%s %s" % (self.user, self.post_content)
