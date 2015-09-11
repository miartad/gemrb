/* GemRB - Infinity Engine Emulator
 * Copyright (C) 2003 The GemRB Project
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 *
 */

/**
 * @file Window.h
 * Declares Window, class serving as a container for Control/widget objects 
 * and displaying windows in GUI
 * @author The GemRB Project
 */

#ifndef WINDOW_H
#define WINDOW_H

#include "View.h"
#include "WindowManager.h"

#include <vector>

namespace GemRB {

class Control;
class Sprite2D;

/**
 * @class Window
 * Class serving as a container for Control/widget objects 
 * and displaying windows in GUI.
 */

class GEM_EXPORT Window : public View {
public:
	// !!! Keep these synchronized with GUIDefines.py !!!
	enum WindowPosition {
		PosTop = 1,		// top
		PosBottom = 2,	// bottom
		PosVmid = 3,	// top + bottom = vmid
		PosLeft = 4,	// left
		PosRight = 8,	// right
		PosHmid = 12,	// left + right = hmid
		PosCentered = 15// top + bottom + left + right = center
	};
	enum WindowFlags {
		Draggable = 1,
		Borderless = 2
	};

protected:
	void SubviewAdded(View* view, View* parent);
	void SubviewRemoved(View* view, View* parent);

	void SizeChanged(const Size&);
	void WillDraw();

	void DrawSelf(Region drawFrame, const Region& clip);

	bool TrySetFocus(View*);

	inline void DispatchMouseOver(const Point&);
	inline void DispatchMouseDown(const Point&, unsigned short /*Button*/, unsigned short /*Mod*/);
	inline void DispatchMouseUp(const Point&, unsigned short /*Button*/, unsigned short /*Mod*/);
	inline void DispatchMouseWheelScroll(const Point&, short x, short y);

public:
	Window(const Region& frame, WindowManager& mgr);
	~Window();

	void Close();
	void Focus();
	bool DisplayModal(WindowManager::ModalShadow = WindowManager::ShadowNone);

	bool OnSpecialKeyPress(unsigned char key);

	/** Sets 'ctrl' as Focused */
	void SetFocused(Control* ctrl);
	void SetPosition(WindowPosition);
	void SetDisabled(bool);
	bool IsDisabled() { return disabled; }
	/** Returns last focused control */
	Control* GetFocus() const;
	View* FocusedView() const { return focusView; }
	const String& TooltipText() const;

	/** Redraw controls of the same group */
	void RedrawControls(const char* VarName, unsigned int Sum);

	bool DispatchEvent(const Event&);
	void OnMouseOver(const Point&);
	void OnMouseDown(const Point&, unsigned short /*Button*/, unsigned short /*Mod*/);
	void OnMouseLeave(const Point&, const DragOp*);

private: // Private attributes
	/** Controls Array */
	std::vector< Control*> Controls;
	View* focusView; // keyboard focus
	View* trackingView; // out of bounds mouse tracking
	View* hoverView; // view the mouse was last over
	Holder<DragOp> drag;
	unsigned long lastMouseMoveTime;
	Point dragOrigin;
	bool isDragging;
	bool disabled;
	VideoBuffer* backBuffer;
	WindowManager& manager;
};

}

#endif
