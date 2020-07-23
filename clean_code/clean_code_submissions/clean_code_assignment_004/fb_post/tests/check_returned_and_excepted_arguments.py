def is_excepted_and_returned_output_of_posts_equal(returned_list,
                                                   expected_list):
    if returned_list:
        for index in range(len(returned_list)):
            check_posts(returned_list[index], expected_list[index])
    else:
        assert returned_list == expected_list
    return True


def check_posts(returned_list, expected_list):
    assert returned_list['post_id'] == expected_list['post_id']
    assert returned_list['posted_by']['user_id'] == expected_list[
        'posted_by']['user_id']
    assert returned_list['posted_by']['name'] == expected_list[
        'posted_by']['name']
    assert returned_list['posted_by']['profile_pic'] == expected_list[
        'posted_by']['profile_pic']
    assert returned_list['posted_at'] == expected_list['posted_at']
    assert returned_list['post_content'] == expected_list['post_content']
    assert returned_list['reactions'] == expected_list['reactions']
    assert check_comments(returned_list['comments'], expected_list['comments'])
    assert returned_list['comments_count'] == expected_list['comments_count']
    return True


def check_comments(returned, expected):
    if returned:
        for index in range(len(returned)):
            assert_statements_of_comments(returned[index], expected[index])
    else:
        assert returned == expected
    return True


def check_reactions(returned, expected):
    assert returned['count'] == expected['count']
    assert returned['type'] == expected['type']
    return True


def assert_statements_of_comments(returned, expected):
    assert returned['comment_id'] == expected['comment_id']
    assert returned['commenter']['user_id'] == expected['commenter'][
        'user_id']
    assert returned['commenter']['name'] == expected['commenter']['name']
    assert returned['commenter']['profile_pic'] == expected['commenter'][
        'profile_pic']
    assert returned['comment_content'] == expected['comment_content']
    assert check_reactions(returned['reactions'], expected['reactions'])
    assert returned['replies_count'] == expected['replies_count']
    assert check_replies(returned['replies'], expected['replies'])
    return True


def check_replies(returned, expected):
    if returned:
        for index in range(len(returned)):
            assert_statements_of_replies_for_comments(returned[index],
                                                      expected[index])
    else:
        assert returned == expected
    return True


def assert_statements_of_replies_for_comments(returned, expected):
    assert returned['comment_id'] == expected['comment_id']
    assert returned['commenter']['user_id'] == expected['commenter'][
        'user_id']
    assert returned['commenter']['name'] == expected['commenter']['name']
    assert returned['commenter']['profile_pic'] == expected['commenter'][
        'profile_pic']
    assert returned['comment_content'] == expected['comment_content']
    assert check_reactions(returned['reactions'], expected['reactions'])
    return True
