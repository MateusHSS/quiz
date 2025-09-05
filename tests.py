import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_remove_invalid_choice_id():
    question = Question(title='q1')

    question.add_choice('a', True)

    with pytest.raises(Exception):
        question.remove_choice_by_id(3)

def test_remove_all_choices():
    question = Question(title='q1')

    question.add_choice('a', True)
    question.add_choice('b', False)

    assert len(question.choices) == 2

    question.remove_all_choices()

    assert len(question.choices) == 0

def test_set_correct_choice():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)

    question.set_correct_choices([1])

    choice = question.choices[0]
    choice2 = question.choices[1]

    assert choice.is_correct
    assert not choice2.is_correct 

def test_set_more_than_max_selections_correct_choices():
    question = Question(title='q1')

    question.add_choice('a', False)
    question.add_choice('b', False)

    with pytest.raises(Exception):
        question.set_correct_choices([1, 2, 3])

def test_set_invalid_correct_choice_id():
    question = Question(title='q1')

    question.add_choice('a', False)

    with pytest.raises(Exception):
        question.set_correct_choices([3])

def test_get_correct_selected_choices():
    question = Question(title='q1', points=1, max_selections=2)

    question.add_choice('a', False)
    question.add_choice('b', True)
    question.add_choice('c', True)

    selected_choices = [1, 2]

    assert question.correct_selected_choices(selected_choices) == [2]

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question('q1', points=-3)
    with pytest.raises(Exception):
        Question('q1', points=500)

def test_create_choice_with_invalid_text():
    question = Question('q1')

    with pytest.raises(Exception):
        question.add_choice('', False)

    with pytest.raises(Exception):
        question.add_choice('a'*300, True)

def test_remove_all_choices_from_question_with_no_choices():
    question = Question('q1')

    assert len(question.choices) == 0

    question.remove_all_choices()

    assert len(question.choices) == 0

def test_multiple_correct_choices_with_max_selections_1():
    question = Question('q1', points=1, max_selections=1)

    question.add_choice('a', True)
    question.add_choice('b', True)
    question.add_choice('c', False)

    assert question.correct_selected_choices([1]) == [1]

    assert question.correct_selected_choices([2]) == [2]
