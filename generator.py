from model import model, package
from util import *
import os

def hasList(obj):
	for var in obj:
		if isinstance(obj[var], dict):
			continue
		if isinstance(obj[var], list):
			return True
		if 'List' in datatypes[obj[var]]:
			return True
	return False

def hasArray(val):
	if '[]' in val:
		return True
	return False

def generateInterface(f, objName, obj):
	f.write('package ' + package + ';\n\n')

	if hasList(obj):
		f.write('import java.util.List;\n\n')

	f.write('public interface I' + objName + ' {\n\n')

	for var in obj:

		f.write('\tpublic boolean has'  + upperfirst(var) + '();\n')

		if isinstance(obj[var], dict):
			f.write('\tpublic I' + upperfirst(var) + ' get'  + upperfirst(var) + '();\n')
			continue

		if isinstance(obj[var], list):
			f.write('\tpublic List<I' + upperfirst(var) + '> get'  + upperfirst(var) + '();\n')
			continue

		datatype = obj[var]

		f.write('\tpublic ' + datatypes[datatype] + ' get' + upperfirst(var) + '();\n')

	f.write('}\n')


def generateAbstract(f, objName, obj):
	f.write('package ' + package + ';\n\n')

	#imports
	f.write('import org.apache.commons.lang3.builder.ReflectionToStringBuilder;\n')

	if hasList(obj):
		f.write('import java.util.ArrayList;\n')
		f.write('import java.util.List;\n\n')

	#class start
	f.write('public abstract class Abstract' + objName + ' implements I' + objName + ' {\n\n')

	#declare vars
	for var in obj:
		if isinstance(obj[var], dict):
			f.write('\tprotected I' + upperfirst(var) + ' '  + checkvar(var) + ';\n')
			continue

		if isinstance(obj[var], list):
			f.write('\tprotected List<I' + upperfirst(var) + '> '  + checkvar(var) + ';\n')
			continue

		datatype = datatypes[obj[var]]

		f.write('\tprotected ' + datatype + ' ' + checkvar(var) + ';\n')

		if isprimitive(datatype):
			f.write('\tprotected boolean has' + checkvar(var) + ';\n')

	f.write('\n')

	for var in obj:
		f.write('\t@Override\n')

		if isinstance(obj[var], dict):
			#getter
			f.write('\tpublic I' + upperfirst(var) + ' get' + upperfirst(var) + '() {\n')
			f.write('\t\treturn ' + checkvar(var) + ';\n')
			f.write('\t}\n\n')

			#has check
			f.write('\t@Override\n')
			f.write('\tpublic boolean has' + upperfirst(var) + '() {\n')
			f.write('\t\treturn ' + checkvar(var) + ' != null;\n')
			f.write('\t}\n\n')
			continue

		if isinstance(obj[var], list):
			#getter
			f.write('\tpublic List<I' + upperfirst(var) + '> get' + upperfirst(var) + '() {\n')
			f.write('\t\treturn ' + checkvar(var) + ';\n')
			f.write('\t}\n\n')

			#has check
			f.write('\t@Override\n')
			f.write('\tpublic boolean has' + upperfirst(var) + '() {\n')
			f.write('\t\treturn !' + checkvar(var) + '.isEmpty();\n')
			f.write('\t}\n\n')
			continue

		datatype = datatypes[obj[var]]

		#getter
		f.write('\tpublic ' + datatype + ' get' + upperfirst(var) + '() {\n')
		f.write('\t\treturn ' + checkvar(var) + ';\n')
		f.write('\t}\n\n')

		#has check
		if isprimitive(datatype):
			f.write('\t@Override\n')
			f.write('\tpublic boolean has' + upperfirst(var) + '() {\n')
			f.write('\t\treturn has' + checkvar(var) + ';\n')
			f.write('\t}\n\n')
		else:
			f.write('\t@Override\n')
			f.write('\tpublic boolean has' + upperfirst(var) + '() {\n')
			f.write('\t\treturn ' + checkvar(var) + ' != null;\n')
			f.write('\t}\n\n')

	#builder start
	f.write('\tpublic abstract static class Builder<T> implements IBuilder<T> {\n')

	#declare vars
	for var in obj:
		if isinstance(obj[var], dict):
			f.write('\t\tprotected I' + upperfirst(var) + ' ' + checkvar(var) + ';\n')
			continue

		if isinstance(obj[var], list):
			f.write('\t\tprotected List<I' + upperfirst(var) + '> ' + checkvar(var) + ';\n')
			continue

		datatype = datatypes[obj[var]]

		f.write('\t\tprotected ' + datatype + ' ' + checkvar(var) + ';\n')

		if isprimitive(datatype):
			f.write('\t\tprotected boolean has' + checkvar(var) + ' = false;\n')

	f.write('\n')

	for var in obj:
		if isinstance(obj[var], dict):
			f.write('\t\tpublic Builder set' + upperfirst(var) + '(I' + upperfirst(var) + ' ' + checkvar(var) + ') {\n')
			f.write('\t\t\tthis.' + checkvar(var) + ' = ' + checkvar(var) + ';\n')
			f.write('\t\t\treturn this;\n')
			f.write('\t\t}\n\n')
			continue

		if isinstance(obj[var], list):
			f.write('\t\tpublic Builder set' + upperfirst(var) + '(List<I' + upperfirst(var) + '> ' + checkvar(var) + ') {\n')
			f.write('\t\t\tthis.' + checkvar(var) + ' = ' + checkvar(var) + ';\n')
			f.write('\t\t\treturn this;\n')
			f.write('\t\t}\n\n')

			f.write('\t\tpublic Builder add' + upperfirst(var) + '(I' + upperfirst(var) + ' ' + checkvar(var) + ') {\n')
			f.write('\t\t\tif (this.' + checkvar(var) + ' == null) {\n')
			f.write('\t\t\t\tthis.' + checkvar(var) + ' = new ArrayList<>();\n')
			f.write('\t\t\t}\n\n')
			f.write('\t\t\tthis.' + checkvar(var) + '.add(' + checkvar(var) + ');\n')
			f.write('\t\t\treturn this;\n')
			f.write('\t\t}\n\n')

			if getbuilder(objName):
				f.write('\t\tpublic List<I' + upperfirst(var) + '> get' + upperfirst(var) + '() {\n')
				f.write('\t\t\treturn this.' + checkvar(var) + ';\n')
				f.write('\t\t}\n\n')
			continue

		datatype = obj[var]

		if hasArray(datatype):
			f.write('\t\tpublic Builder add' + upperfirst(var) + '(' + arrdatatype[datatype] + ' ' + checkvar(var) + ') {\n')
			f.write('\t\t\tif (this.' + checkvar(var) + ' == null) {\n')
			f.write('\t\t\t\tthis.' + checkvar(var) + ' = new ArrayList<>();\n')
			f.write('\t\t\t}\n\n')
			f.write('\t\t\tthis.' + checkvar(var) + '.add(' + checkvar(var) + ');\n')
			f.write('\t\t\treturn this;\n')
			f.write('\t\t}\n\n')

		f.write('\t\tpublic Builder set' + upperfirst(var) + '(' + datatypes[datatype] + ' ' + checkvar(var) + ') {\n')
		if isprimitive(datatypes[datatype]):
			f.write('\t\t\tthis.has' + checkvar(var) + ' = true;\n')
		f.write('\t\t\tthis.' + checkvar(var) + ' = ' + checkvar(var) + ';\n')
		f.write('\t\t\treturn this;\n')
		f.write('\t\t}\n\n')

		if getbuilder(objName):
			f.write('\t\tpublic ' + datatypes[datatype] + ' get' + upperfirst(var) + '() {\n')
			f.write('\t\t\treturn this.' + checkvar(var) + ';\n')
			f.write('\t\t}\n\n')

			if not isprimitive(datatypes[datatype]):
				f.write('\t\tpublic boolean has' + upperfirst(var) + '() {\n')
				f.write('\t\t\treturn this.' + checkvar(var) + ' != null;\n')
				f.write('\t\t}\n\n')


	f.write('\t\t@Override\n')
	f.write('\t\tpublic abstract T build();\n')
	f.write('\t}\n\n')

	f.write('\t@Override\n')
	f.write('\tpublic String toString() {\n')
	f.write('\t\treturn ReflectionToStringBuilder.toString(this);\n')
	f.write('\t}\n')
	f.write('}\n')


def generateImplementation(f, objName, obj):
	f.write('package ' + package + ';\n\n')

	f.write('public class ' + objName + ' extends Abstract' + objName + ' {\n\n')
	f.write('\tpublic static class Builder extends Abstract' + objName + '.Builder<' + objName + '> {\n\n')

	f.write('\t\t@Override\n')
	f.write('\t\tpublic ' + objName + ' build() {\n')
	f.write('\t\t\treturn new ' + objName + '(this);\n')
	f.write('\t\t}\n')
	f.write('\t}\n\n')

	f.write('\tprivate ' + objName + '(Builder builder) {\n')

	for var in obj:
		f.write('\t\t' + checkvar(var) + ' = builder.' + checkvar(var) + ';\n')

		if not isinstance(obj[var], list) and not isinstance(obj[var], dict) and isprimitive(datatypes[obj[var]]):
			f.write('\t\thas' + checkvar(var) + ' = builder.has' + checkvar(var) + ';\n')

	f.write('\t}\n}\n')


def walk(node, name=None):
	if name != None:
		createJava(name, node)

	for item in node:
		value = node[item]

		if isinstance(value, dict) and name == None:
			createJava(item, value)

		if isinstance(value, dict):
			walk(value, item)

		if isinstance(value, list):
			walk(value[0], item)


def createJava(name, node):
	objName = upperfirst(name)
	intf = open(filepath + 'I' + objName + '.java', 'w')
	abst = open(filepath + 'Abstract' + objName + '.java', 'w')
	impl = open(filepath + objName + '.java', 'w')

	generateInterface(intf, objName, node)
	generateAbstract(abst, objName, node)
	generateImplementation(impl, objName, node)

	intf.close()
	abst.close()
	impl.close()


if __name__ == '__main__':
	filepath = 'out/' + package.replace('.', '/') + '/'

	if not os.path.exists(filepath):
	    os.makedirs(filepath)

	createBuilderInterface(filepath, package)
	createExtInterface(filepath, package)

	walk(model)
