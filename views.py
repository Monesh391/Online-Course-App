from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Question, Choice, Submission


def submit(request, course_id):

    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(lesson__course=course)

    submission = Submission.objects.create(question=questions.first())

    for question in questions:
        selected = request.POST.getlist(str(question.id))
        for choice_id in selected:
            choice = Choice.objects.get(id=choice_id)
            submission.selected_choices.add(choice)

    return HttpResponseRedirect(
        reverse('show_exam_result', args=(course.id, submission.id))
    )


def show_exam_result(request, course_id, submission_id):

    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.selected_choices.all()

    correct_answers = 0
    total_questions = Question.objects.filter(lesson__course=course).count()

    for choice in selected_choices:
        if choice.is_correct:
            correct_answers += 1

    context = {
        'course': course,
        'correct_answers': correct_answers,
        'total_questions': total_questions
    }

    return render(request, 'exam_result.html', context)
