Name: tk
Version: 8.5.10
Release: 1.0
Summary: A GUI Toolkit based on Tcl
URL: http://www.tcl.tk
Group: Development/TCL
License: BSD
Source: http://prdownloads.sourceforge.net/tcl/tk%{version}-src.tar.gz
BuildRequires: grep, sed, gawk, make
BuildRequires: gcc
BuildRequires: kernel-headers, eglibc-devel
BuildRequires: libX11, xorg-xproto


%description
Tk is a graphical user interface toolkit that takes developing desktop
applications to a higher level than conventional approaches. Tk is the
standard GUI not only for Tcl, but for many other dynamic languages,
and can produce rich, native applications that run unchanged across
Windows, Mac OS X, Linux and more.


%files
%defattr(-, root, root)
%doc README changes license.terms ChangeLog*

%{_bindir}/wish
%{_bindir}/wish8.5

%{_libdir}/libtk8.5.so

%dir %{_libdir}/tk8.5
%{_libdir}/tk8.5/*.tcl
%{_libdir}/tk8.5/tclIndex

%dir %{_libdir}/tk8.5/images
%{_libdir}/tk8.5/images/README
%{_libdir}/tk8.5/images/*.*

%dir %{_libdir}/tk8.5/msgs
%{_libdir}/tk8.5/msgs/*.msg

%dir %{_libdir}/tk8.5/ttk
%{_libdir}/tk8.5/ttk/*.tcl

%dir %{_libdir}/tk8.5/demos
%{_libdir}/tk8.5/demos/README
%{_libdir}/tk8.5/demos/license.terms
%{_libdir}/tk8.5/demos/browse
%{_libdir}/tk8.5/demos/hello
%{_libdir}/tk8.5/demos/ixset
%{_libdir}/tk8.5/demos/rmt
%{_libdir}/tk8.5/demos/rolodex
%{_libdir}/tk8.5/demos/square
%{_libdir}/tk8.5/demos/tclIndex
%{_libdir}/tk8.5/demos/tcolor
%{_libdir}/tk8.5/demos/timer
%{_libdir}/tk8.5/demos/widget
%{_libdir}/tk8.5/demos/*.tcl
%{_libdir}/tk8.5/demos/*.msg

%dir %{_libdir}/tk8.5/demos/images
%{_libdir}/tk8.5/demos/images/*.*

%doc %{_mandir}/man1/wish.1*
%doc %{_mandir}/mann/bell.n*
%doc %{_mandir}/mann/wm.n*
%doc %{_mandir}/mann/bind.n*
%doc %{_mandir}/mann/bindtags.n*
%doc %{_mandir}/mann/bitmap.n*
%doc %{_mandir}/mann/button.n*
%doc %{_mandir}/mann/canvas.n*
%doc %{_mandir}/mann/checkbutton.n*
%doc %{_mandir}/mann/ttk::scale.n*
%doc %{_mandir}/mann/ttk::combobox.n*
%doc %{_mandir}/mann/clipboard.n*
%doc %{_mandir}/mann/colors.n*
%doc %{_mandir}/mann/console.n*
%doc %{_mandir}/mann/cursors.n*
%doc %{_mandir}/mann/destroy.n*
%doc %{_mandir}/mann/entry.n*
%doc %{_mandir}/mann/event.n*
%doc %{_mandir}/mann/focus.n*
%doc %{_mandir}/mann/ttk::radiobutton.n*
%doc %{_mandir}/mann/font.n*
%doc %{_mandir}/mann/frame.n*
%doc %{_mandir}/mann/ttk::scrollbar.n*
%doc %{_mandir}/mann/grab.n*
%doc %{_mandir}/mann/grid.n*
%doc %{_mandir}/mann/image.n*
%doc %{_mandir}/mann/keysyms.n*
%doc %{_mandir}/mann/label.n*
%doc %{_mandir}/mann/labelframe.n*
%doc %{_mandir}/mann/listbox.n*
%doc %{_mandir}/mann/loadTk.n*
%doc %{_mandir}/mann/lower.n*
%doc %{_mandir}/mann/menu.n*
%doc %{_mandir}/mann/menubutton.n*
%doc %{_mandir}/mann/message.n*
%doc %{_mandir}/mann/ttk::separator.n*
%doc %{_mandir}/mann/option.n*
%doc %{_mandir}/mann/ttk::sizegrip.n*
%doc %{_mandir}/mann/options.n*
%doc %{_mandir}/mann/pack-old.n*
%doc %{_mandir}/mann/pack.n*
%doc %{_mandir}/mann/ttk::spinbox.n*
%doc %{_mandir}/mann/photo.n*
%doc %{_mandir}/mann/place.n*
%doc %{_mandir}/mann/radiobutton.n*
%doc %{_mandir}/mann/raise.n*
%doc %{_mandir}/mann/scale.n*
%doc %{_mandir}/mann/scrollbar.n*
%doc %{_mandir}/mann/selection.n*
%doc %{_mandir}/mann/send.n*
%doc %{_mandir}/mann/spinbox.n*
%doc %{_mandir}/mann/text.n*
%doc %{_mandir}/mann/tk.n*
%doc %{_mandir}/mann/panedwindow.n*
%doc %{_mandir}/mann/tkerror.n*
%doc %{_mandir}/mann/tkvars.n*
%doc %{_mandir}/mann/tkwait.n*
%doc %{_mandir}/mann/toplevel.n*
%doc %{_mandir}/mann/tk_*.n*
%doc %{_mandir}/mann/ttk::button.n*
%doc %{_mandir}/mann/ttk::style.n*
%doc %{_mandir}/mann/ttk::checkbutton.n*
%doc %{_mandir}/mann/ttk::entry.n*
%doc %{_mandir}/mann/ttk::frame.n*
%doc %{_mandir}/mann/ttk_image.n*
%doc %{_mandir}/mann/ttk::intro.n*
%doc %{_mandir}/mann/ttk::label.n*
%doc %{_mandir}/mann/ttk::treeview.n*
%doc %{_mandir}/mann/ttk::labelframe.n*
%doc %{_mandir}/mann/ttk_vsapi.n*
%doc %{_mandir}/mann/ttk::menubutton.n*
%doc %{_mandir}/mann/ttk::notebook.n*
%doc %{_mandir}/mann/ttk::widget.n*
%doc %{_mandir}/mann/ttk::panedwindow.n*
%doc %{_mandir}/mann/winfo.n*
%doc %{_mandir}/mann/ttk::progressbar.n*


%post -p %{__ldconfig}
%postun -p %{__ldconfig}


%package devel
Summary: Header Files and C API Documentation for Tk
Group: Development/TCL
License: BSD
Requires: tk = %{version}-%{release}


%description devel
If you plan to extend Tk using its C interface, you'll need to install this
package. It contains header files and the C API documentation.
Tk is a graphical user interface toolkit that takes developing desktop
applications to a higher level than conventional approaches. Tk is the
standard GUI not only for Tcl, but for many other dynamic languages,
and can produce rich, native applications that run unchanged across
Windows, Mac OS X, Linux and more.


%files devel
%defattr(-, root, root)
%doc README changes license.terms ChangeLog*

%{_includedir}/tk.h
%{_includedir}/tkDecls.h
%{_includedir}/tkPlatDecls.h

%{_libdir}/tkConfig.sh
%{_libdir}/libtkstub8.5.a
%{_libdir}/tk8.5/tkAppInit.c

%doc %{_mandir}/man3/Tk_*.3*
%doc %{_mandir}/man3/Ttk_*.3*


%prep
%setup -q -n '%{name}%{version}'


%build
pushd 'unix'
%configure \
    --enable-threads \
    --enable-man-symlinks \
    --enable-man-compression=gzip
%{__make} %{?_smp_mflags}
popd


%install
# Avoid conflicts with ncurses:
%{__mv} doc/menubar.n doc/tk_menubar.n
%{__mv} doc/dialog.n doc/tk_dialog.n
%{__mv} doc/panedwindow.n doc/tk_panedwindow.n

%{__make} -C unix install DESTDIR='%{buildroot}'

%{__ln_s} '%{_bindir}/wish8.5' '%{buildroot}%{_bindir}/wish'

[[ -e '%{buildroot}/%{_infodir}/dir' ]] \
    && %{__rm} -f '%{buildroot}/%{_infodir}/dir'
