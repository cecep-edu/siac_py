/**
 * @class IAEN.desktop.Constants
 * @extends Object
 * requires 
 *
 * Description
 * Constantes generales del sistema.
 *
 **/


Ext.define("IAEN.desktop.Constants",{
	alternateClassName	: "IAEN.Constants" ,
	singleton	: true,

	/* login url sistema/cargar_escritorio/ */
	DESKTOP_CONFIGURATION_URL	: "sistema/cargar_escritorio/",
	DESKTOP_LOGIN_URL			: "sistema/login_user/",
	DESKTOP_REGISTRAR_URL		: "sistema/registrar_user/",
	DESKTOP_LOGOUT_URL			: "index",
	DESKTOP_HOME_URL			: "home",
	
	/* The directory where the avatars are */
	USERS_AVATAR_PATH			: IAEN.BASE_PATH+"resources/avatars/",
	
	/* The directory where the JS's are*/
	JS_PATH						: IAEN.BASE_PATH,
	
	/* Default width and height for windows */
	DEFAULT_WINDOW_WIDTH		: 800,
	DEFAULT_WINDOW_HEIGHT		: 480,
	LOGIN_IMAGE					: IAEN.BASE_PATH+"resources/images/login-image.png"
	
});
