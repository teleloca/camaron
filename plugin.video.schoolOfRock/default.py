# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon,xbmcgui,xbmcplugin

addonID = 'plugin.video.schoolOfRock'
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')


# main menu folders http://rockaxis.com.co/sites/default/files/node/articulos/imagen/120363.jpg
folderlist = [
        ("Batería", "http://static.wixstatic.com/media/4facbb_364074deeb0545998ada5028a477456f~mv2.jpg_256"),
        ("Guitarra", "http://static.wixstatic.com/media/4facbb_da54e65e6e274839b4ea4b8fd3e5aa0c.jpg_256"),
        ("Violín", "http://static.wixstatic.com/media/83eecc_34b966a3de6e47b09e255000ae4b03cd~mv2.jpg_256" ),
        ("Armónica", "http://www.haworthguitars.com.au/application/assets/uploads/products/detail_images/1101B.jpg" ),

        ]

fanartFolder = {
        "Guitarra":"http://www.directordealabanza.com/wp-content/uploads/2014/02/Playing-Acoustic-Guitar-HD-Wallpaper.jpg",
        "Violín":"https://allwallpapers.info/wp-content/uploads/2016/05/21728-violin-1920x1080-music-wallpaper.jpeg",
        "Batería":"http://www.albertochala.com/wp-content/uploads/Bateria2.jpeg",
        "Armónica":"https://i.ytimg.com/vi/Vp9CsHCd3Xg/maxresdefault.jpg",

        }
                



# channels for each folder
violinChannels=[
        ("Cadenza Strings", "user/cadenzastringsnc", 'https://yt3.ggpht.com/-yUnhviHx_0I/AAAAAAAAAAI/AAAAAAAAAAA/VslbMXvnvHo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Fiddle Hed", "channel/UCjDhiaiSoTPHQ7t-QfanVMw", 'https://yt3.ggpht.com/-YvrssmUbpME/AAAAAAAAAAI/AAAAAAAAAAA/sREj0G2rXZM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Violin Tutor Pro", "user/violintutorpro", 'https://yt3.ggpht.com/-2wvpSOBPVBo/AAAAAAAAAAI/AAAAAAAAAAA/bIN6HB1eNFk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Kiko Perera", "user/sgeolan28", 'https://yt3.ggpht.com/-t-bBZ7i9J5o/AAAAAAAAAAI/AAAAAAAAAAA/QfDty67FrPM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("ViolinTips83", "channel/UCjqfcWLVA9lH2VTEIg-LIgQ", 'https://yt3.ggpht.com/-WdMjY50WMmM/AAAAAAAAAAI/AAAAAAAAAAA/SoLjTEXf9CY/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Joaquín Blasco Pagán", "channel/UCd_XPMk4Nkuege9fAeQIC3Q", 'https://yt3.ggpht.com/-l6wfKOhmIzk/AAAAAAAAAAI/AAAAAAAAAAA/81zDTYMPP0k/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Como Tocar Violín", "channel/UC7p0HIwf72fJhBzw_N7Y9GA", 'https://yt3.ggpht.com/-qlNEaLcxyec/AAAAAAAAAAI/AAAAAAAAAAA/reJInCjQmWc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("EasyViolinLesson", "channel/UCHPjB5YzMdfIA0a_Z3i6R7A", 'https://yt3.ggpht.com/-e_13FIv2CJg/AAAAAAAAAAI/AAAAAAAAAAA/MO5rBWIiiU4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Fiddlerman", "user/1stfiddlerman", 'https://yt3.ggpht.com/-b-cF322D6bE/AAAAAAAAAAI/AAAAAAAAAAA/srou6_8sung/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),
        ("Violin Lab Channel", "user/violinlab", 'https://yt3.ggpht.com/-ojiGZgoPP0I/AAAAAAAAAAI/AAAAAAAAAAA/dJpul280rVo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg'),

        ]

guitarraChannels=[
        ("Guitarrista Paso a paso", "channel/UCFVsw4eL_QsmhapKW6xmIKA", "https://yt3.ggpht.com/-0r_yWKEqdjU/AAAAAAAAAAI/AAAAAAAAAAA/5GTxKzLjE0s/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Gurú de la Guitarra", "user/GuruDeLaGuitarra", "https://yt3.ggpht.com/-ujyKYdV_xUI/AAAAAAAAAAI/AAAAAAAAAAA/SkaLzLxDJ08/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("MiguelRiveraGuitar", "user/MiguelRiveraGuitar", "https://yt3.ggpht.com/-hmBR7CoIYdU/AAAAAAAAAAI/AAAAAAAAAAA/A7uVnDfECyM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Enguitarra", "user/EnGuitarra", "https://yt3.ggpht.com/-sh3O2Xn53V8/AAAAAAAAAAI/AAAAAAAAAAA/dYsZvqh8kuA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("FermiGuitarra", "channel/UCWDI9w1vO56lEuyoNa16O8A", "https://yt3.ggpht.com/-gcWZkBsFCww/AAAAAAAAAAI/AAAAAAAAAAA/bzFnK57qD6Y/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Chachi Guitar", "channel/UCA-i40P-jwXWoTQMsxBqHBA", "https://yt3.ggpht.com/-XQEq9G_tbqo/AAAAAAAAAAI/AAAAAAAAAAA/xWHieZvyt8w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("ChordHouse", "channel/UCeELeNRiPUCZUugEH9vD6Cg", "https://yt3.ggpht.com/-arl6fdvYTRI/AAAAAAAAAAI/AAAAAAAAAAA/6Dg1l9xOnm0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Kalinchita", "user/kalinchita", "https://yt3.ggpht.com/-nb3jHMjO7tQ/AAAAAAAAAAI/AAAAAAAAAAA/JKM9iDNDCf8/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Tus Clases de Guitarra", "channel/UC3k4Tn0XRZ2urVwBLY5s9Zw", "https://yt3.ggpht.com/-hGvQDOVdLBM/AAAAAAAAAAI/AAAAAAAAAAA/gjRRuNz2-hA/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Guitarra Viva", "channel/UCXm0v3a9g17bSATE-DMMxRg", "https://yt3.ggpht.com/-DqfI8-KgQ5k/AAAAAAAAAAI/AAAAAAAAAAA/f4BCtnDHpDQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),

        ]

bateriaChannels=[
        ("Mass Batería", "user/massbateria", "https://yt3.ggpht.com/-13P3MEPOjxU/AAAAAAAAAAI/AAAAAAAAAAA/MgLLJQiReNQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Zeben Drums", "channel/UCKdv1jB1mwjAXowtgU4vUXA", "https://yt3.ggpht.com/-6vVPVwAS8P8/AAAAAAAAAAI/AAAAAAAAAAA/zXBIcOjNxFg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Drumer Tv Argentina", "user/DrummerTVArgentina", "https://yt3.ggpht.com/-JYqXjP3BjS4/AAAAAAAAAAI/AAAAAAAAAAA/_my4dWYHtLU/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Mr Online Drums Tv", "user/MrOnlineDrumsTV", "https://yt3.ggpht.com/-BybZI0PSjC8/AAAAAAAAAAI/AAAAAAAAAAA/FtANm_OMLGQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Felipe Arroyave Giraldo", "user/FelipeDrummer87","https://yt3.ggpht.com/-NVM3i2Hqk1A/AAAAAAAAAAI/AAAAAAAAAAA/syr-YHodDXk/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Adam Tuminaro", "user/adamtuminaro89", "https://yt3.ggpht.com/-CeGtALCibbI/AAAAAAAAAAI/AAAAAAAAAAA/pIg0TGZ1Rrg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Juan Carlito Mendoza", "user/jmensticks", "https://yt3.ggpht.com/-EwSvC43VRu0/AAAAAAAAAAI/AAAAAAAAAAA/gVz5JqA-sFo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Rdavidr", "user/rdavidr", "https://yt3.ggpht.com/-OWzl0g30MKA/AAAAAAAAAAI/AAAAAAAAAAA/j18dB5mcFHQ/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Mastermildb", "user/mastermildb", "https://yt3.ggpht.com/-guu0vPqVeys/AAAAAAAAAAI/AAAAAAAAAAA/_K2vTFaVuoc/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Moro Tovar", "user/comotocarbateria", "https://yt3.ggpht.com/-g6grDw6Rijk/AAAAAAAAAAI/AAAAAAAAAAA/1sAmX6KOS1c/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("El DrumBlog", "user/ElDrumBlogOficial", "https://yt3.ggpht.com/-m9AcZfxG7vQ/AAAAAAAAAAI/AAAAAAAAAAA/zvJPag-pnP0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Mike Johnston", "user/drumteacher76", "https://yt3.ggpht.com/-kbykKN13eXU/AAAAAAAAAAI/AAAAAAAAAAA/UXw9JhAu4J4/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Drumeo", "user/freedrumlessons", "https://yt3.ggpht.com/-VM4FYFxDvN8/AAAAAAAAAAI/AAAAAAAAAAA/kWWPfo_AjMM/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ]

harmonicaChannels=[
        ("LearnTheHarmonica.com", "user/learntheharmonica", "https://yt3.ggpht.com/-m_23XlI-NiA/AAAAAAAAAAI/AAAAAAAAAAA/4FntSUa40L0/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Modern Blues Harmonica", "user/KudzuRunner"+ '\#g/', "https://yt3.ggpht.com/-OcamKzgjMHs/AAAAAAAAAAI/AAAAAAAAAAA/aO8VRds6CQs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("harmonicalessons", "user/harmonicalessons", "https://yt3.ggpht.com/-C_tZyFcuzEM/AAAAAAAAAAI/AAAAAAAAAAA/1pPKrTTUabs/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Funky Harp", "user/FunkyHarp", "https://yt3.ggpht.com/-3nq8m-B9bIw/AAAAAAAAAAI/AAAAAAAAAAA/YiYZwuQGj2w/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("JPAllen", "user/jpallen7", "https://yt3.ggpht.com/-yDdKZmshzkc/AAAAAAAAAAI/AAAAAAAAAAA/H6J06BtpiAg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Tomlin Leckie", "user/tomlinleckie", "https://yt3.ggpht.com/-WqoMxpYivTQ/AAAAAAAAAAI/AAAAAAAAAAA/SSdEMo8n2Yo/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Aprende Armónica", "user/aprendearmonica", "https://yt3.ggpht.com/-pNzWw2KqLtQ/AAAAAAAAAAI/AAAAAAAAAAA/-XiO2eOsszw/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Harpvard Universidad de la Armónica", "channel/UC3IWTq0prfJsB5c1SFhZtaw", "https://yt3.ggpht.com/-LQZ6Bw6Qpcc/AAAAAAAAAAI/AAAAAAAAAAA/dXBHPcQzens/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),
        ("Canal de lecciones de Armónica", "user/leccionesdearmonica", "https://yt3.ggpht.com/-QaENI0fTz4E/AAAAAAAAAAI/AAAAAAAAAAA/SrtJhGO1Xkg/s900-c-k-no-mo-rj-c0xffffff/photo.jpg"),

        ]        

# Entry point
def run():
    plugintools.log("START PLUGIN")
    params = plugintools.get_params()  
    action = params.get("action")

    # create the main menu
    if action is None:  
        for name, icon in folderlist:
            plugintools.add_item(action='main', title=name,url="",thumbnail=icon,folder=True, fanart='http://rockaxis.com.co/sites/default/files/node/articulos/imagen/120363.jpg' )

        #plugintools.close_item_list()
    elif action == 'main':
        title = params.get('title')
        buildChannel(title)
        

    else:
        exec action+"(params)"  
        plugintools.close_item_list() 

        #exec action+"(params)"
        
    plugintools.close_item_list()




    # plugintools.log("schoolOfRock.run")
    
    # # Get params
    # params = plugintools.get_params()
    
    # if params.get("action") is None:
    #     main_list(params)
    # else:
    #     action = params.get("action")
    #     exec action+"(params)"
    
    # plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("schoolOfRock.main_list "+repr(params))
#for name, id, icon in channellist:
#	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True, fanart="http://rockaxis.com.co/sites/default/files/node/articulos/imagen/120363.jpg" )

def buildChannel(title):
    plugintools.log("RUN_CHAN" + title)
    if title == 'Violín':
        createChannelsFromFolder(violinChannels, str(fanartFolder['Violín']))
    elif title == 'Guitarra':
        createChannelsFromFolder(guitarraChannels, fanartFolder['Guitarra'])
    elif title == 'Batería':
        createChannelsFromFolder(bateriaChannels, fanartFolder['Batería'])
    elif title == 'Armónica':
        createChannelsFromFolder(harmonicaChannels, fanartFolder['Armónica'])

    
def createChannelsFromFolder(folder, fanart):
    plugintools.log("RUN_CHAN")
    for name, id, icon in folder:
        plugintools.add_item(title=name,url="plugin://plugin.teleloca.support.ytb/"+id+"/",thumbnail=icon,folder=True, fanart=fanart)



run()