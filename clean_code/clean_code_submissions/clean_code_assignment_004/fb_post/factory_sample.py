from datetime import datetime, timedelta
import random
import factory, factory.fuzzy
from .models import User, Post, Comment, Reaction
from .constants import ReactionType


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.Sequence(lambda n: 'vinay%d' % n)

    @factory.lazy_attribute
    def profile_pic(self):
        return '%s@example.com' % self.name


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    posted_by = factory.SubFactory(UserFactory)

    posted_at = factory.LazyFunction(datetime.now)

    @factory.sequence
    def content(n):
        return 'post content of post%d' % n

    # posted_by = factory.SubFactory(UserFactory,
    #     username=factory.LazyAttribute(
    #         lambda o: o.factory_parent.post_content))


class PostCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    commented_by = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    commented_at = factory.LazyFunction(datetime.now)
    parent_comment = None

    @factory.sequence
    def content(n):
        return 'comment content of comment%d' % n

class ReplyCommentFactory(PostCommentFactory):

    parent_comment = factory.Iterator(Comment.objects.all())

Reaction_Choices = (
    (ReactionType.LIT.value, ReactionType.LIT.value),
    (ReactionType.WOW.value, ReactionType.WOW.value),
    (ReactionType.HAHA.value, ReactionType.HAHA.value),
    (ReactionType.THUMBS_UP.value, ReactionType.THUMBS_UP.value),
    (ReactionType.THUMBS_DOWN.value, ReactionType.THUMBS_DOWN.value),
    (ReactionType.SAD.value, ReactionType.SAD.value),
    (ReactionType.ANGRY.value, ReactionType.ANGRY.value)
)
class PostReactionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reaction

    reacted_by = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    comment = None
    reacted_at = factory.LazyFunction(datetime.now)

    reaction = factory.fuzzy.FuzzyChoice(Reaction_Choices, getter=lambda c: c[0])

class CommentReactionsFactory(PostReactionsFactory):
    comment = factory.SubFactory(PostCommentFactory)


class ReplyCommentReactionsFactory(PostReactionsFactory):
    comment = factory.SubFactory(ReplyCommentFactory)
