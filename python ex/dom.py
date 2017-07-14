#futur_domain = [('state','in',['open','toclose']),('start_date','>',today)]
#expired_domain = [('state','in',['open','futur']),('expiration_date','<',today)


#def dom2tree():
today = '2001-01-01'
dom = ['&','!','|','&',('a'),('x'),'&',('b'),('y'),
	'|','&',('a'),('x'),'&',('b'),('y')]
#dom= ['&','!','|','&',('state','in',['open','toclose']),('start_date','>',today),'&',('state','in',['open','futur']),('expiration_date','<',today),
#	'|','&',('state','in',['open','toclose']),('start_date','>',today),'&',('state','in',['open','futur']),('expiration_date','<',today)]
tree = list(reversed(dom))
c = []
n = list(reversed(dom))
while len(tree)>0:
  for elem in tree:
    print 'c is ',c
    print 'elem is ',elem
    if elem == '!': 
      t=[tree.pop(0),c.pop(0)]
      print 't is in !',t
      c = [t]+c
      break
    elif elem =='|' or elem=='&':
      a=c.pop(-1)
      b=c.pop(-1)
      t = [(b),tree.pop(0),(a)]
      print 't is ',t
      c.append(t)
      break
    else:
      c.append((tree.pop(0)))
      break
print 'Tree = \n',c
#tree = 
#[ 
#   	['!' 
#		[ 
#			[('state','in',['open','toclose']),'&',('start_date','>',today)],
#			'|',
#			[('state','in',['open','futur']),'&',('expiration_date','>',today)],
#		]
#  	]
#  	'&'
#  	[ 
#		[('state','in',['open','toclose']),'&',('start_date','>',today)],
#		'|',
#		[('state','in',['open','futur']),'&',('expiration_date','>',today)],
#	]
#]
#['!','|','&',('state','in',['open','toclose']),('start_date','>',today),'&',('state','in',['open','futur']),('expiration_date','<',today)]
['!', 
	[
		[
			[
				('state', 'in', ['open', 'toclose']), 
				'&',
				 ('start_date', '>', '2001-01-01')
			], 
			'|', 
			[
				('state', 'in', ['open', 'futur']),
				 '&', 
				('expiration_date', '<', '2001-01-01')
			]
		], 
		'&', 
		[
			[
				('state', 'in', ['open', 'toclose']), 
				'&',
				('start_date', '>', '2001-01-01')
			], 
			'|', 
			[
				('state', 'in', ['open', 'futur']), 
				'&', 
				('expiration_date', '<', '2001-01-01')
			]
		]
	]
]

[
	[
		[
			['a', '&', 'x'], 
			'|',
			['b', '&', 'y']
		], 
		'&', 
		[
			'!',
	 		[
				['a', '&', 'x'], 
				'|', 
				['b', '&', 'y']
			]
		]
	]
]

[[[['a', '&', 'x'], '|', ['b', '&', 'y']], '&', ['!', [['a', '&', 'x'], '|', ['b', '&', 'y']]]]]

[
	[
		['!', 
			[
				['y', '&', 'b'], 
				'|', 
				['x', '&', 'a']
			]
		], 
		'&', 
		[
			['y', '&', 'b'],
			 '|'
			, 
			['x', '&', 'a']
		]
	]
]


























