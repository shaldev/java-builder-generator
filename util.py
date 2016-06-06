STRING = 'String'
INTEGER = 'int'
FLOAT = 'double'

datatypes = {
	'str' : STRING,
	'int' : INTEGER,
	'float' : FLOAT,
	'str[]' : 'List<String>',
	'int[]' : 'List<Integer>',
	'ext' : 'IExt'
}

arrdatatype = {
	'str[]' : STRING,
	'int[]' : INTEGER
}

__primitives = [INTEGER, FLOAT]
__builder_get = ['seatbid', 'bid']

#java reserved words skip
__varchange = {
	'native' : 'nativ'
}

def isprimitive(v):
	return v in __primitives

def getbuilder(v):
	return v.lower() in __builder_get

def checkvar(var):
	if var in __varchange:
		return __varchange[var]
	return var

def createBuilderInterface(path, package):
	f = open(path + '/IBuilder.java', 'w')
	f.write('package ' + package + ';\n\n')
	f.write('public interface IBuilder<T> {\n')
	f.write('\tpublic T build();\n')
	f.write('}\n')
	f.close()

def createExtInterface(path, package):
	f = open(path + '/IExt.java', 'w')
	f.write('package ' + package + ';\n\n')
	f.write('public interface IExt<T> {\n')
	f.write('}\n')
	f.close()

def upperfirst(x):
    return x[0].upper() + x[1:]
