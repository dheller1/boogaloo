class GameFlowController:
    def __init__(self):
        self.current_phase = None

    def proceed(self):
        if not self.current_phase:
            return

        if self.current_phase.status == GamePhase.Status.ReadyToProceed:
            next = self.current_phase.finalize()
            next.initialize()
            self.current_phase = next


class GamePhase:
    class Status:
        NotYetActive = 0
        Active = 1
        ReadyToProceed = 2
        Finalized = 3

    def __init__(self, name):
        self.name = name
        self.next_phase = None
        self.next_phase_options = []
        self.status = GamePhase.Status.NotYetActive

    def determine_next_phase(self, *args):
        raise NotImplementedError()

    def finalize(self):
        assert self.status == GamePhase.Status.ReadyToProceed
        self.status = GamePhase.Status.Finalized
        return self.next_phase

    def initialize(self):
        assert self.status == GamePhase.Status.NotYetActive
        self.status = GamePhase.Status.Active


class FixedPhaseSequence(GamePhase):
    def __init__(self, name, phases):
        super().__init__(name)
        self.phases = phases

