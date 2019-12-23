class State:
    current_context = None

    def __init__(self, context):
        self.current_context = context

    def trigger(self):
        return True


class StateContext:
    state = None
    current_state = None
    availableStates = {}

    def setState(self, newstate):
        try:
            self.current_state = self.availableStates[newstate]
            self.state = newstate
            self.current_state.trigger()
            return True

        except KeyError:
            return True
