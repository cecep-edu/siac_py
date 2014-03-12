

if(Ext.isEmpty(IAEN.BASE_PATH)){
	IAEN.log("Por favor , verifica la ruta de 'IAEN.BASE_PATH' constante!");
	Ext.Msg.alert("Error!!","Por favor , verifica la ruta de 'IAEN.BASE_PATH' constante!");
}

Ext.Loader.setConfig({
	enabled : true,
	paths   : {
		IAEN 	: IAEN.desktop.Constants.JS_PATH+"IAEN",
		Ext		: IAEN.desktop.Constants.JS_PATH+"extjs"
	} 
});

Ext.require("IAEN.abstract.MessageBox");
Ext.require("IAEN.desktop.Application");


Ext.onReady(function(){

	IAEN.App = Ext.create("IAEN.desktop.Application",{
		name		: "IAEN.App",
		listeners	: {
			ready	: function(){
				setTimeout(function(){
					Ext.get("loading").remove();
					Ext.get("loading-mask").fadeOut({remove:true});
				},250);
			}
		}
	});
	
});
