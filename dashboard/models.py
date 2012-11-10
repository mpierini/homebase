from django.db import models
from django.contrib.auth.models import User
import django.forms as forms


class Team(models.Model):
    '''Information for individual teams.'''
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    sport = models.CharField(max_length=64)
    membership = models.CharField(max_length=300)
    location = models.CharField(max_length=200)
    logo = models.ImageField()
    blog = models.CharField(max_length=600)


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'sport', 'membership', 'location', 'logo', 'blog')


class Social(models.Model):
    '''Collection of social media information for each team.'''
    sid = models.AutoField(primary_key=True)
    tid = models.ForeignKey(Team)
    facebook_url = models.CharField(max_length=200)
    twitter_url = models.CharField(max_length=200)
    homepage_url = models.CharField(max_length=200)
    photobook_url = models.CharField(max_length=200)


class TeamForm(forms.ModelForm):

    class Meta:
        model = Social
        fields = ('facebook_url', 'twitter_url', 'homepage_url', 'photobook_url')


class Membership(models.Model):
    '''Membership, linking individual users and their
    relationship to each team.'''
    mid = models.AutoField(primary_key=True)
    tid = models.ForeignKey(Team)
    uid = models.ForeignKey(User)
    admin = models.BooleanField(default=False)
    position = models.CharField(max_length=100)
    notes = models.CharField(max_length=200)


class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        fields = ('admin', 'position', 'notes')


class Game(models.Model):
    '''Individual games, linking to teams and scores.'''
    gid = models.AutoField(primary_key=True)
    tid = models.ForeignKey(Team)
    score = models.CharField(max_length=50)
    vs = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    time = models.DateTimeField()
    notes = models.CharField(max_length=400)


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('vs', 'date', 'time', 'location', 'score', 'notes')


class Player(models.Model):
    pid = models.AutoField(primary_key=True)
    gid = models.ForeignKey(Game)
    uid = models.ForeignKey(User)
    position = models.CharField(max_length=50)
    attending = models.BooleanField(default=False)
    notes = models.CharField(max_length=200)


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('position', 'attending')
