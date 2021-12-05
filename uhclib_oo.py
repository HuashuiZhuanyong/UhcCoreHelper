import json as j

class Item:
	def __init__(self, amount, display=None, nbt=None, *ench):
		self.amount = amount;
		if desplay:
			self.customize = False;
		else:
			self.customize = True;
			self.display = display;
		self.source = dict();
		self.enchants = list();
		enchant = dict();
		for ele in ench:
			enchant["type"] = ele[0];
			enchant["level"] = int(ele[1]);
			self.enchants.append(enchant);
		self.source["enchantments"] = enchants;
	def __add__(self, other):
		return MultiItem(self, other);
	def enc(self):
		

if __name__ == "__main__":
	main();
