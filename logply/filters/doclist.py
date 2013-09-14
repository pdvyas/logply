def do(obj, kwargs):

	if kwargs['is_single']:
		obj.update(kwargs['extra_kwargs'])
		return [obj]

	ret = []
	parent = {}
	parent.update({key:obj[key] for key in kwargs['parent']['keys']})
	parent.update(kwargs['parent']['extra_kwargs'])

	ret.append(parent)

	children = obj[kwargs['child']['key']]
	for child in children:
		child.update(kwargs['child']['extra_kwargs'])
		ret.append(child)

	return ret

