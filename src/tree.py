import sys
import os
if __name__ == '__main__':
	try:
		class node(object):
			def __init__(self):
				self.data = None
				self.pointers = []

		class tree(object):
			Z = 0
			clild=[]
			def __init__(self):
				self.root = None
			
			def insert_root(self,data):
				
				if (self.root == None):
					nnode = node()
					nnode.data = data
					self.root = nnode
				#elif not self.root.pointers:
				else:
					nnode = node()
					nnode.data = data
					#input_search = input('Enter search element')
					self.root.pointers.append(nnode)
				#else:
				#	print('E')
				 

			def insert(self,data,list_node,search_element):
				# if self.root == None:
				# 	nnode =node()
				# 	nnode.data = data
				# 	self.root = nnode
				# 	return True
				# elif not self.root.pointers:
				# 	nnode = node()
				# 	nnode.data = data
				# 	self.root.pointers.append(nnode)
				# 	return True
				self.list_node_list = []
				if not list_node:
					print('Not found that element')
					return False
				else:
					
					for leafNode in list_node:
						#condition
						if leafNode.data == search_element:
							print('Found')
							nnode = node()
							nnode.data = data
							leafNode.pointers.append(nnode)
							return True
						else:
							for subs in leafNode.pointers:
								self.list_node_list.append(subs)
							return self.insert(data,self.list_node_list,search_element)

			def root_leaf_list(self):
				self.leaf_list = []
				leaf_len=len(self.root.pointers)
				for i in range(0,leaf_len):
					self.leaf_list.append(self.root.pointers[i])
				return self.leaf_list

			def leafs(self,return_list):
				if not return_list:
					print('Empty list')
					return False #cause there is no leaf node left 
				else:
					self.gather_ton_of_leaf_node = []
					for leafNode in return_list:
						#print(leafNode.data)
						for sub in leafNode.pointers:
							self.gather_ton_of_leaf_node.append(sub)
					print('====')
					for i in self.gather_ton_of_leaf_node:
						print(i.data)
					print('====')
					
					return self.leafs(self.gather_ton_of_leaf_node)

			#def traversalPos(self):
				#will start from here 

							
		obj = tree()

		obj.insert_root(4)
		obj.insert_root(10)
		obj.insert_root(20)
		X = obj.root_leaf_list()
		obj.insert(30,X,10)
		obj.insert(40,X,20)
		obj.insert(50,X,10)
		obj.insert(60,X,10)
		#obj.printt(hhead) 
		
		# if not X[2].pointers:
		# 	print('None')
		# else:
		# 	print('have elements')
		# for i in X:
		# 	print(i.data)
		obj.leafs(X)
		

	except KeyboardInterrupt:
		try:
			print('\n')
			sys.exit(0)
		except SystemExit:
			print('\n')
			os._exit(0)


#output

# Not found that element
# 10
# 20
# 40
# 50
# 60
# Empty list
# ➜  src git:(master) ✗ python3 tree.py
# Not found that element
# Found
# Found
# Found
# 10
# 20
# 40
# 50
# 60
# Empty list
# ➜  src git:(master) ✗ python3 tree.py
# Not found that element
# Not found that element
# Found
# Found
# 10
# 20
# 50
# 60
# Empty list
# ➜  src git:(master) ✗ python3 tree.py
# Not found that element
# Not found that element
# Not found that element
# Found
# 10
# 20
# 60
# Empty list



