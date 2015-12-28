import datetime

from django.utils import timezone
from django.utils.html import escape
from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name = u'Source'
        verbose_name_plural = u'Sources'
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def set_url(self, value):
        if 'http://' not in value and 'https://' not in value and len(value) > 0:
            self.url = u'http://{0}'.format(value)
        else:
            self.url = value

class Review(models.Model):
    UNPUBLISHED = u'U'
    PUBLISHED = u'P'
    REVIEW_STATUS = (
        (UNPUBLISHED, u'Unpublished'),
        (PUBLISHED, u'Published'),
        )

    name = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    objective = models.TextField(max_length=1000)
    sources = models.ManyToManyField(Source)
    status = models.CharField(max_length=1, choices=REVIEW_STATUS, default=UNPUBLISHED)
    co_authors = models.ManyToManyField(User, related_name='co_authors')
    quality_assessment_cutoff_score = models.FloatField(default=0.0)
    population = models.CharField(max_length=200, blank=True)
    intervention = models.CharField(max_length=200, blank=True)
    comparison = models.CharField(max_length=200, blank=True)
    outcome = models.CharField(max_length=200, blank=True)
    context = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = u'Review'
        verbose_name_plural = u'Reviews'
        unique_together = (('name', 'author'),)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('review', args=(str(self.author.username), str(self.name)))

    def get_questions(self):
        questions = Question.objects.filter(review__id=self.id)
        return questions

    def get_inclusion_criterias(self):
        return SelectionCriteria.objects.filter(review__id=self.id, criteria_type='I')

    def get_exclusion_criterias(self):
        return SelectionCriteria.objects.filter(review__id=self.id, criteria_type='E')

    def get_keywords(self):
        return Keyword.objects.filter(review__id=self.id, synonym_of=None)

    def is_author_or_coauthor(self, user):
        if user.id == self.author.id:
            return True
        for co_author in self.co_authors.all():
            if user.id == co_author.id:
                return True
        return False

    def get_generic_search_string(self):
        try:
            search_string = SearchSession.objects.filter(review__id=self.id, source=None)[:1].get()
        except SearchSession.DoesNotExist:
            search_string = SearchSession(review=self)
        return search_string

    def get_latest_source_search_strings(self):
        return self.searchsession_set.exclude(source=None).order_by('source__name')

    def get_source_articles(self, source_id=None):
        if source_id is None:
            return Article.objects.filter(review__id=self.id)
        else:
            return Article.objects.filter(review__id=self.id, source__id=source_id)

    def get_duplicate_articles(self):
        articles = Article.objects.filter(review__id=self.id).exclude(status=Article.DUPLICATED).order_by('title')
        grouped_articles = dict()

        for article in articles:
            slug = slugify(article.title)
            if slug not in grouped_articles.keys():
                grouped_articles[slug] = { 'size': 0, 'articles': list() }
            grouped_articles[slug]['size'] += 1
            grouped_articles[slug]['articles'].append(article)

        duplicates = list()
        for slug, data in grouped_articles.iteritems():
            if data['size'] > 1:
                duplicates.append(data['articles'])

        return duplicates

    def get_accepted_articles(self):
        return Article.objects.filter(review__id=self.id, status=Article.ACCEPTED)

    def get_final_selection_articles(self):
        accepted_articles = Article.objects.filter(review__id=self.id, status=Article.ACCEPTED)
        if self.has_quality_assessment_checklist() and self.quality_assessment_cutoff_score > 0.0:
            articles = accepted_articles
            for article in accepted_articles:
                if article.get_score() <= self.quality_assessment_cutoff_score:
                    articles = articles.exclude(id=article.id)
            return articles
        else:
            return accepted_articles

    def has_quality_assessment_checklist(self):
        has_questions = self.qualityquestion_set.exists()
        has_answers = self.qualityanswer_set.exists()
        return has_questions and has_answers

    def get_data_extraction_fields(self):
        return DataExtractionField.objects.filter(review__id=self.id)

    def get_quality_assessment_questions(self):
        return QualityQuestion.objects.filter(review__id=self.id)

    def get_quality_assessment_answers(self):
        return QualityAnswer.objects.filter(review__id=self.id)

    def calculate_quality_assessment_max_score(self):
        try:
            questions_count = QualityQuestion.objects.filter(review__id=self.id).count()
            higher_weight_answer = QualityAnswer.objects.filter(review__id=self.id).order_by('-weight')[:1].get()
            if questions_count and higher_weight_answer:
                return questions_count * higher_weight_answer.weight
            else:
                return 0.0
        except:
            return 0.0
