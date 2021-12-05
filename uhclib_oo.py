import json as j

class EncodeError(BaseException):
	pass;

class Item:
	def __init__(self, item, amount, display=None, nbt=None, *ench):
		if type(item) != type(str()):
			raise EncodeError("Item type must be a string.");
		if type(amount) != type(int()):
			raise EncodeError("Amount type must be an integer.");
			
		self.amount = amount;
		if desplay:
			self.customize = False;
		else:
			self.customize = True;
			self.display = display;
		self.item = item.upper()
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

	def decode(self, strcode, amount):
		self.amount = amount;
		if strcode.find("(")==-1:
			self.item = strcode.upper();
		else:
			enchants = strcode[strcode.find("(")+1:strcode.find(")")];
			enchants = enchants.split(sep=',');
			enchant = dict();
			for i in enchants:
				enclist = enclist.split("+");
				enchant["type"] = enclist[0].strip();
				enchant["level"] = int(enclist[1].strip());
				self.enchants.append(enchant);

	def encode(self):
		enc = dict();
		enc["type"] = self.item; 
		enc["amount"] = self.amount;
		enc["enchantments"] = self.enchants;
		return enc;

if __name__ == "__main__":
	main();
