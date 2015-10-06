
def p_decorat(func):
	def func_wrapper(*args, **kwargs):
		return "<p>{0}</p>".format(func(*args, **kwargs))
	return func_wrapper

def div_decorat(func):
	def func_wrapper(name):
		return "<div>{0}</div>".format(func(name))
	return func_wrapper

def strong_decorat(func):
	def func_wrapper(name):
		return "<strong>{0}</strong>".format(func(name))
	return func_wrapper

def reverse_decorat(func):
	def func_wrapper(txt):
		txt = func(txt)
		print txt
		return txt[::-1]
	return func_wrapper

def reverseName(func):
	def func_wrapper(txt):
		txt = func(txt)
		return txt[::-1]

	return func_wrapper


@div_decorat
@p_decorat
@strong_decorat
def getText(name):
	return "llorem ipsum, {0} dolor sit amet".format(name)

print getText('Nain')

def getLlorem(text='dolor sit amet'):
	return "llorem ipsum "+text

reverseFunc = reverseName(getLlorem)

print reverseFunc('nain')


class Person(object):
	def __init__(self, name="Luke", lastname="Skywalker"):
		self.name = name
		self.lastname = lastname

	@reverse_decorat
	def getFullName(self):
		return self.name+" "+self.lastname


luke = Person()

print luke.getFullName()
