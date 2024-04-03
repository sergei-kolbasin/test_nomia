from django.db import models
from django.utils.translation import gettext_lazy as _


class Institution(models.Model):
    """
    Модель заведения
    """
    class Meta:
        verbose_name_plural = _("Заведения")
        verbose_name = _("Заведение")

    name = models.CharField(max_length=255, null=False, unique=True, verbose_name=_('Название заведения'))
    city_country = models.CharField(max_length=255, null=False, verbose_name=_('Страна и город'))
    address = models.CharField(max_length=200, null=False, unique=True, verbose_name=_('Адрес'))
    business_type = models.CharField(max_length=50, null=False, blank=True, verbose_name=_('Тип бизнеса'))
    direction = models.CharField(max_length=50, null=False, blank=True, verbose_name=_('Направление'))
    service_type = models.CharField(max_length=50, null=False, blank=True, verbose_name=_('Тип сервисов'))

    def __str__(self):
        return (f"Название заведения - {self.name}\n"
                f"Тип бизнеса - {self.business_type})\n"
                f"Направление - {self.direction}")


class Question(models.Model):
    """
    Модель вопроса
    """
    class Meta:
        verbose_name_plural = _("Вопросы")
        verbose_name = _("Вопрос")

    title = models.CharField(max_length=255, verbose_name=_('Заголовок'))
    comment = models.TextField(null=True, blank=True, verbose_name=_('Дополнительный комментарий'))

    def __str__(self):
        return f"Вопрос - '{self.title}'"


def answer_image_directory_path(instance: "Answer", filename: str) -> str:
    return "answers_pictures/{filename}".format(
        answer=instance.text,
        filename=filename,
    )


class Answer(models.Model):
    """
    Модель ответа
    """
    class Meta:
        verbose_name_plural = _("Ответы")
        verbose_name = _("Ответ")

    text = models.CharField(max_length=255)
    clarification = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Уточнение"),
    )
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to=answer_image_directory_path,
        verbose_name=_("Картинка"),
    )

    def __str__(self):
        return self.text


class Survey(models.Model):
    """
    Модель опроса
    """
    class Meta:
        verbose_name_plural = _("Опросы")
        verbose_name = _("Опрос")

    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("Вопрос"), related_name='surveys')
    answers = models.ManyToManyField(Answer, verbose_name=_("Ответы"))