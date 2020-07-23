from freezegun import freeze_time

from fb_post_clean_arch.constants.enums import ReactionType
from fb_post_clean_arch.interactors.storages.storage_interface import PostDto, \
    UserDto, ReactionDto, CommentDto
from fb_post_clean_arch.models import User, Post, Reactions, Comment


class CustomTestUtils:
    USERS = [
        {
            'username': 'user1',
            "name": "lakshmi",
            "profile_pic": "profile_pic1"
        },
        {
            'username': 'user2',
            "name": "lakshmi",
            "profile_pic": "profile_pic2"
        },
        {
            'username': 'user3',
            "name": "lakshmi",
            "profile_pic": "profile_pic3"
        },
        {
            'username': 'user4',
            "name": "lakshmi",
            "profile_pic": "profile_pic4"
        }
    ]

    POSTS = [
        {
            "user_id": 1,
            "post_content": "NEW POST1",
        },
        {
            "user_id": 1,
            "post_content": "NEW POST2",
        }
    ]

    POST_REACTIONS = [
        {
            "post_id": 1,
            "user_id": 1,
            "reaction_type": "LIKE",
            "comment_id": None
        }
    ]
    COMMENTS = [
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "nice post",
            "parent_comment_id": None
        },
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "great",
            "parent_comment_id": None
        },
        {
            "user_id": 1,
            "post_id": 1,
            "comment_content": "nice",
            "parent_comment_id": 2
        }
    ]

    COMMENTS_REACTIONS = [
        {
            "comment_id": 1,
            "post_id": None,
            "user_id": 1,
            "reaction_type": "SAD"
        }
    ]

    COMMENT_REPLIES = [
        {
            "user_id": 1,
            "post_id": None,
            "comment_content": "nice post",
            "parent_comment_id": 2
        }
    ]
    REPLY_REACTIONS = [
        {
            "comment_id": 2,
            "post_id": None,
            "user_id": 1,
            "reaction_type": "WOW"
        }
    ]

    def create_post_reactions(self):
        for reaction in self.POST_REACTIONS:
            Reactions.objects.create(post_id=reaction['post_id'],
                                     user_id=reaction['user_id'],
                                     reaction_type=reaction['reaction_type'])

    def create_posts(self):
        for post in self.POSTS:
            with freeze_time("22-04-2019"):
                Post.objects.create(
                    user_id=post['user_id'],
                    post_content=post['post_content']
                )

    def create_comments(self):
        for comment in self.COMMENTS:
            with freeze_time("22-04-2019"):
                Comment.objects.create(user_id=comment['user_id'],
                                       post_id=comment['post_id'],
                                       comment_text=comment['comment_content']
                                       )

    def create_comment_reactions(self):
        for reaction in self.COMMENTS_REACTIONS:
            Reactions.objects.create(comment_id=reaction['comment_id'],
                                     user_id=reaction['user_id'],
                                     reaction_type=reaction[
                                         'reaction_type'])

    def create_replies_for_comment(self):
        for reply in self.COMMENT_REPLIES:
            with freeze_time("22-04-2019"):
                Comment.objects.create(user_id=reply['user_id'],
                                       comment_text=reply['comment_content'],
                                       parent_comment_id=reply[
                                           'parent_comment_id'])

    def create_reply_reactions(self):
        for reaction in self.REPLY_REACTIONS:
            Reactions.objects.create(comment_id=reaction['comment_id'],
                                     user_id=reaction['user_id'],
                                     reaction_type=reaction['reaction_type'])

    def create_user(self):
        for user in self.USERS:
            User.objects.create(
                username=user['username'],
                name=user['name'],
                profile_pic=user['profile_pic']
            )

    @staticmethod
    def get_user_dtos():
        user_dtos = [UserDto(user_id=1,
                             name='lakshmi',
                             profile_pic='profile_pic1',
                             username='user1'),
                     UserDto(user_id=1,
                             name='lakshmi',
                             profile_pic='profile_pic1',
                             username='user1')]

        return user_dtos

    @staticmethod
    def get_reaction_dtos():
        reaction_dtos = [
            ReactionDto(reaction_id=2, comment=None, post_id=1, user_id=1,
                        reaction_type=ReactionType.LIKE.value),
            ReactionDto(reaction_id=1, comment=1, post_id=None, user_id=1,
                        reaction_type=ReactionType.SAD.value)
        ]

        return reaction_dtos

    @staticmethod
    def get_comment_dtos():
        comment_dtos = [
            CommentDto(comment_id=1,
                       user_id=1,
                       post_id=1,
                       comment_content='nice post',
                       pub_date_time='04-22-2019,00:00:1555871400.000000',
                       parent_comment=None),
            CommentDto(comment_id=2,
                       user_id=1,
                       post_id=1,
                       comment_content='great',
                       pub_date_time='04-22-2019,00:00:1555871400.000000',
                       parent_comment=None)
        ]
        return comment_dtos

    @staticmethod
    def get_post_dto():
        post_dtos = PostDto(
            post_id=1,
            user_id=1,
            post_content='NEW POST1',
            pub_date_time="04-22-2019,00:00:1555871400.000000"
        )
        return post_dtos

    @staticmethod
    def get_post():
        expected_get_post_details = [
            {
                'post_id': 1,
                'posted_by': {
                    'user_id': 1,
                    'user_name': 'user1',
                    'profile_pic': 'profile_pic1'
                },
                'posted_at': '04-22-2019,00:00:1555871400.000000',
                'post_content': 'NEW POST1',
                'reactions': {
                    'count': 0,
                    'type': [

                    ]
                },
                'comments': [
                    {
                        'comment_id': 1,
                        'commenter': {
                            'user_id': 1,
                            'user_name': 'user1',
                            'profile_pic': 'profile_pic1'
                        },
                        'commented_at': '04-22-2019,00:00:1555871400.000000',
                        'comment_content': 'nice post',
                        'reactions': {
                            'count': 1,
                            'type': [
                                'SAD'
                            ]
                        },
                        'replies_count': 0,
                        'replies': [
                            {

                            }
                        ]
                    },
                    {
                        'comment_id': 2,
                        'commenter': {
                            'user_id': 1,
                            'user_name': 'user1',
                            'profile_pic': 'profile_pic1'
                        },
                        'commented_at': '04-22-2019,00:00:1555871400.000000',
                        'comment_content': 'great',
                        'reactions': {
                            'count': 1,
                            'type': [
                                'WOW'
                            ]
                        },
                        'replies_count': 1,
                        'replies': [
                            {
                                'comment_id': 7,
                                'commenter': {
                                    'user_id': 1,
                                    'user_name': 'user1',
                                    'profile_pic': 'profile_pic1'
                                },
                                'commented_at': '04-22-2019,00:00:1555871400.000000',
                                'comment_content': 'nice post',
                                'reactions': {
                                    'count': 0,
                                    'type': [

                                    ]
                                }
                            }
                        ]
                    },
                    {
                        'comment_id': 3,
                        'commenter': {
                            'user_id': 1,
                            'user_name': 'user1',
                            'profile_pic': 'profile_pic1'
                        },
                        'commented_at': '04-22-2019,00:00:1555871400.000000',
                        'comment_content': 'nice',
                        'reactions': {
                            'count': 0,
                            'type': [

                            ]
                        },
                        'replies_count': 0,
                        'replies': [
                            {

                            }
                        ]
                    }
                ],
                'comments_count': 3
            },
            {
                'post_id': 2,
                'posted_by': {
                    'user_id': 1,
                    'user_name': 'user1',
                    'profile_pic': 'profile_pic1'
                },
                'posted_at': '04-22-2019,00:00:1555871400.000000',
                'post_content': 'NEW POST2',
                'reactions': {
                    'count': 0,
                    'type': [

                    ]
                },
                'comments': [
                    {
                        'comment_id': 4,
                        'commenter': {
                            'user_id': 1,
                            'user_name': 'user1',
                            'profile_pic': 'profile_pic1'
                        },
                        'commented_at': '04-22-2019,00:00:1555871400.000000',
                        'comment_content': 'nice post',
                        'reactions': {
                            'count': 0,
                            'type': [

                            ]
                        },
                        'replies_count': 0,
                        'replies': [
                            {

                            }
                        ]
                    },
                    {
                        'comment_id': 5,
                        'commenter': {
                            'user_id': 1,
                            'user_name': 'user1',
                            'profile_pic': 'profile_pic1'
                        },
                        'commented_at': '04-22-2019,00:00:1555871400.000000',
                        'comment_content': 'great',
                        'reactions': {
                            'count': 0,
                            'type': [

                            ]
                        },
                        'replies_count': 0,
                        'replies': [
                            {

                            }
                        ]
                    },
                    {
                        'comment_id': 6,
                        'commenter': {
                            'user_id': 1,
                            'user_name': 'user1',
                            'profile_pic': 'profile_pic1'
                        },
                        'commented_at': '04-22-2019,00:00:1555871400.000000',
                        'comment_content': 'nice',
                        'reactions': {
                            'count': 0,
                            'type': [

                            ]
                        },
                        'replies_count': 0,
                        'replies': [
                            {

                            }
                        ]
                    }
                ],
                'comments_count': 3
            }
        ]
        return expected_get_post_details
