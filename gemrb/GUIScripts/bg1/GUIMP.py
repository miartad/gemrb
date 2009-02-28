#Single Player Party Formation
import GemRB

PartyFormationWindow = 0
ExitWindow = 0

def OnLoad():
	global PartyFormationWindow
	GemRB.LoadWindowPack("GUIMP")
	
	PartyFormationWindow = GemRB.LoadWindowObject(0)
	
	ExitButton = PartyFormationWindow.GetControl(30)
	ExitButton.SetText(13906)
	ExitButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, "ExitPress")
	ExitButton.SetFlags(IE_GUI_BUTTON_CANCEL, OP_OR)

	ModifyCharactersButton = PartyFormationWindow.GetControl(43)
	ModifyCharactersButton.SetText(18816)
	ModifyCharactersButton.SetState(IE_GUI_BUTTON_DISABLED)
	ModifyCharactersButton.SetEvent(IE_GUI_BUTTON_ON_PRESS,"ModifyCharactersPress")

	DoneButton = PartyFormationWindow.GetControl(28)
	DoneButton.SetText(11973)
	Portraits = 0
	
	for i in range(18,24):
		Label = PartyFormationWindow.GetControl(0x10000012+i)
		#removing this label, it just disturbs us
		Label.SetSize(0, 0)
		Button = PartyFormationWindow.GetControl(i-12)
		ResRef = GemRB.GetPlayerPortrait(i-17, 1)
		if ResRef == "":
			Button.SetFlags(IE_GUI_BUTTON_NORMAL,OP_SET)
		else:
			Button.SetPicture(ResRef)
			Button.SetFlags(IE_GUI_BUTTON_PICTURE, OP_OR)
			Portraits = Portraits+1

		Button.SetVarAssoc("Slot",i-17)
		Button.SetEvent(IE_GUI_BUTTON_ON_PRESS, "GeneratePress")

		Button = PartyFormationWindow.GetControl(i)
		Button.SetVarAssoc("Slot",i-17)
		if ResRef == "":
			Button.SetText(10264)
		else:
			Button.SetText(GemRB.GetPlayerName(i-17,0) )

		Button.SetEvent(IE_GUI_BUTTON_ON_PRESS, "GeneratePress")
	
	if Portraits == 0:
		DoneButton.SetState(IE_GUI_BUTTON_DISABLED)
	else:
		DoneButton.SetState(IE_GUI_BUTTON_ENABLED)
	DoneButton.SetEvent(IE_GUI_BUTTON_ON_PRESS,"EnterGamePress")

	PartyFormationWindow.SetVisible(1)
	return
	
def ExitPress():
	global PartyFormationWindow, ExitWindow
	PartyFormationWindow.SetVisible(0)
	ExitWindow = GemRB.LoadWindowObject(7)
	
	TextArea = ExitWindow.GetControl(0)
	TextArea.SetText(11329)
	
	CancelButton = ExitWindow.GetControl(2)
	CancelButton.SetText(13727)
	CancelButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, "ExitCancelPress")
	CancelButton.SetFlags(IE_GUI_BUTTON_CANCEL, OP_OR)
	
	DoneButton = ExitWindow.GetControl(1)
	DoneButton.SetText(11973)
	DoneButton.SetEvent(IE_GUI_BUTTON_ON_PRESS, "ExitDonePress")
	DoneButton.SetFlags(IE_GUI_BUTTON_DEFAULT, OP_OR)
	
	ExitWindow.SetVisible(1)
	return
	
def ExitDonePress():
	global PartyFormationWindow, ExitWindow
	if ExitWindow:
		ExitWindow.Unload()
	if PartyFormationWindow:
		PartyFormationWindow.Unload()
	GemRB.SetNextScript("Start")
	return
	
def ExitCancelPress():
	global PartyFormationWindow, ExitWindow
	if ExitWindow:
		ExitWindow.Unload()
	PartyFormationWindow.SetVisible(1)
	return
	
def GeneratePress():
	global PartyFormationWindow
	slot = GemRB.GetVar("Slot")
	ResRef = GemRB.GetPlayerPortrait(slot, 0)
	if ResRef:
		print "Already existing slot, we should drop it"
	if PartyFormationWindow:
		PartyFormationWindow.Unload()
	GemRB.SetNextScript("CharGen")
	return

def EnterGamePress():
	GemRB.EnterGame()
	return

