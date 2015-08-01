#!/usr/bin/env python

import ply.lex as lex

# Commonmark specification by John MacFarlane
# http://spec.commonmark.org/0.21/

# The spec uses BMP Unicode codepoints:
# U+NNNN where 0000 <= NNNN <= FFFF
# https://en.wikipedia.org/wiki/Plane_(Unicode)#Basic_Multilingual_Plane

# The building blocks are:
# character, line, line ending, blank line, whitespace character,
# whitespace, unicode whitespace, space, non-whitespace character,
# ascii punctuation character, punctuation character

# Tabs in lines are kept as is. But in contexts where indentation is
# significant each tab is replaced by 4 characters.
# TODO: Take a closer look at examples

# U+0000 is an insecure character. Replace it with U+FFFD.
# Why? can't seem to find a reason!
# TODO: find out why U+0000 is insecure

# blocks:
# a document is made up of multiple blocks
# each block has a type: paragraph, block quote, list, header, rule, code block,
# etc
# some types of blocks (block quote and list item)  can *contain* other blocks
# (header and paragraph)
# other blocks can contain *inline* content such as text, links, ems, imgs,
# code, etc

# blocks have greater precedence compared to inline structures.
# the above rule implicates a two-step parsing procedure
# **step1: ** block structure of doc is found out (linear)
# **step2: ** inline content is parsed (parallel)

# leaf blocks: blocks that can't contain other blocks (unlike container blocks)
# horiz rules, ATX headers (the-hash-# format), Setext headers

# indented code block is composed of one or more *indented chunks* separated by
# blank lines. An indented chunk is a sequence of non-blank lines each indented
# four or more spaces.

# *code fence* a sequence of three consecutive backticks/tildes (``` or ~~~)
# *fenced code block* begins with a code fence, indented at max three space
# UHH: why are they using this magic number 3??

# *info string* optional text following the code fence

# *html block* group of lines treated as HTML. There are 7 types of blocks.
# TODO: What is this "may/may not interrupt a paragraph concept? understand it.

# *link reference definition* consists of a link label, a colon, optional
# whitespace, link destination, optional whitespace, optional link title.

# *paragraphs* sequence of non-blank lines that cannot be interpreted as other
# kinds of blocks forms a paragraph.
# **interrupting paragraph** means this. to interrupt, there must be some
# element that causes the interruption. So, what the spec is saying is that
# introducing a new element or new sequence of character after the beginning of
# a paragraph may either end the paragraph or keep it running further. if the
# new element causes the running paragraph to be closed, then it is said to
# "interrupt the paragraph".
# if a newly introduced element doesn't close the running paragraph, then it is
# said to "not interrupt the paragraph"

# there are two kinds of container blocks: block quotes and list items (lists
# are meta-containers for list items)
# syntax for container blocks is defined recursively

# *block quote marker: * 0-3 spaces + '>' + space then blah blah

# *list marker* can be either a bullet list marker (-, +, *) or ordered list
# marker (0-9)

# *lists* a principle of uniformity is applied here.

# *inlines* parsed sequentially left to right

# escaping should be handled.

# code spans

# autolinks

# TODO: Read and understand parsing strategy. Begin from there.

