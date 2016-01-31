groupTags = ["prites", "sounds", "backgrounds", "paths", "scripts", "shaders", "fonts", "timelines", "objects"]
assetTags = ["prite", "sound", "background", "path", "script", "shader", "font", "timeline", "object"]
objectTags = ["event"]
pathTags = ["point"]
roomTags = ["code"]

eventNumber = {
	"0": "Normal",
	"0": "StepNormal",
	"1": "StepBegin",
	"2": "StepEnd",
	"0": "DrawNormal",
	"64": "DrawGUI",
	"64": "DrawResize",
	"0": "OutsideRoom",
	"1": "IntersectBoundary",
	"2": "GameStart",
	"3": "GameEnd",
	"4": "RoomStart",
	"5": "RoomEnd",
	"6": "NoMoreLives",
	"7": "AnimationEnd",
	"8": "EndOfPath",
	"9": "NoMoreHealth",
	"10": "User0",
	"11": "User1",
	"12": "User2",
	"13": "User3",
	"14": "User4",
	"15": "User5",
	"16": "User6",
	"17": "User7",
	"18": "User8",
	"19": "User9",
	"20": "User10",
	"21": "User11",
	"22": "User12",
	"23": "User13",
	"24": "User14",
	"25": "User15",
	"40": "OutsideView0",
	"41": "OutsideView1",
	"42": "OutsideView2",
	"43": "OutsideView3",
	"44": "OutsideView4",
	"45": "OutsideView5",
	"46": "OutsideView6",
	"47": "OutsideView7",
	"50": "BoundaryView0",
	"51": "BoundaryViewView1",
	"52": "BoundaryViewView2",
	"53": "BoundaryViewView3",
	"54": "BoundaryViewView4",
	"55": "BoundaryViewView5",
	"56": "BoundaryViewView6",
	"57": "BoundaryViewView7",
	"63": "AyscDialog",
	"66": "AyscIAP",
	"67": "AyscCloud",
	"68": "AyscNetworking",
	"8": "KeyboardBackspace",
	"13": "KeyboardEnter",
	"16": "KeyboardShift",
	"17": "KeyboardControl",
	"18": "KeyboardAlt",
	"27": "KeyboardEscape",
	"32": "KeyboardSpace",
	"33": "KeyboardPageUp",
	"34": "KeyboardPageDown",
	"35": "KeyboardEnd",
	"36": "KeyboardHome",
	"37": "KeyboardArrowLeft",
	"38": "KeyboardArrowUp",
	"39": "KeyboardArrowRight",
	"40": "KeyboardArrowDown",
	"45": "KeyboardInsert",
	"46": "KeyboardDelete",
	"48": "Keyboard0",
	"49": "Keyboard1",
	"50": "Keyboard2",
	"51": "Keyboard3",
	"52": "Keyboard4",
	"53": "Keyboard5",
	"54": "Keyboard6",
	"55": "Keyboard7",
	"56": "Keyboard8",
	"57": "Keyboard9",
	"65": "KeyboardA",
	"66": "KeyboardB",
	"67": "KeyboardC",
	"68": "KeyboardD",
	"69": "KeyboardE",
	"70": "KeyboardF",
	"71": "KeyboardG",
	"72": "KeyboardH",
	"73": "KeyboardI",
	"74": "KeyboardJ",
	"75": "KeyboardK",
	"76": "KeyboardL",
	"77": "KeyboardM",
	"78": "KeyboardN",
	"79": "KeyboardO",
	"80": "KeyboardP",
	"81": "KeyboardQ",
	"82": "KeyboardR",
	"83": "KeyboardS",
	"84": "KeyboardT",
	"85": "KeyboardU",
	"86": "KeyboardV",
	"87": "KeyboardW",
	"88": "KeyboardX",
	"89": "KeyboardY",
	"90": "KeyboardZ",
	"96": "KeyboardKeyPad0",
	"97": "KeyboardKeyPad1",
	"98": "KeyboardKeyPad2",
	"99": "KeyboardKeyPad3",
	"100": "KeyboardKeyPad4",
	"101": "KeyboardKeyPad5",
	"102": "KeyboardKeyPad6",
	"103": "KeyboardKeyPad7",
	"104": "KeyboardKeyPad8",
	"105": "KeyboardKeyPad9",
	"106": "KeyboardKeyPadMultiply",
	"107": "KeyboardKeyPadAdd",
	"109": "KeyboardKeyPadSubstract",
	"110": "KeyboardKeyPadPeriod",
	"111": "KeyboardKeyPadSlash",
	"112": "KeyboardF1",
	"113": "KeyboardF2",
	"114": "KeyboardF3",
	"115": "KeyboardF4",
	"116": "KeyboardF5",
	"117": "KeyboardF6",
	"118": "KeyboardF7",
	"119": "KeyboardF8",
	"120": "KeyboardF9",
	"121": "KeyboardF10",
	"122": "KeyboardF11",
	"123": "KeyboardF12"
}

eventKind = ["Create",
"Destroy",
"Alarm",
"Step",
"Collision",
"Keyboard",
"Mouse",
"Other",
"Draw",
"Press",
"Release",
"Asyncronous",
"Unknown"]

actionID = {"604": "someaction"}

functions = [
"hspeed"
]

variables = [
"curret_time"
]

colorCode = {
"comment": "black",
"function": "white",
"operator": "red",
}

def path():
	''' absolute project path from any file/folder in it '''
	return

def groups(projectPath):
	''' all groups ''' 
	return

def assets(projectPath):
	''' all assets ''' 
	return
	
def groupsAssets(projectPath, group):
	''' assets in group ''' 
	assets = []
	name = ""
	soup = ""
	for tag in soup.find_all(group+""):
		group, name = tag.text.split('//')
		assets.append(name)
	return assets
	
def props(projectPath, asset):
	''' one assets properties ''' 
	return
	
def func(line):
	''' color code text ''' 
	return "somewird qt coloring per line function"
	
def func():
	'''  ''' 
	return


#   usage
# gmx.assets("gmxpath", "somegroup")
# 	[obj_one, obj_two, obj_three]
# 
# 