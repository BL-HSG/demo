from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'demo01'
    players_per_group = 3
    num_rounds = 3
    endowment = 100
    multiplier = 1.8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    average_contribution = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.average_contribution = self.total_contribution / Constants.players_per_group
        split_total_contribution = (self.total_contribution * Constants.multiplier) / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + split_total_contribution


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)
