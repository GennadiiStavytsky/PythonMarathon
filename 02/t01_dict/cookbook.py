def search_cookbook(cookbook, recipe, section):
	if cookbook.get(recipe) != None:
		for book in cookbook:
				if book == recipe:
					res = cookbook[book].get(section)
		if res != None:
			return res
		else:
			return f'There is no "{section}" in the "{recipe}" recipe.'
	else:
		return f'There is no "{recipe}" recipe in the cookbook.'