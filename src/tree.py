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
			
			def insert(self,data,point_node,search_element):
				nnode = node()
				nnode.data = data
				if (self.root == None):
					self.root = nnode
				elif not self.root.pointers:
					#input_search = input('Enter search element')
						self.root.pointers.append(nnode)
				else:
					print('E')
					#will start from here 

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
						print(leafNode.data)
						for sub in leafNode.pointers:
							self.gather_ton_of_leaf_node.append(sub)
					return self.leafs(self.gather_ton_of_leaf_node)

			#def traversalPos(self):
				#will start from here 

							
		obj = tree()

		obj.insert(4,obj.root,4)
		obj.insert(10,obj.root,4)
		obj.insert(20,obj.root,4)
		obj.insert(30,obj.root,4)
		obj.insert(40,obj.root,4)
		obj.insert(50,obj.root,4)
		obj.insert(60,obj.root,4)
		#obj.printt(hhead) 
		X = obj.root_leaf_list()
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



