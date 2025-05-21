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


def construir_clave(alice_bases, bob_bases, bob_results):
    """Filtra los bits donde las bases coinciden para formar la clave."""
    clave = []
    indices_coincidentes = []
    for i in range(len(alice_bases)):
        if alice_bases[i] == bob_bases[i]:
            clave.append(bob_results[i])
            indices_coincidentes.append(i)
    return clave, indices_coincidentes


# ---------- Simulación ----------
n = 20  # Número de bits que Alice envía

alice_bits = generador_bits_random(n)
alice_bases = generador_bases_random(n)
bob_bases = generador_bases_random(n)

qubits_sent = encode_qubits(alice_bits, alice_bases)
bob_results = resultado_bob(qubits_sent, bob_bases)
clave_secreta, indices_utiles = construir_clave(alice_bases, bob_bases, bob_results)

# ---------- Mostrar resultados ----------
print("=== Simulación BB84 ===")
print(f"Bits de Alice:       {alice_bits}")
print(f"Bases de Alice:      {alice_bases}")
print(f"Bases de Bob:        {bob_bases}")
print(f"Resultados de Bob:   {bob_results}")


print("\n--- Clave Secreta ---")
print(f"Índices coincidentes: {indices_utiles}")
print(f"Clave compartida:     {clave_secreta}")
print(f"Longitud de la clave: {len(clave_secreta)} bits")


# ------------- Ataque de Eve ------------
def eve_intercept(qubits_sent):
    """Eve mide los qubits con bases aleatorias, introduciendo errores."""
    eve_bases = generador_bases_random(len(qubits_sent))
    eve_results = []
    for (bit, alice_base), eve_base in zip(qubits_sent, eve_bases):
        if alice_base == eve_base:
            eve_results.append(bit)  # Eve acierta por casualidad
        else:
            eve_results.append(random.randint(0, 1))  # Eve mide mal
    return eve_bases, eve_results


# Simulación con Eve
eve_bases, eve_results = eve_intercept(qubits_sent)
bob_results_con_eve = resultado_bob(list(zip(eve_results, eve_bases)), bob_bases)  # Bob recibe los qubits alterados
clave_con_eve, _ = construir_clave(alice_bases, bob_bases, bob_results_con_eve)
# ---------- Mostrar resultados con Eve ----------
print("\n--- Con Eve (ataque) ---")
print(f"Clave con Eve:       {clave_con_eve}")
print(f"Errores introducidos: {sum(1 for a, b in zip(clave_secreta, clave_con_eve) if a != b)}")
# Fin de la simulación