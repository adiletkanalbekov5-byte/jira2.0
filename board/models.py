from django.db import models
from django.contrib.auth import get_user_model

# Получаем кастомную или стандартную модель пользователя
User = get_user_model()


class Task(models.Model):
    """
    Модель задачи для канбан-доски.
    Содержит информацию о названии, описании, назначенном пользователе,
    статусе, приоритете, сроках и порядке отображения.
    """

    # -----------------------------
    # Варианты статуса задачи
    # -----------------------------
    STATUS_CHOICES = [
        ('todo', 'To Do'),          # Задача не начата
        ('progress', 'In Progress'), # В работе
        ('done', 'Done'),           # Завершена
    ]

    # -----------------------------
    # Приоритет задачи
    # -----------------------------
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]

    # -----------------------------
    # Основные поля задачи
    # -----------------------------
    title = models.CharField(
        "Название задачи",
        max_length=200
    )

    description = models.TextField(
        "Описание",
        blank=True
    )

    # Назначенный исполнитель задачи
    assignee = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,   # Если юзер удалён → исполнитель станет NULL
        null=True,
        blank=True,
        verbose_name="Исполнитель"
    )

    # Даты старта и дедлайна задачи (необязательные)
    start_date = models.DateField(
        null=True,
        blank=True
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )

    # Статус задачи: todo / progress / done
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='todo'
    )

    # Приоритет: low / medium / high
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    # Автоматическое время создания записи
    created = models.DateTimeField(
        auto_now_add=True
    )

    # Автоматическое время последнего изменения записи
    updated = models.DateTimeField(
        auto_now=True
    )

    # Порядок задачи внутри своей колонки на канбан-доске
    order = models.PositiveIntegerField(default=0)

    # -----------------------------
    # Методы модели
    # -----------------------------
    def __str__(self):
        """Отображение задачи в админке и shell."""
        return self.title

    # -----------------------------
    # Метаданные модели
    # -----------------------------
    class Meta:
        ordering = ['status', 'order', '-priority']
        # Сначала сортируем по статусу (todo → progress → done)
        # затем по порядку внутри колонки
        # затем по приоритету (высокий выше)
