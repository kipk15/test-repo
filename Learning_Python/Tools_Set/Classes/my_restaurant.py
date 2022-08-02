#from restaurants import Restaurant, IceCreamStand 
"""as above you can import specific Classes from a module
or, as below, the entire module. If importing entire module,
use dot notation if you decide, i.e module_name.ClassName"""
import restaurants 

#my_stand = IceCreamStand('my-stand', 'cream-ice')
my_stand = restaurants.IceCreamStand('my-stand', 'cream-ice')
my_stand.describe_flavors()