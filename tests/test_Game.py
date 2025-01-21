import math
import sys
import os
import pytest
import unittest
from unittest.mock import MagicMock, patch , Mock
import pygame
import customtkinter as ctk
import numpy as np
import time

# Ajouter le chemin racine du projet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importer la classe JeuDeCablage et jeu
from powerplant.classes.jeux_cable import JeuDeCablage
from powerplant.classes.jeux_sinus import SinusMatchingGame 

# test unitaires pour jeux_cable.py 


def test_calculate_cable_path():
    """Test de la génération de la trajectoire du câble."""
    game = Mock()  # Pas besoin de l'initialisation complète
    start = (100, 200)
    end = (300, 400)
    gravity = 50
    segments = 5

    path = JeuDeCablage.calculate_cable_path(game, start, end, gravity, segments)
    assert len(path) == segments + 1  # Vérifie le nombre de segments
    for i, (x, y) in enumerate(path):
        t = i / segments
        assert math.isclose(x, start[0] + (end[0] - start[0]) * t)  # x doit être interpolé
        assert y >= start[1]  # La courbe est descendante puis ascendante

def test_is_inside_circle():
    """Vérifie si un point est bien dans un cercle donné."""
    game = Mock()
    center = (200, 300)
    radius = 50
    assert JeuDeCablage.is_inside_circle(game, 200, 300, center, radius)  # Dans le cercle
    assert not JeuDeCablage.is_inside_circle(game, 300, 400, center, radius)  # Hors du cercle

# Tests unitaires pour jeux_sinus.py 

def test_generate_sinus():
    # Paramètres de test
    amplitude = 1.0
    frequency = 1.0
    x_values = np.linspace(0, 1, 500)
    
    # Calcul attendu
    expected_y_values = amplitude * np.sin(2 * np.pi * frequency * x_values)
    
    # Appel de la fonction via l'instance de jeu
    game = SinusMatchingGame(ctk.CTk())
    result = game.generate_sinus(amplitude, frequency, x_values)
    
    # Vérification que les résultats sont égaux
    np.testing.assert_array_almost_equal(result, expected_y_values)
