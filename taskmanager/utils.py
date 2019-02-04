from mezzanine.models import Projects


def get_all_projects_enumerated():
    choices = [("Нет", "Нет")]
    for project in Projects.objects.all():
        choices.append((project.title, project.title))

    return choices