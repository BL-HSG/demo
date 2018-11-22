from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        data = [g.average_contribution for g in self.group.in_all_rounds()]
        series = [{'name': 'Contribution', 'type': 'column', 'data': data}]
        return {'series': series}


class End(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    Contribute,
    ResultsWaitPage,
    Results,
    End,
]
