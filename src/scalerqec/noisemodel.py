#A Noise model calss
#Rewrite all stim program/Clifford circuit to support the noise model





class NoiseModel:
    """
    A class representing a noise model for quantum error correction simulations.
    """


    def __init__(self, error_rates: float, has_measurement_error: bool, has_reset_error: bool) -> None:
        self._error_rates = error_rates
        self._has_measurement_error = has_measurement_error
        self._has_reset_error = has_reset_error


    def rewrite_stim_program(self, stim_program) -> str:
        """
        Rewrite a given stim program to incorporate the noise model.

        Args:
            stim_program: The original stim program to be modified.

        Returns:
            A new stim program with the noise model applied.
        """
        # Placeholder for actual implementation
        return stim_program



    def uniform_depolarization_single(stim_program: str) -> str:
        """
        Apply uniform depolarization noise to single-qubit operations in the stim program.

        Args:
            stim_program (str): The original stim program. 

        Returns:
            str: The modified stim program with depolarization noise applied.

        # Placeholder for actual implementation
        """
        return stim_program

