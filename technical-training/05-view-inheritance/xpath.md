//field[@name='is_company']  => set cursor position by xpath on view

/form/sheet/div

expr="//button[@name='toggle_active']/.." => /.. to go up one element or /../.. to go up 2 and so on

//div[@name='button_box']


xpath => un petit langage xml pour les fichiers xml

position = ".." => to select new element position compared to cursor
	after
	before
	inside
	attributes => to change attributes of an element <xpath expr="//field[@name='is_company']" position="attributes">
								<attribute name="invisible">1</attribute> 
							</xpath> 
	replace = replace expr element with new element(s) inside xpath

<field name="is_company" position="after">  => dans la vue enfant
	... => put new fields you want to add here
</field>

<mode="extension" > => jouer sur la vue d'un model 
	"primary" => copier la vue sur une class enfant

to not to rewrite form view you can auto generate and edit formview on debug mode to copy paste in your xml file
