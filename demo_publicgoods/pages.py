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
        series = []
        payoff_me = [p.payoff for p in self.player.in_all_rounds()]
        series.append({
            'name': 'Your Payoff',
            'data': payoff_me
        })

        for player in self.player.get_others_in_group():
            payoff_other = [p.payoff for p in player.in_all_rounds()]
            series.append({
                'name': 'Payoff other Player',
                'data': payoff_other
            })

        avg_contribution = [g.average_contribution for g in self.group.in_all_rounds()]
        series.append({
            'name': 'Average Contribution',
            'data': avg_contribution
        })

        return {
            'highcharts_series': series
        }


class End(Page):
    def vars_for_template(self):
        image1 = 'demo_publicgoods/smiley2.jpg'
        return {'image1': image1}

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    Intro,
    Contribute,
    ResultsWaitPage,
    Results,
    End,
]
