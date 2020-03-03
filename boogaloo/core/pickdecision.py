from boogaloo.core.decision import Decision


class PickDecision(Decision):
    def __init__(self, options, required_choices=1):
        assert 1 <= required_choices <= len(options)
        self.options = options
        self.required_choices = required_choices
        self.result = None

    def decide(self, picks):
        if len(picks) != self.required_choices:
            raise ValueError('wrong number of choices')
        self.result = picks


class ConsolePickDecider:
    def __init__(self, decision):
        self.decision = decision
        self.options = [opt for opt in decision.options]
        self.picks = []

    def run(self):
        while len(self.picks) < self.decision.required_choices:
            left_to_pick = self.decision.required_choices - len(self.picks)
            print(f'Choose {left_to_pick} options:')
            for i, opt in enumerate(self.options):
                print(f' [{i+1}] - {opt}')

            user_choice = -1
            while user_choice not in range(len(self.options)):
                try:
                    user_choice = int(input('Choice: ')) - 1
                except ValueError:
                    pass

            self.picks.append(self.options.pop(user_choice))

        return self.picks
