import math
import sys
import json
from typing import Any, Dict, List, Optional, Tuple, Callable
import tkinter as tk
from tkinter import ttk, messagebox

# --- Scientific Constants (Part of the "Knowns") ---
GRAVITY_EARTH = 9.80665  # m/s^2
R_GAS_CONSTANT = 8.314    # J/(mol·K)

class QuantumAlchemist:
    """
    Core engine for scientific and computational analysis.
    This class is the module's backend, providing all calculation methods.
    """

    # --- Domain-Specific Calculation Methods ---

    @staticmethod
    def solve_quadratic(a: float, b: float, c: float) -> Tuple[str, List[complex]]:
        """Solves ax^2 + bx + c = 0."""
        if a == 0: return "Error: 'a' cannot be zero.", []
        delta = (b**2) - (4 * a * c)
        if delta >= 0:
            root1 = (-b + math.sqrt(delta)) / (2 * a)
            root2 = (-b - math.sqrt(delta)) / (2 * a)
            return "Two real roots found.", [root1, root2]
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(abs(delta)) / (2 * a)
            root1 = complex(real_part, imaginary_part)
            root2 = complex(real_part, -imaginary_part)
            return "Two complex roots found.", [root1, root2]

    @staticmethod
    def solve_linear_system(a1: float, b1: float, c1: float, a2: float, b2: float, c2: float) -> Tuple[str, Optional[Tuple[float, float]]]:
        """Solves system: a1x + b1y = c1 and a2x + b2y = c2."""
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return "Error: Determinant is zero (no unique solution).", None
        
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return "Unique solution found.", (x, y)

    @staticmethod
    def calculate_molar_mass(formula_str: str, atomic_masses: Dict[str, float]) -> Optional[float]:
        """Calculates molar mass from a formula string (simplified)."""
        # Simple parser: expects elements followed by count (e.g., "H2O1")
        import re
        parsed_formula = re.findall('([A-Z][a-z]?)([0-9]*)', formula_str)
        
        molar_mass = 0.0
        for element, count_str in parsed_formula:
            count = int(count_str) if count_str else 1
            mass = atomic_masses.get(element)
            if mass is None:
                return None
            molar_mass += mass * count
        return molar_mass

    @staticmethod
    def calculate_kinetic_energy(mass_kg: float, velocity_mps: float) -> float:
        """Calculates E = 0.5 * m * v^2."""
        if mass_kg < 0 or velocity_mps < 0:
            raise ValueError("Mass and velocity must be non-negative.")
        return 0.5 * mass_kg * (velocity_mps ** 2)

    @staticmethod
    def calculate_potential_energy(mass_kg: float, height_m: float) -> float:
        """Calculates E = m * g * h (using Earth's gravity)."""
        if mass_kg < 0 or height_m < 0:
            raise ValueError("Mass and height must be non-negative.")
        return mass_kg * GRAVITY_EARTH * height_m
    
    @staticmethod
    def calculate_force(mass_kg: float, acceleration_mps2: float) -> float:
        """Calculates Force = mass * acceleration (F=ma)."""
        return mass_kg * acceleration_mps2

    @staticmethod
    def calculate_ideal_gas_pressure(moles: float, volume: float, temp_k: float) -> float:
        """Calculates P using PV=nRT."""
        return (moles * R_GAS_CONSTANT * temp_k) / volume

    # --- Computational Dissection Method (Knowing the Unknown) ---

    @staticmethod
    def decipher_computational_signature(data_input: Any) -> Dict[str, Any]:
        """
        Deciphers the core computational signature of an arbitrary Python object,
        providing granular data representation details (byte, bit, hex, binary).
        """
        try:
            if isinstance(data_input, (dict, list, tuple)):
                string_representation = json.dumps(data_input, sort_keys=True)
            elif isinstance(data_input, bytes):
                byte_representation = data_input
                string_representation = data_input.hex()
            else:
                string_representation = str(data_input)

            if not isinstance(data_input, bytes):
                byte_representation = string_representation.encode('utf-8')

        except Exception as e:
            return {"decipher_status": f"ERROR: Encoding failed: {e}"}

        byte_length = sys.getsizeof(data_input) if not isinstance(data_input, str) else len(byte_representation)
        bit_length = byte_length * 8
        hex_signature = byte_representation.hex()

        try:
            packed_integer = int.from_bytes(byte_representation, byteorder='big')
            binary_signature = bin(packed_integer)[2:]
        except (OverflowError, ValueError):
            binary_signature = ''.join(format(byte, '08b') for byte in byte_representation)

        return {
            "input_type": type(data_input).__name__,
            "byte_length_bytes": byte_length,
            "bit_length_total": bit_length,
            "hexadecimal_signature": hex_signature,
            "binary_signature": binary_signature,
            "decipher_status": "Success"
        }

    # --- Algorithmic Utility (35 Input Placeholder Fulfillment) ---

    def apply_complex_algorithm(self, numerical_inputs: List[float], complexity_factor: float = 1.0) -> float:
        """
        Applies a functional mathematical expression (wave modulation,
        logarithmic decay, and index-based exponentiation) to 10 inputs.
        """
        total_sum = 0.0
        n = len(numerical_inputs)
        if n == 0:
            return 0.0

        for i, x in enumerate(numerical_inputs):
            # Complex expression: Sine wave modulation, logarithmic decay, and index-based exponentiation
            term = (x * math.sin((i + 1) * math.pi / n)) + math.log1p(abs(x) + 1)
            total_sum += term ** ((i + 1) / n + 1)

        result = total_sum * complexity_factor
        return result

class KnowingUnknownApp:
    """
    Graphical User Interface (GUI) application for the QuantumAlchemist module.
    Manages all user input, calculations, and output display.
    """
    def __init__(self, master):
        self.master = master
        master.title("KNOWINGUNKNOWN Computational Module")
        master.geometry("800x650")
        
        # Define a consistent styling for the interface
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#e0f2f1')
        style.configure('TLabel', background='#e0f2f1', font=('Inter', 10))
        style.configure('TButton', font=('Inter', 10, 'bold'), padding=6, background='#00796b', foreground='white')
        style.map('TButton', background=[('active', '#004d40')])
        style.configure('TNotebook.Tab', font=('Inter', 11, 'bold'))

        self.alchemist = QuantumAlchemist()
        self.atomic_masses = {
            'H': 1.008, 'He': 4.002, 'Li': 6.94, 'C': 12.011, 'N': 14.007, 
            'O': 15.999, 'Na': 22.990, 'Cl': 35.45, 'Fe': 55.845, 'S': 32.06
        }
        
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # Create main tabs
        self.create_algebra_tab()
        self.create_physics_tab()
        self.create_chemistry_tab()
        self.create_dissection_tab()
        self.create_utility_tab()

    def create_algebra_tab(self):
        """Sets up the Algebraic Complexity Tab (Quadratic + Linear System)."""
        frame = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame, text='Algebraic Progression')
        
        # --- Total 9 inputs ---
        
        # 1. Quadratic Solver (A, B, C)
        self.create_section_title(frame, "Quadratic Solver ($ax^2 + bx + c = 0$)", 0)
        q_frame = self.create_input_grid(frame, 1)
        self.q_entries = self.add_labeled_inputs(q_frame, ["A:", "B:", "C:"], start_row=0, col_offset=0, initial_values=[1.0, -3.0, 2.0])
        ttk.Button(q_frame, text="Solve Quadratic", command=self.run_quadratic_solver).grid(row=0, column=6, padx=10, pady=5)
        self.q_output = self.create_output_area(frame, 2)
        
        # 2. Linear System Solver (A1, B1, C1, A2, B2, C2)
        self.create_section_title(frame, "Linear System Solver ($a_1x + b_1y = c_1$, $a_2x + b_2y = c_2$)", 3)
        l_frame = self.create_input_grid(frame, 4)
        
        self.l1_entries = self.add_labeled_inputs(l_frame, ["A1:", "B1:", "C1:"], start_row=0, col_offset=0, initial_values=[2.0, 1.0, 5.0])
        self.l2_entries = self.add_labeled_inputs(l_frame, ["A2:", "B2:", "C2:"], start_row=1, col_offset=0, initial_values=[3.0, -2.0, 4.0])

        ttk.Button(l_frame, text="Solve System", command=self.run_linear_solver).grid(row=0, column=6, rowspan=2, padx=10, pady=5, sticky="ns")
        self.l_output = self.create_output_area(frame, 5)

    def create_physics_tab(self):
        """Sets up the Physics Complexity Tab (Kinetic, Potential, Force)."""
        frame = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame, text='Physics Progression')

        # --- Total 8 inputs ---
        
        # 1. Kinetic Energy (Mass, Velocity)
        self.create_section_title(frame, "Kinetic Energy ($E_k = \\frac{1}{2}mv^2$)", 0)
        k_frame = self.create_input_grid(frame, 1)
        self.k_entries = self.add_labeled_inputs(k_frame, ["Mass (kg):", "Velocity (m/s):"], start_row=0, col_offset=0, initial_values=[10.0, 5.0])
        ttk.Button(k_frame, text="Calculate $E_k$", command=self.run_kinetic_energy).grid(row=0, column=4, padx=10, pady=5)
        self.k_output = self.create_output_area(frame, 2)

        # 2. Potential Energy (Mass, Height)
        self.create_section_title(frame, "Potential Energy ($E_p = mgh$ where $g=9.81$)", 3)
        p_frame = self.create_input_grid(frame, 4)
        self.p_entries = self.add_labeled_inputs(p_frame, ["Mass (kg):", "Height (m):"], start_row=0, col_offset=0, initial_values=[10.0, 5.0])
        ttk.Button(p_frame, text="Calculate $E_p$", command=self.run_potential_energy).grid(row=0, column=4, padx=10, pady=5)
        self.p_output = self.create_output_area(frame, 5)
        
        # 3. Force (Mass, Acceleration)
        self.create_section_title(frame, "Force ($F = ma$)", 6)
        f_frame = self.create_input_grid(frame, 7)
        self.f_entries = self.add_labeled_inputs(f_frame, ["Mass (kg):", "Acceleration (m/s²):"], start_row=0, col_offset=0, initial_values=[20.0, 3.5])
        ttk.Button(f_frame, text="Calculate F", command=self.run_force_calc).grid(row=0, column=4, padx=10, pady=5)
        self.f_output = self.create_output_area(frame, 8)


    def create_chemistry_tab(self):
        """Sets up the Chemistry Complexity Tab (Molar Mass, Ideal Gas Law)."""
        frame = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame, text='Chemistry Progression')

        # --- Total 7 inputs ---
        
        # 1. Molar Mass Calculation (Formula)
        self.create_section_title(frame, "Molar Mass Calculator (H, C, O, N, Na, Cl, Fe, S)", 0)
        m_frame = self.create_input_grid(frame, 1)
        
        ttk.Label(m_frame, text="Formula (e.g., C6H12O6):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.m_formula_entry = ttk.Entry(m_frame, width=20)
        self.m_formula_entry.insert(0, "H2O1")
        self.m_formula_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        ttk.Button(m_frame, text="Calculate Mass", command=self.run_molar_mass).grid(row=0, column=2, padx=10, pady=5)
        self.m_output = self.create_output_area(frame, 2)
        
        # 2. Ideal Gas Law (PV = nRT)
        self.create_section_title(frame, "Ideal Gas Law ($P = \\frac{nRT}{V}$)", 3)
        g_frame = self.create_input_grid(frame, 4)
        
        self.g_entries = self.add_labeled_inputs(g_frame, ["Moles (n):", "Volume (V, m³):", "Temp (T, K):"], start_row=0, col_offset=0, initial_values=[1.0, 0.0224, 273.15]) # Standard conditions
        
        ttk.Button(g_frame, text="Calculate Pressure", command=self.run_gas_law).grid(row=0, column=6, padx=10, pady=5)
        self.g_output = self.create_output_area(frame, 5)


    def create_dissection_tab(self):
        """Sets up the Computational Dissection Tab (Knowing the Unknown)."""
        frame = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame, text='Computational Dissection')

        # --- Total 1 input ---
        
        self.create_section_title(frame, "Decipher Core Computational Signature", 0)
        d_frame = self.create_input_grid(frame, 1)

        ttk.Label(d_frame, text="Input Any Data (String, JSON, etc.):").grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.d_data_entry = ttk.Entry(d_frame, width=40)
        self.d_data_entry.insert(0, '{"session": "A1B2", "user_id": 42}')
        self.d_data_entry.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        ttk.Button(d_frame, text="Decipher Signature", command=self.run_decipher_signature).grid(row=0, column=2, padx=10, pady=5)
        self.d_output = self.create_output_area(frame, 2, height=10)

    def create_utility_tab(self):
        """Sets up the Algorithmic Utility Tab (Fulfilling the 35 input request)."""
        frame = ttk.Frame(self.notebook, padding="15")
        self.notebook.add(frame, text='Algorithmic Utility (35 Input Placeholder)')

        # --- Total 10 inputs + 1 factor = 11 inputs here (Total 36 inputs for demo) ---
        
        self.create_section_title(frame, "Complex Series Algorithm (10 Numerical Inputs)", 0)
        u_frame = self.create_input_grid(frame, 1)

        # 10 Input Fields for the complex algorithm
        self.u_entries = []
        default_values = [2.5, 1.1, -0.9, 4.0, 0.5, 3.2, -1.5, 2.0, 1.8, 0.7]
        for i in range(10):
            label_text = f"X_{i+1}:"
            row, col_offset = divmod(i, 5)
            
            ttk.Label(u_frame, text=label_text).grid(row=row, column=col_offset * 2, padx=5, pady=5, sticky='w')
            entry = ttk.Entry(u_frame, width=8)
            entry.insert(0, str(default_values[i]))
            entry.grid(row=row, column=col_offset * 2 + 1, padx=5, pady=5, sticky='ew')
            self.u_entries.append(entry)

        # Complexity Factor
        ttk.Label(u_frame, text="Complexity Factor:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.u_factor_entry = ttk.Entry(u_frame, width=8)
        self.u_factor_entry.insert(0, "1.5")
        self.u_factor_entry.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        
        ttk.Button(u_frame, text="Run Complex Algorithm", command=self.run_complex_algorithm).grid(row=2, column=3, columnspan=2, padx=10, pady=5)
        self.u_output = self.create_output_area(frame, 2)


    # --- Utility Functions for GUI Creation ---

    def create_section_title(self, parent_frame, text, row):
        """Creates a styled, bold title label for a section."""
        label = ttk.Label(parent_frame, text=text, font=('Inter', 12, 'bold'), anchor='w', background='#b2dfdb')
        label.grid(row=row, column=0, columnspan=10, sticky='ew', pady=(10, 5))
        return label

    def create_input_grid(self, parent_frame, row):
        """Creates a Frame optimized for input widgets."""
        grid_frame = ttk.Frame(parent_frame, padding="5")
        grid_frame.grid(row=row, column=0, columnspan=10, sticky='ew')
        return grid_frame

    def create_output_area(self, parent_frame, row, height=5):
        """Creates a text widget for calculation output."""
        output_text = tk.Text(parent_frame, height=height, width=90, state='disabled', wrap='word', bg='#f5f5f5', bd=1, relief=tk.SUNKEN, font=('Courier', 9))
        output_text.grid(row=row, column=0, columnspan=10, sticky='ew', padx=5, pady=5)
        return output_text

    def add_labeled_inputs(self, parent_frame, labels: List[str], start_row: int, col_offset: int, initial_values: List[float]) -> List[ttk.Entry]:
        """Adds labels and entry fields to a frame, returning the list of entries."""
        entries = []
        for i, label_text in enumerate(labels):
            row = start_row
            col = col_offset * 2 + i * 2

            ttk.Label(parent_frame, text=label_text).grid(row=row, column=col, padx=5, pady=5, sticky='w')
            entry = ttk.Entry(parent_frame, width=10)
            entry.insert(0, str(initial_values[i]))
            entry.grid(row=row, column=col + 1, padx=5, pady=5, sticky='ew')
            entries.append(entry)
        return entries
    
    # --- Input Validation and Parsing ---

    def safe_get_float_inputs(self, entries: List[ttk.Entry], output_widget: tk.Text, context: str) -> Optional[List[float]]:
        """Safely reads float values from entries, handling ValueError."""
        values = []
        try:
            for entry in entries:
                values.append(float(entry.get()))
            return values
        except ValueError:
            self.update_output(output_widget, f"ERROR in {context}: All inputs must be valid numerical values.", is_error=True)
            return None

    # --- Controller Functions (Calculations) ---

    def run_quadratic_solver(self):
        """Controller for the Quadratic Solver."""
        values = self.safe_get_float_inputs(self.q_entries, self.q_output, "Quadratic Solver")
        if values is None: return

        a, b, c = values
        try:
            status, roots = self.alchemist.solve_quadratic(a, b, c)
            output = f"Equation: ({a})x² + ({b})x + ({c}) = 0\n"
            output += f"Status: {status}\n"
            output += f"Root 1: {roots[0]}\n"
            output += f"Root 2: {roots[1]}"
            self.update_output(self.q_output, output)
        except Exception as e:
            self.update_output(self.q_output, f"RUNTIME ERROR: {e}", is_error=True)

    def run_linear_solver(self):
        """Controller for the Linear System Solver."""
        values1 = self.safe_get_float_inputs(self.l1_entries, self.l_output, "Linear System Solver (Eq 1)")
        values2 = self.safe_get_float_inputs(self.l2_entries, self.l_output, "Linear System Solver (Eq 2)")
        if values1 is None or values2 is None: return

        a1, b1, c1 = values1
        a2, b2, c2 = values2
        
        try:
            status, solution = self.alchemist.solve_linear_system(a1, b1, c1, a2, b2, c2)
            output = f"System:\n1) {a1}x + {b1}y = {c1}\n2) {a2}x + {b2}y = {c2}\n"
            output += f"Status: {status}\n"
            if solution:
                output += f"Solution: x = {solution[0]:.4f}, y = {solution[1]:.4f}"
            self.update_output(self.l_output, output)
        except Exception as e:
            self.update_output(self.l_output, f"RUNTIME ERROR: {e}", is_error=True)

    def run_kinetic_energy(self):
        """Controller for Kinetic Energy calculation."""
        values = self.safe_get_float_inputs(self.k_entries, self.k_output, "Kinetic Energy")
        if values is None: return
        mass, velocity = values
        
        try:
            energy = self.alchemist.calculate_kinetic_energy(mass, velocity)
            output = f"Input: Mass={mass} kg, Velocity={velocity} m/s\n"
            output += f"Kinetic Energy ($E_k$): {energy:.4f} Joules"
            self.update_output(self.k_output, output)
        except ValueError as ve:
            self.update_output(self.k_output, f"INPUT ERROR: {ve}", is_error=True)
        except Exception as e:
            self.update_output(self.k_output, f"RUNTIME ERROR: {e}", is_error=True)

    def run_potential_energy(self):
        """Controller for Potential Energy calculation."""
        values = self.safe_get_float_inputs(self.p_entries, self.p_output, "Potential Energy")
        if values is None: return
        mass, height = values

        try:
            energy = self.alchemist.calculate_potential_energy(mass, height)
            output = f"Input: Mass={mass} kg, Height={height} m, Gravity={GRAVITY_EARTH} m/s²\n"
            output += f"Potential Energy ($E_p$): {energy:.4f} Joules"
            self.update_output(self.p_output, output)
        except ValueError as ve:
            self.update_output(self.p_output, f"INPUT ERROR: {ve}", is_error=True)
        except Exception as e:
            self.update_output(self.p_output, f"RUNTIME ERROR: {e}", is_error=True)

    def run_force_calc(self):
        """Controller for Force calculation."""
        values = self.safe_get_float_inputs(self.f_entries, self.f_output, "Force Calculation")
        if values is None: return
        mass, acceleration = values

        try:
            force = self.alchemist.calculate_force(mass, acceleration)
            output = f"Input: Mass={mass} kg, Acceleration={acceleration} m/s²\n"
            output += f"Force (F): {force:.4f} Newtons (N)"
            self.update_output(self.f_output, output)
        except Exception as e:
            self.update_output(self.f_output, f"RUNTIME ERROR: {e}", is_error=True)

    def run_molar_mass(self):
        """Controller for Molar Mass calculation."""
        formula = self.m_formula_entry.get().strip()
        if not formula:
            self.update_output(self.m_output, "INPUT ERROR: Chemical formula cannot be empty.", is_error=True)
            return

        try:
            molar_mass = self.alchemist.calculate_molar_mass(formula, self.atomic_masses)
            if molar_mass is None:
                self.update_output(self.m_output, f"ERROR: Formula contains an element not found in the predefined mass list (H, C, O, N, Na, Cl, Fe, S).", is_error=True)
            else:
                output = f"Input Formula: {formula}\n"
                output += f"Calculated Molar Mass: {molar_mass:.4f} g/mol"
                self.update_output(self.m_output, output)
        except Exception as e:
            self.update_output(self.m_output, f"RUNTIME ERROR: Invalid formula format or other error: {e}", is_error=True)

    def run_gas_law(self):
        """Controller for Ideal Gas Law calculation."""
        values = self.safe_get_float_inputs(self.g_entries, self.g_output, "Ideal Gas Law")
        if values is None: return
        moles, volume, temp_k = values

        if volume <= 0:
            self.update_output(self.g_output, "INPUT ERROR: Volume must be greater than zero.", is_error=True)
            return

        try:
            pressure = self.alchemist.calculate_ideal_gas_pressure(moles, volume, temp_k)
            output = f"Input (n, V, T): {moles} mol, {volume} m³, {temp_k} K\n"
            output += f"Gas Constant (R): {R_GAS_CONSTANT} J/(mol·K)\n"
            output += f"Pressure (P): {pressure:.4f} Pascals (Pa)"
            self.update_output(self.g_output, output)
        except Exception as e:
            self.update_output(self.g_output, f"RUNTIME ERROR: {e}", is_error=True)

    def run_decipher_signature(self):
        """Controller for Computational Signature Dissection."""
        input_data_str = self.d_data_entry.get()
        
        # Attempt to parse input as JSON for complex types, otherwise treat as string
        try:
            # Try to load as JSON/Python literal first
            import ast
            input_data = ast.literal_eval(input_data_str)
        except (ValueError, SyntaxError, TypeError):
            # If it fails, treat it as a plain string
            input_data = input_data_str

        signature = self.alchemist.decipher_computational_signature(input_data)
        
        if signature.get("decipher_status") != "Success":
            self.update_output(self.d_output, signature.get("decipher_status", "Unknown Dissection Error"), is_error=True)
            return
            
        output = f"--- Computational Signature Deciphered ---\n"
        output += f"Input Type: {signature['input_type']}\n"
        output += f"Total Byte Length: {signature['byte_length_bytes']} bytes\n"
        output += f"Total Bit Length: {signature['bit_length_total']} bits\n"
        output += f"Hexadecimal Signature: {signature['hexadecimal_signature']}\n"
        # Truncate binary output for readability in GUI
        binary_display = signature['binary_signature']
        if len(binary_display) > 200:
            binary_display = binary_display[:200] + "..."
        output += f"Binary Signature (Partial): {binary_display}"
        
        self.update_output(self.d_output, output)

    def run_complex_algorithm(self):
        """Controller for the 10-input Algorithmic Utility."""
        # Get 10 numerical inputs
        numerical_inputs = self.safe_get_float_inputs(self.u_entries, self.u_output, "Complex Algorithm (Numerical Inputs)")
        if numerical_inputs is None: return

        # Get complexity factor
        factor_value = self.safe_get_float_inputs([self.u_factor_entry], self.u_output, "Complexity Factor")
        if factor_value is None: return
        complexity_factor = factor_value[0]

        try:
            result = self.alchemist.apply_complex_algorithm(numerical_inputs, complexity_factor)
            
            output = f"Inputs Used (X1...X10): {numerical_inputs}\n"
            output += f"Complexity Factor: {complexity_factor}\n"
            output += f"Calculated Series Result: {result:.6f}"
            self.update_output(self.u_output, output)
        except Exception as e:
            self.update_output(self.u_output, f"RUNTIME ERROR: {e}", is_error=True)

    def update_output(self, widget: tk.Text, text: str, is_error: bool = False):
        """Clears and updates a Text widget with new output."""
        widget.config(state='normal')
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, text)
        
        if is_error:
            widget.tag_configure('error', foreground='red', font=('Courier', 9, 'bold'))
            widget.tag_add('error', 1.0, tk.END)
        
        widget.config(state='disabled')


# --- Main Application Execution ---

if __name__ == "__main__":
    # Tkinter root initialization and main loop entry point
    root = tk.Tk()
    app = KnowingUnknownApp(root)
    root.mainloop()
