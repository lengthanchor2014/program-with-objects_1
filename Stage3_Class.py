#import the Real Expression to extract information 
#The object on the first line is the superclass, i.e. this says that MyClass is a subclass of object. This is normal for Python class definitions.
import re


# ------- CLASS   ----------------------------------------------------------


# We are explicitly inheriting the object class in Python to show good format. 
# This really isn't needed since it's built into our class being called. 
class Concept(object):
  """Class that represents our Concept object.
  Each Concept object will have a title and a description property
  """
  
  #Construtor "__init__"
  #object = self, title, description
  def __init__(self,title,description):
    """Constructor to initialize our object"""
    self.title = title
    self.description = description
    
	#concept = Concept('title','description) = calls constructor "__init__" & pass func
	#concept.title = 'title'
	#concept.description = description



  #Define function "generate_html" 
  def generate_html(self):
    """Generates html for our concept"""
    html_text_1 = """
    <div class="concept">

    		<div class="concept-title">

        				""" + self.title

    html_text_2 = """
    		</div>

    		<div class="concept-description">

		  <p>
			
       		 		""" + self.description + """ 
  
          </p>"""

    html_text_3 = '''

    		</div>

    </div>'''

    return  html_text_1 + html_text_2 + html_text_3

#------------------------------------------------------------------------------------------------



#Step # 1 - set variable 
random_starting_variable = ''


#step 3 

def get_text_file (text):
	
	#OPEN TEXT from file "Concept.text" and read it
	with open("Concept.txt","r") as myfile:
		global data
		data = myfile.read().replace('\n', ' ')
		
	#text = data = Set of data string that we extracted from a file
	text = data
	
	#Extract the "title" and "description" from text variable
	title_info = re.findall(r'TITLE: (.+?) DESCRIPTION: ',text)
	description_info = re.findall(r'DESCRIPTION: (.+?)/END',text)
	
	count = 0
	list_length = len(title_info)
	
	
	print '''<!DOCTYPE html>'''
	print '''<html>  '''
	print '''<body>'''
	
	#while loop program
	while count < list_length:
		
		#TITLE text
		title_list = title_info[count]
		
		#DESCRIPTION text 
		description_list = description_info[count]
		
		
		#Use class "Concept" to print information 
		html_display = Concept (title_list,description_list)
		print html_display.generate_html()
        
        # Keep count 
		count = count + 1
	
	print "       "
	print "</body>"
	print "</html>"
		

# Step 2 - 
get_text_file(random_starting_variable)


