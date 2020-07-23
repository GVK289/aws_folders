# Generated by Django 3.0 on 2020-04-16 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('commented_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('posted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_pic', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction', models.CharField(choices=[('WOW', 'WOW'), ('LIT', 'LIT'), ('LOVE', 'LOVE'), ('HAHA', 'HAHA'), ('THUMBS-UP', 'THUMBS-UP'), ('THUMBS-DOWN', 'THUMBS-DOWN'), ('ANGRY', 'ANGRY'), ('SAD', 'SAD')], max_length=100)),
                ('reacted_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='fb_post.Comment')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='fb_post.Post')),
                ('reacted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='fb_post.User')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(related_name='commented_to_post', through='fb_post.Comment', to='fb_post.User'),
        ),
        migrations.AddField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='fb_post.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fb_post.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply_to_comment', to='fb_post.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='fb_post.Post'),
        ),
    ]
