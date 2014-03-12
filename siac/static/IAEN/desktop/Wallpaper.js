/**
 * @class IAEN.desktop.Wallpaper
 * @extends Ext.Component
 * requires 
 *
 * Description
 *
 *
 **/

Ext.define("IAEN.desktop.Wallpaper",{
	extend				: "Ext.Component",
	alternateClassName	: "IAEN.Wallpaper" ,
	
	statics				: {
		CENTERED	: "centered",
		TILED		: "tiled",
		STRETCH		: "stretch"
	},
	cls			: "IAEN-wallpaper",
	stretch		: false,
	mode		: "centered",
    wallpaper	: null,

	initComponent	: function() {
		var me = this;
		
	    me.html = '<img src="'+Ext.BLANK_IMAGE_URL+'">';
        
		me.callParent();
	},
	
	afterRender: function () {
        var me = this;
        me.callParent();

		if(me.wallpaper){
			me.setWallpaper(me.wallpaper, me.mode);
		}
    },

	applyState: function () {
        var me = this, old = me.wallpaper;
        me.callParent(arguments);
        if (old != me.wallpaper) {
            me.setWallpaper(me.wallpaper);
        }
    },

    getState: function () {
        return this.wallpaper && { wallpaper: this.wallpaper };
    },

	setWallpaper: function (wallpaper, mode) {
        var me = this, imgEl, bkgnd;

        me.mode = mode;
        me.wallpaper = wallpaper;

        if (me.rendered) {
            imgEl = me.el.dom.firstChild;

			Ext.fly(imgEl).hide();
			
            if(me.mode === "stretch") {
                imgEl.src = wallpaper;

                me.el.removeCls('IAEN-wallpaper-tiled');
				me.el.removeCls('IAEN-wallpaper-centered');
                Ext.fly(imgEl).setStyle({
                    width: '100%',
                    height: '100%'
                }).show();
            } else if(me.mode === "centered"){
                bkgnd = 'url('+wallpaper+')';

				me.el.removeCls('IAEN-wallpaper-tiled');
                me.el.addCls('IAEN-wallpaper-centered');
            }else{
				bkgnd = 'url('+wallpaper+')';

				me.el.removeCls('IAEN-wallpaper-centered');
				me.el.addCls('IAEN-wallpaper-tiled');
			}

            me.el.setStyle({
                backgroundImage: bkgnd || ''
            });
        }
        return me;
    }
});