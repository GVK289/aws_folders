from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.URLField()


class Post(models.Model):
    content = models.CharField(max_length=1000)
    posted_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='post')
    # comment = models.ManyToManyField(User, through='Comment',
    #                                  related_name='commented_to_post')


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    commented_at = models.DateTimeField(auto_now=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE,
                                       null=True,
                                       related_name='reply_to_comment')


class Reaction(models.Model):
    react = (
        ('WOW', 'WOW'), ('LIT', 'LIT'),
        ('LOVE', 'LOVE'), ('HAHA', 'HAHA'),
        ('THUMBS-UP', 'THUMBS-UP'),
        ('THUMBS-DOWN', 'THUMBS-DOWN'),
        ('ANGRY', 'ANGRY'), ('SAD', 'SAD'))

    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True,
                             related_name='reactions')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True,
                                related_name='reactions')
    reaction = models.CharField(max_length=100, choices=react)
    reacted_at = models.DateTimeField(auto_now=True)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='reactions')
