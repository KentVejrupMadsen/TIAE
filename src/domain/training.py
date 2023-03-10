from src.misc.generate_case_name \
    import generate_case_name

from src.extensions.wandb.artifacts \
    import load \
    as load_dataset


class Training:
    def __init__(self):
        generated_case_name = generate_case_name()

    def execute(self):
        load_dataset()
        self.test()

    def test(self):
        pass

    def done(self):
        pass
