from lib.animal import *
from lib.zoo import *
import ipdb
# code here

# e.g.  
micke_grove = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
Animal( 'Tiger', 75, 'Luke', micke_grove )
Animal( 'Tiger', 75, 'Boulder', micke_grove )
Animal( 'Snake', 25, 'Jake', micke_grove)

san_diego = Zoo( 'San Diego Zoo', 'San Diego, CA' )
Animal( 'Lion', 75, 'Leia', san_diego )
Animal( 'Dog', 75, 'Joy', san_diego )


# do not remove 
ipdb.set_trace()
