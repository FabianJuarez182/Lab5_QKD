import random

def generador_bits_random(n):
    return [random.randint(0, 1) for _ in range(n)]

def generador_bases_random(n):
    return [random.choice(['↕', '↗']) for _ in range(n)]

def encode_qubits(bits, bases):
    """Simula el envío de bits en ciertas bases (no representamos qubits reales)."""
    return list(zip(bits, bases))

def resultado_bob(qubits_sent, bob_bases):
    """Simula cómo Bob mide los qubits de Alice con sus propias bases."""
    results = []
    for (bit, alice_base), bob_base in zip(qubits_sent, bob_bases):
        if alice_base == bob_base:
            results.append(bit)  # misma base, Bob recibe el bit correctamente
        else:
            results.append(random.randint(0, 1))  # base diferente, resultado aleatorio ya que no se usara en la clave secreta
    return results

# ---------- Simulación ----------
n = 20  # Número de bits que Alice envía

alice_bits = generador_bits_random(n)
alice_bases = generador_bases_random(n)
bob_bases = generador_bases_random(n)

qubits_sent = encode_qubits(alice_bits, alice_bases)
bob_results = resultado_bob(qubits_sent, bob_bases)

# Mostrar resultados
print("Bit original de Alice:  ", alice_bits)
print("Bases de Alice:         ", alice_bases)
print("Bases de Bob:           ", bob_bases)
print("Resultados de Bob:      ", bob_results)