


from enum import Enum
from clifford import CliffordCircuit

class SCHEME(Enum):
    STANDARD = 0
    SHOR = 1
    KNILL = 2
    FLAG = 3




def commute(stab1: str, stab2: str) -> bool:
    """
    Check if two stabilizer generators commute.

    Args:
        stab1 (str): The first stabilizer generator.
        stab2 (str): The second stabilizer generator.

    Returns:
        bool: True if the stabilizers commute, False otherwise.
    """
    assert len(stab1) == len(stab2), "Stabilizers must be of the same length."
    anti_commute_count = sum(1 for a, b in zip(stab1, stab2) if a != 'I' and b != 'I' and a != b)
    return anti_commute_count % 2 == 0



"""
Current types of IR instructions.
TODO: Support repeat, conditional operations, etc. The IR should be stored as a tree structure.
"""
class IRType(Enum):
    PROP = 0
    DETECTOR = 1
    OBSERVABLE = 2
    IF_THEN = 3
    WHILE = 4
    REPEAT_UNTIL = 5


class IRInstruction:
    """
    A class representing an intermediate representation (IR) instruction for quantum circuits.
    """
    def __init__(self, instr_type: IRType, dest: str, args: list[str]) -> None:
        self._instr_type = instr_type
        self._dest = dest
        self._args = args


    def __str__(self) -> str:
        match self._instr_type:
            case IRType.PROP:
                return f"{self._dest} = Prop {' '.join(self._args)}"
            case IRType.DETECTOR:
                return f"{self._dest} = Parity {' '.join(self._args)}"
            case IRType.OBSERVABLE:
                return f"{self._dest} = Parity {' '.join(self._args)}"
            case _:
                raise NotImplementedError(f"IR type {self._instr_type} not implemented.")


    def get_dest_index(self) -> int:
        """
        Get the index of the destination qubit/observable/detector from the destination string.

        Returns:
            int: The index extracted from the destination string.
        """
        return int(self._dest[1:])  # Assumes dest is in the form 'c0', 'd1', 'o2', etc.


    def get_args_indices(self) -> list[int]:
        """
        Get the indices of the arguments from the argument strings.

        Returns:
            list[int]: A list of indices extracted from the argument strings.
        """
        return [int(arg[1:]) for arg in self._args]  # Assumes args are in the form 'c0', 'd1', 'o2', etc.



class QECStab:
    """
    A class representing a quantum error-correcting code (QECC) using the stabilizer formalism.
    """
    def __init__(self, n: int, k: int, d: int) -> None:
        self._n = n
        self._k = k
        self._d = d
        self._stabs = []
        self._scheme = SCHEME.STANDARD
        self._circuit = None
        self._IRList = []

    def add_stab(self, stab: str) -> None:
        """
        Add a stabilizer generator to the code.

        Args:
            stab (str): A string representation of the stabilizer generator.
        """
        assert len(stab) == self._n, "Stabilizer length must match number of qubits."
        assert all(c in 'IXYZ' for c in stab), "Stabilizer must only contain I, X, Y, Z."

        self._stabs.append(stab)


    def set_scheme(self, scheme: str) -> None:
        """
        Set the error correction scheme for the code.

        Args:
            scheme (SCHEME): The error correction scheme to use.
        """
        match scheme:
            case "Standard":
                self._scheme = SCHEME.STANDARD
            case "Shor":
                self._scheme = SCHEME.SHOR
            case "Knill":
                self._scheme = SCHEME.KNILL
            case "Flag":
                self._scheme = SCHEME.FLAG
            case _:
                raise ValueError(f"Unknown scheme: {scheme}")
            
    def construct_circuit(self):
        """
        Construct the quantum error-correcting circuit based on the stabilizers and scheme.

        There is a two step compilation:
             First, compile the stabilizers into an intermediate representation (IR) of the circuit.
             Second, translate the IR into a Clifford circuit.
             In IR, there is no concept of qubits, only Pauli operators, detectors, observables, and their relationships.
        The IR has the form:

        
        c0 = Prop XYZIX
        c1 = Prop IXYZI
        d0 = Parity c0 c1
        o0 = Parity c0   
        """
        pass



    def construct_IR_standard_scheme(self):
        """
        Construct the quantum error-correcting circuit using the standard scheme.
        Now, we will create the intermediate representation (IR) for the circuit.
        """
        self._circuit = CliffordCircuit(self._n)



    def show_IR(self):
        """
        Display the intermediate representation of the quantum error-correcting circuit.

        The IR has the form:
        """
        if self._circuit is None:
            raise ValueError("Circuit has not been constructed yet.")
        print(self._circuit)


    def compile_stim_circuit_from_IR(self) -> str:
        """
        Compile the stim circuit from the intermediate representation (IR).

        Returns:
            str: The compiled stim circuit as a string.
        """
        if self._circuit is None:
            raise ValueError("Circuit has not been constructed yet.")
        stim_circuit = ""
        # Placeholder for actual implementation
        return stim_circuit




def test_commute():
    assert commute("IXYZ", "IYZX") == False
    assert commute("XZZI", "ZXXI") == False
    assert commute("IIII", "ZZZZ") == True
    assert commute("XIZY", "YZXI") == True



if __name__ == "__main__":
    test_commute()