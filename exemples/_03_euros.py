#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Convert euros and francs."""

EURO = 6.55957

def francs2euros(f):
	"""Converts francs to euros."""
	return f/EURO

def euros2francs(e):
	"""Converts euros to francs."""
	return e*EURO