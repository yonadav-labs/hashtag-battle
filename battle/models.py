from __future__ import unicode_literals

from django.db import models


COMPARE_TYPE = (
	('Number of typos', 'Number of typos'),
	('Length of tweets', 'Length of tweets'),
	('Frequency of tweets', 'Frequency of tweets'),
)

STATUS = (
	('Initiated', 'Initiated'),
	('Started', 'Started'),
	('Finished', 'Finished'),
)

class Battle(models.Model):
	name = models.CharField(max_length=250, help_text='Battle Name')
	tag1 = models.CharField(max_length=250, help_text='Hashtag 1 - no # sign, no space')
	tag2 = models.CharField(max_length=250, help_text='Hashtag 2')
	num_typo1 = models.IntegerField(default=0, help_text='Number of typos in tweets with hashtag1, Smaller is winner.')
	num_typo2 = models.IntegerField(default=0, help_text='Number of typos in tweets with hashtag2')
	avg_length1 = models.IntegerField(default=0, help_text='Average Length of tweets with hashtag1, Bigger is winner.')
	avg_length2 = models.IntegerField(default=0, help_text='Average Length of tweets with hashtag2')
	frequency1 = models.IntegerField(default=0, help_text='Frequency of tweets with hashtag1, Bigger is winner.')
	frequency2 = models.IntegerField(default=0, help_text='Frequency of tweets with hashtag2')
	start_time = models.DateTimeField(help_text='Format: YYYY-MM-DD hh:mm:ss')
	end_time = models.DateTimeField(help_text='Format: YYYY-MM-DD hh:mm:ss')
	status = models.CharField(choices=STATUS, default='Initiated', max_length=20, help_text='')
	# compare = models.CharField(choices=COMPARE_TYPE, default='Number of typos', max_length=50)

	def __str__(self):
		return self.name

	# def save(self, **kwargs):
	# 	pass