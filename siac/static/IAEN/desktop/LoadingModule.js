/**
 * @class IAEN.desktop.LoadingModule
 * @extends IAEN.ui.ModalWindow
 * requires 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.desktop.LoadingModule",{
	extend		: "IAEN.abstract.ModalWindow",

	bodyCls		: "IAEN-loading-module",
	layout		: "auto",
	width		: 400,
	height		: 240,
	closable	: false,
	
	initComponent	: function() {
		var me = this;
		
        me.html = "<p>Please wait, loading module...</p>";

		me.callParent();
	}
});