/**
 * @class IAEN.abstract.TreeStore
 * @extends Ext.data.TreeStore
 * requires 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.abstract.TreeStore",{
	extend		: "Ext.data.TreeStore",
	
	autoLoad	: true,
	folderSort	: true,
	
	constructor	: function() {
		var me = this;
		
        me.proxy = {
			type	: "ajax",
			url		: me.url,//antes IAEN.BASE_PATH + "index.html/"+me.url
			params	: this.params
		};
		
		me.callParent();
	}
});