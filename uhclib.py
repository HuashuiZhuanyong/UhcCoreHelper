import json as j
import yaml as y

def itemenc(item, cnt=1):
	encs = "enchantments";
	jsond = dict()
	if item.find("(")==-1:
		jsond["type"] = item.upper();
		jsond["amount"] = cnt;
	else:
		jsond["type"] = item[:item.find("(")].upper();
		jsond["amount"] = cnt;
		jsond[encs] = list();
		ench = item[item.find("(")+1:item.find(")")];
		ench = ench.split(sep=",");
		for i in range(len(ench)):
			ench[i] = ench[i].strip();
			ench[i] = ench[i].split(sep="+");
			jsond[encs].append(dict());
			jsond[encs][-1]["type"] = ench[i][0];
			jsond[encs][-1]["level"] = int(ench[i][1]);
	return j.dumps(jsond);

def kitenc(item, name, items):
	kit = dict();
	kit["symbol"] = dict();
	kit["symbol"]["item"] = item;
	kit["symbol"]["name"] = name;
	kit["items"] = items;
	return kit;

def main(ifile, ofile):
	item = str();
	case = int(ifile.readline().strip("\n"));
	kits = dict();
	for cntk in range(case):
		pro = ifile.readline();
		while pro == '\n':
			pro = ifile.readline();
		pro = pro.strip("\n");
		if pro.find("(")==-1:
			pro = pro.split();
			citem = int(pro[0]);
			idn = pro[1];
			item = itemenc(pro[2]);
			name = pro[3];
		else:
			pros = pro.split();
			citem = int(pros[0]);
			idn = pros[1];
			name = pros[-1];
			item = str();
			for i in pros[2:-1]:
				item += i;
			item = itemenc(item);
		items = list();
		for cnti in range(citem):
			kitem = ifile.readline().strip("\n");
			ind = kitem.rfind(' ');
#			sitem = kitem.split();
			if (ind!=-1) and (kitem[ind+1:].isdigit()):
				items.append(itemenc(kitem[:ind], int(kitem[ind+1:])));
			else:
				items.append(itemenc(kitem));
		
		kit = kitenc(item, name, items);
		kits[idn] = kit;
	
	ofile.write(y.dump({"kits":kits}));

if __name__ == "__main__":
	ifile = open("kits.in", "r");
	ofile = open("kits.yml", "w");
#	ifile = open(input("input file:"), "r");
#	ofile = open(input("output file:"), "w");
	main(ifile, ofile);
	ifile.close();
	ofile.close();
	print("解析完成，已存储为 kits.yml\n是否写入 ./plugins/UhcCore/kits.yml [Y/n] : ", end='')
	if input()[0]=='Y':
		ifile = open("kits.in", "r");
		ofile = open("plugins/UhcCore/kits.yml", "w");
		main(ifile, ofile);
		ifile.close();
		ofile.close();

