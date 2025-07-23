from django.db import migrations


def seed_tasks(apps, schema_editor):
    AITaskType = apps.get_model('generation', 'AITaskType')
    tasks = [
        ('check_topic', 'Проверка темы'),
        ('normalize_topic', 'Нормализация и категоризация'),
        ('generate_outline', 'Генерация структуры курса'),
        ('generate_chapter', 'Генерация главы'),
        ('generate_quiz', 'Генерация теста'),
    ]
    for code, title in tasks:
        AITaskType.objects.get_or_create(code=code, defaults={'title': title})


class Migration(migrations.Migration):
    dependencies = [
        ('generation', '0003_aimodel_aitasktype_prompttemplate_airequestlog'),
    ]

    operations = [migrations.RunPython(seed_tasks)]
