
def tags(tagName):
	def tags_decorator(func):
		def func_wrapper(*args, **kwargs):
			return "<{0}>{1}</{0}>".format(tagName, func(*args, **kwargs))
		return func_wrapper
	return tags_decorator


@tags('p')
def getText(name):
	return "llorem ipsum, {0} dolor sit amet".format(name)

print getText('Nain')

