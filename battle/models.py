# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone

import tweepy
from enchant.checker import SpellChecker
from enchant.tokenize import *
from datetime import datetime
from threading import Thread
from time import sleep


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
	num_typo1 = models.IntegerField(default=0, help_text='Number of typos in tweets with hashtag1, - Smaller is WINNER')
	num_typo2 = models.IntegerField(default=0, help_text='Number of typos in tweets with hashtag2')
	avg_length1 = models.FloatField(default=0, help_text='Average Length of tweets with hashtag1, - Bigger is WINNER')
	avg_length2 = models.FloatField(default=0, help_text='Average Length of tweets with hashtag2')
	frequency1 = models.FloatField(default=0, help_text='Frequency of tweets with hashtag1 (number of tweets per minute), - Bigger is WINNER')
	frequency2 = models.FloatField(default=0, help_text='Frequency of tweets with hashtag2')
	start_time = models.DateTimeField(help_text='Format: YYYY-MM-DD hh:mm:ss')
	end_time = models.DateTimeField(help_text='Format: YYYY-MM-DD hh:mm:ss')
	status = models.CharField(choices=STATUS, default='Initiated', max_length=20, help_text='')
	compare = models.CharField(choices=COMPARE_TYPE, default='Number of typos', max_length=50)
	winner = models.CharField(max_length=250, null=True, blank=True)


	def __str__(self):
		return self.name

	def save(self, **kwargs):
		is_new = self.pk is None
		super(Battle, self).save() 

		if is_new: 
			print '===== Battle Daemon: "%s"-%d Created =====' % (self.name, self.id)
			# run thread to get the result of the battle
			work_thread = Thread(target = do_battle, args = (self.id, ))
			work_thread.setDaemon(True)
			work_thread.start()		
			


auth = tweepy.OAuthHandler(settings.OAUTH_KEYS['consumer_key'], settings.OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

exclude_words = ['RSS', 'app', 'SEO', 'sewatch', 'webmaster', 'http', 'https', 'online', 'podcast', 'podcasts', 'aka', 'admin', 'pdf', 'hashtag', 'dol', 'CMS']

NUM_TWEETS = 50
INTERVAL = 15


class HashTagFilter(Filter):
	"""Filter skipping over hashtags.
	This filter skips any words matching the following regular expression:
	   
		   ^[#@]\w+…?$
		
	That is, any words that are Hashtags.
	"""
	_pattern = re.compile(ur"^[#@]\w+…?$", re.UNICODE)
	def _skip(self,word):
		if self._pattern.match(word):
			return True
		return False


class PronounFilter(Filter):
	"""Filter skipping over pronouns.
	This filter skips any words matching the following regular expression:
	   
		   ^[A-Z][a-z]+('s)?$
		
	That is, any words that are Pronouns.
	"""
	_pattern = re.compile(r"^[A-Z][a-z]+('s)?$")
	def _skip(self,word):
		if self._pattern.match(word):
			return True
		return False


def do_battle(battle_id):
	try:
		while(1):
			battle = Battle.objects.get(id=battle_id)
			print battle.start_time, '@@@@@@@@@'
			if battle.start_time < timezone.now() and battle.status != 'Started':
				battle.status = 'Started'
				battle.save()
				print '===== Battle: "%s" Started =====' % battle.name
			elif battle.end_time < timezone.now():
				battle.status = 'Finished'
				battle.save()
				print '===== Battle: "%s" Finished =====' % battle.name
				break

			if battle.status == 'Started':
				# for the first time
				if battle.avg_length1 == 0:
					battle.num_typo1, battle.avg_length1, battle.frequency1 = get_data(battle.tag1)
					battle.num_typo2, battle.avg_length2, battle.frequency2 = get_data(battle.tag2)
				else:
					num_typo, avg_length, frequency = get_data(battle.tag1)
					battle.num_typo1 += num_typo
					battle.avg_length1 += avg_length
					battle.frequency1 += frequency
					battle.avg_length1 /= 2
					battle.frequency1 /= 2

					num_typo, avg_length, frequency = get_data(battle.tag2)
					battle.num_typo2 += num_typo
					battle.avg_length2 += avg_length
					battle.frequency2 += frequency
					battle.avg_length2 /= 2
					battle.frequency2 /= 2
				if battle.compare == 'Number of typos':
					battle.winner = battle.tag1
					if battle.num_typo1 > battle.num_typo2:
						battle.winner = battle.tag2
				elif battle.compare == 'Length of tweets':
					battle.winner = battle.tag1
					if battle.avg_length1 < battle.avg_length2:
						battle.winner = battle.tag2
				else:
					battle.winner = battle.tag1
					if battle.frequency1 < battle.frequency2:
						battle.winner = battle.tag2

				battle.save()

			sleep(INTERVAL)			
	except Exception, e:
		raise e

def get_data(hashtag):
	chkr = SpellChecker("en_US",filters=[EmailFilter, URLFilter, WikiWordFilter, HashTagFilter, PronounFilter])

	for word in exclude_words:
		chkr.add(word)

	# cricTweet = tweepy.Cursor(api.search, q='#keyword', lang='en', since='2016-05-24', until='2016-05-25',).items()
	cricTweet = tweepy.Cursor(api.search, q='#'+hashtag, lang='en').items(NUM_TWEETS)

	index = 0
	num_typo = 0
	len_tweets = 0
	tweet_start_time = ''
	tweet_end_time = ''

	try:
		for tweet in cricTweet:
			if index == 0:
				tweet_start_time = tweet.created_at

			index += 1

			if index == NUM_TWEETS:
				tweet_end_time = tweet.created_at

			chkr.set_text(tweet.text)
			len_tweets += len(tweet.text)

			typos = [err.word for err in chkr]
			num_typo += len(typos)
	except tweepy.TweepError, e:
		print e, '##################'

	date_format = "%Y-%m-%d %H:%M:%S"
	a = datetime.strptime(str(tweet_end_time), date_format)
	b = datetime.strptime(str(tweet_start_time), date_format)
	delta = b - a
	minutes = delta.total_seconds() / 60

	return num_typo, len_tweets/NUM_TWEETS, NUM_TWEETS/minutes

