#!/usr/bin/env python3

class Element:

	tag = ""
	indent = "   "

	def __init__(self, *content, **kwcontent):
		self.content = []
		self.attr= []
		if content:
			for item in content:
				self.content.append(item)
			for key in kwcontent:
				value = key + '="' + kwcontent[key] + '"'
				self.attr.append (value)


	def append(self, *content, **kwcontent):
		#self.content.append(content)
		for item in content:
			self.content.append(item)
		for key in kwcontent:
			value = key + '="' + kwcontent[key] + '"'
			self.attr.append(value)
		

	def render(self, out_file, ind=""):
		#tag_indent=self.initial_indent # or initial_indent=indent
		tag_out = ind + "<" + self.tag
		for att in self.attr:
			tag_out += " "
			tag_out += att
		tag_out += ">\n"
		out_file.write (tag_out)
		for stuff in self.content:
			if isinstance(stuff, Element):
				# look into using if hasattr (i, 'render')
				indent2 = self.indent + ind
				stuff.render(out_file, indent2)
			else:
				indent2 = self.indent + ind 
				out_file.write(self.indent + ind + stuff + "\n")
		tag_out = ind + "</" + self.tag + ">\n"
		out_file.write (tag_out)	

class Html(Element):
	tag = "html"
	indent = ""

class Head(Element):
	tag = "head"

class Title(Element):
	tag = "title"

class Body(Element):
	tag = "body"

class P(Element):
	tag = "p"

class Hr(Element):
	tag = "hr"