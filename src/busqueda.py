def binary_search(arr, target):
    """Busca un elemento en una lista ordenada usando búsqueda binaria.

    Args:
        arr (list): Lista ordenada de elementos.
        target (any): Elemento objetivo a encontrar.

    Returns:
        int: Índice del elemento si se encuentra, -1 si no.

    Raises:
        TypeError: Si arr no es una lista o si los elementos no son comparables.
        ValueError: Si la lista no está ordenada.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3], 6)
        -1
    """
    if not isinstance(arr, list):
        raise TypeError("El argumento 'arr' debe ser una lista.")
    if not all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
        raise ValueError("La lista debe estar ordenada.")

    izquierda, derecha = 0, len(arr) - 1
    
    # Divide y conquista en cada iteración
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == target:
            return medio
        elif arr[medio] < target:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1


# Ejemplo de uso
if __name__ == "__main__":
    lista_ordenada = [1, 2, 3, 4, 5, 7, 9]
    objetivo = 5
    resultado = binary_search(lista_ordenada, objetivo)
    print(f"Elemento encontrado en índice: {resultado}")  # Salida: 4
